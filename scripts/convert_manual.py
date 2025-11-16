#!/usr/bin/env python3
"""
PDF to Markdown Converter with ASCII Art
Converts PDF manuals to Markdown with embedded ASCII art diagrams
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional
import fitz  # PyMuPDF
from PIL import Image
import numpy as np
import io


class PDFToMarkdownConverter:
    """Main converter class for PDF to Markdown with ASCII art"""

    def __init__(self, pdf_path: str, output_dir: str = "output", ascii_dir: str = "ascii",
                 ascii_width: int = 80, ascii_height: Optional[int] = None):
        """
        Initialize the converter

        Args:
            pdf_path: Path to the input PDF file
            output_dir: Directory for output markdown files
            ascii_dir: Directory for ASCII art files
            ascii_width: Width of ASCII art in characters
            ascii_height: Height of ASCII art in characters (auto if None)
        """
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.ascii_dir = Path(ascii_dir)
        self.ascii_width = ascii_width
        self.ascii_height = ascii_height

        # Create output directories
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.ascii_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectory for this PDF's ASCII art
        self.pdf_ascii_dir = self.ascii_dir / self.pdf_path.stem
        self.pdf_ascii_dir.mkdir(parents=True, exist_ok=True)

        self.doc = None

    def __enter__(self):
        """Context manager entry"""
        self.doc = fitz.open(self.pdf_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        if self.doc:
            self.doc.close()

    def image_to_ascii(self, image: Image.Image, width: int = 80, height: Optional[int] = None) -> str:
        """
        Convert PIL Image to ASCII art

        Args:
            image: PIL Image object
            width: Width of ASCII art in characters
            height: Height of ASCII art in characters (auto if None)

        Returns:
            ASCII art as string
        """
        # ASCII characters from darkest to lightest
        ASCII_CHARS = "@%#*+=-:. "

        # Convert to grayscale
        image = image.convert('L')

        # Calculate height maintaining aspect ratio if not specified
        if height is None:
            aspect_ratio = image.height / image.width
            height = int(width * aspect_ratio * 0.55)  # 0.55 to account for character aspect ratio

        # Resize image
        image = image.resize((width, height), Image.Resampling.LANCZOS)

        # Convert to numpy array
        pixels = np.array(image)

        # Normalize to 0-255
        if pixels.max() > pixels.min():
            pixels = ((pixels - pixels.min()) / (pixels.max() - pixels.min()) * 255).astype(np.uint8)
        else:
            # Handle uniform images
            pixels = np.full_like(pixels, 128, dtype=np.uint8)

        # Map pixels to ASCII characters
        ascii_art = []
        for row in pixels:
            ascii_row = ''.join([ASCII_CHARS[min(int(pixel) * len(ASCII_CHARS) // 256, len(ASCII_CHARS) - 1)] for pixel in row])
            ascii_art.append(ascii_row.rstrip())

        return '\n'.join(ascii_art)

    def extract_images_from_page(self, page_num: int) -> List[Dict]:
        """
        Extract images from a PDF page with position information

        Args:
            page_num: Page number (0-indexed)

        Returns:
            List of dicts with image info (image, bbox, position)
        """
        page = self.doc[page_num]
        images = []

        image_list = page.get_images(full=True)

        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]

            # Get image bbox (position on page)
            img_rects = page.get_image_rects(xref)
            if not img_rects:
                continue

            bbox = img_rects[0]  # Use first occurrence

            # Extract image data
            try:
                base_image = self.doc.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))

                # Filter out very small images (likely decorative elements)
                if image.width < 50 or image.height < 50:
                    continue

                images.append({
                    'image': image,
                    'bbox': bbox,
                    'y_position': bbox.y0,  # Top of image
                    'page': page_num,
                    'index': img_index
                })
            except Exception as e:
                print(f"Warning: Could not extract image {img_index} from page {page_num}: {e}")
                continue

        return images

    def extract_text_blocks(self, page_num: int) -> List[Dict]:
        """
        Extract text blocks with formatting information using PyMuPDF

        Args:
            page_num: Page number (0-indexed)

        Returns:
            List of text blocks with position and formatting info
        """
        page = self.doc[page_num]

        # Extract text blocks with font information
        blocks_data = page.get_text("dict", flags=11)["blocks"]

        blocks = []

        for block in blocks_data:
            # Only process text blocks (not images)
            if block.get("type") != 0:
                continue

            # Process each line in the block
            for line in block.get("lines", []):
                line_text = []
                font_sizes = []
                font_names = []
                y_position = line.get("bbox", [0, 0, 0, 0])[1]  # Top of line

                for span in line.get("spans", []):
                    text = span.get("text", "").strip()
                    if text:
                        line_text.append(text)
                        font_sizes.append(span.get("size", 12))
                        font_names.append(span.get("font", ""))

                if not line_text:
                    continue

                # Calculate average font size for line
                avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 12

                # Check if any font is bold
                is_bold = any(
                    'bold' in fname.lower() or 'heavy' in fname.lower() or 'black' in fname.lower()
                    for fname in font_names
                )

                blocks.append({
                    'text': ' '.join(line_text),
                    'y_position': y_position,
                    'font_size': avg_font_size,
                    'font_name': font_names[0] if font_names else '',
                    'is_bold': is_bold,
                    'page': page_num
                })

        return blocks

    def detect_heading_level(self, block: Dict, avg_font_size: float) -> int:
        """
        Detect if a text block is a heading and return its level

        Args:
            block: Text block dict
            avg_font_size: Average font size in document

        Returns:
            Heading level (1-6) or 0 if not a heading
        """
        font_size = block['font_size']
        is_bold = block['is_bold']
        text = block['text'].strip()

        # Check if text looks like a heading
        is_short = len(text) < 100
        is_title_case = text[0].isupper() if text else False

        # Determine heading level based on font size relative to average
        size_ratio = font_size / avg_font_size

        if size_ratio > 1.5 and (is_bold or is_title_case):
            return 1
        elif size_ratio > 1.3 and (is_bold or is_title_case) and is_short:
            return 2
        elif size_ratio > 1.1 and is_bold and is_short:
            return 3
        elif is_bold and is_short and is_title_case:
            return 4

        # Check for numbered sections (e.g., "1. Introduction", "1.1 Overview")
        if re.match(r'^\d+\.(\d+\.)*\s+[A-Z]', text):
            if size_ratio > 1.2:
                return 2
            else:
                return 3

        return 0

    def merge_content_by_position(self, text_blocks: List[Dict], images: List[Dict]) -> List[Dict]:
        """
        Merge text blocks and images based on their vertical position

        Args:
            text_blocks: List of text block dicts
            images: List of image dicts

        Returns:
            Merged list sorted by vertical position
        """
        content = []

        # Add text blocks
        for block in text_blocks:
            content.append({
                'type': 'text',
                'data': block,
                'y_position': block['y_position'],
                'page': block['page']
            })

        # Add images
        for img in images:
            content.append({
                'type': 'image',
                'data': img,
                'y_position': img['y_position'],
                'page': img['page']
            })

        # Sort by page, then by y_position
        content.sort(key=lambda x: (x['page'], x['y_position']))

        return content

    def convert_to_markdown(self) -> str:
        """
        Convert the entire PDF to Markdown

        Returns:
            Markdown content as string
        """
        markdown_lines = []

        # Add document title (from filename)
        title = self.pdf_path.stem.replace('-', ' ').replace('_', ' ')
        markdown_lines.append(f"# {title}\n")
        markdown_lines.append(f"*Converted from PDF: {self.pdf_path.name}*\n")
        markdown_lines.append("---\n")

        # Calculate average font size across document
        all_font_sizes = []
        for page_num in range(len(self.doc)):
            blocks = self.extract_text_blocks(page_num)
            all_font_sizes.extend([b['font_size'] for b in blocks])

        avg_font_size = np.mean(all_font_sizes) if all_font_sizes else 12

        # Process each page
        for page_num in range(len(self.doc)):
            print(f"Processing page {page_num + 1}/{len(self.doc)}...")

            # Extract text blocks and images
            text_blocks = self.extract_text_blocks(page_num)
            images = self.extract_images_from_page(page_num)

            # Merge and sort by position
            content = self.merge_content_by_position(text_blocks, images)

            # Convert to markdown
            for item in content:
                if item['type'] == 'text':
                    block = item['data']
                    text = block['text'].strip()

                    if not text:
                        continue

                    # Detect if it's a heading
                    heading_level = self.detect_heading_level(block, avg_font_size)

                    if heading_level > 0:
                        markdown_lines.append(f"\n{'#' * heading_level} {text}\n")
                    else:
                        # Regular paragraph
                        # Check if it's a list item
                        if re.match(r'^\s*[-•*]\s+', text) or re.match(r'^\s*\d+\.\s+', text):
                            markdown_lines.append(f"{text}\n")
                        else:
                            markdown_lines.append(f"{text}\n")

                elif item['type'] == 'image':
                    img_data = item['data']
                    image = img_data['image']

                    # Generate ASCII art
                    ascii_art = self.image_to_ascii(image, width=self.ascii_width, height=self.ascii_height)

                    # Save ASCII art to file
                    ascii_filename = f"page{page_num + 1}_img{img_data['index']}.txt"
                    ascii_path = self.pdf_ascii_dir / ascii_filename

                    with open(ascii_path, 'w', encoding='utf-8') as f:
                        f.write(ascii_art)

                    # Add to markdown
                    markdown_lines.append(f"\n```text\n{ascii_art}\n```\n")
                    markdown_lines.append(f"*Figure from page {page_num + 1}*\n")

            # Add page separator
            if page_num < len(self.doc) - 1:
                markdown_lines.append("\n---\n")

        return '\n'.join(markdown_lines)

    def save_markdown(self, markdown_content: str) -> Path:
        """
        Save markdown content to file

        Args:
            markdown_content: Markdown string

        Returns:
            Path to saved file
        """
        output_file = self.output_dir / f"{self.pdf_path.stem}.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"Markdown saved to: {output_file}")
        return output_file


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Convert PDF manuals to Markdown with ASCII art diagrams"
    )
    parser.add_argument(
        "pdf_path",
        help="Path to the PDF file to convert"
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory for output markdown files (default: output)"
    )
    parser.add_argument(
        "--ascii-dir",
        default="ascii",
        help="Directory for ASCII art files (default: ascii)"
    )
    parser.add_argument(
        "--ascii-width",
        type=int,
        default=192,
        help="Width of ASCII art in characters (default: 80)"
    )
    parser.add_argument(
        "--ascii-height",
        type=int,
        default=None,
        help="Height of ASCII art in characters (default: auto)"
    )

    args = parser.parse_args()

    # Validate PDF exists
    if not Path(args.pdf_path).exists():
        print(f"Error: PDF file not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)

    # Convert PDF
    print(f"Converting {args.pdf_path}...")

    with PDFToMarkdownConverter(
        pdf_path=args.pdf_path,
        output_dir=args.output_dir,
        ascii_dir=args.ascii_dir,
        ascii_width=args.ascii_width,
        ascii_height=args.ascii_height
    ) as converter:
        markdown = converter.convert_to_markdown()
        output_file = converter.save_markdown(markdown)

    print(f"✓ Conversion complete!")
    print(f"  Markdown: {output_file}")
    print(f"  ASCII art: {converter.pdf_ascii_dir}")


if __name__ == "__main__":
    main()
