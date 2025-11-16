#!/usr/bin/env python3
"""
Advanced PDF to Markdown Converter
Converts PDF manuals to Markdown with:
- Markdown pipe tables
- Box-drawing character diagrams
- Text-based charts and graphs
- Proper structure preservation
"""

import os
import sys
import re
import argparse
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
import fitz  # PyMuPDF
import pdfplumber
from PIL import Image
import numpy as np
import cv2
import io


class AdvancedPDFConverter:
    """Advanced PDF to Markdown converter with table/diagram support"""

    # Box-drawing characters for better diagram rendering
    BOX_CHARS = {
        'horizontal': '─',
        'vertical': '│',
        'top_left': '┌',
        'top_right': '┐',
        'bottom_left': '└',
        'bottom_right': '┘',
        'cross': '┼',
        't_down': '┬',
        't_up': '┴',
        't_right': '├',
        't_left': '┤',
        'heavy_horizontal': '━',
        'heavy_vertical': '┃',
        'double_horizontal': '═',
        'double_vertical': '║',
    }

    def __init__(self, pdf_path: str, output_dir: str = "output", ascii_dir: str = "ascii",
                 diagram_width: int = 100, enable_tables: bool = True):
        """
        Initialize the converter

        Args:
            pdf_path: Path to the input PDF file
            output_dir: Directory for output markdown files
            ascii_dir: Directory for diagram files
            diagram_width: Width of diagrams in characters
            enable_tables: Enable table extraction
        """
        self.pdf_path = Path(pdf_path)
        self.output_dir = Path(output_dir)
        self.ascii_dir = Path(ascii_dir)
        self.diagram_width = diagram_width
        self.enable_tables = enable_tables

        # Create output directories
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.ascii_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectory for this PDF's diagrams
        self.pdf_ascii_dir = self.ascii_dir / self.pdf_path.stem
        self.pdf_ascii_dir.mkdir(parents=True, exist_ok=True)

        self.fitz_doc = None
        self.plumber_pdf = None

    def __enter__(self):
        """Context manager entry"""
        self.fitz_doc = fitz.open(self.pdf_path)
        self.plumber_pdf = pdfplumber.open(self.pdf_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        if self.fitz_doc:
            self.fitz_doc.close()
        if self.plumber_pdf:
            self.plumber_pdf.close()

    def image_to_box_drawing(self, image: Image.Image, width: int = 100) -> str:
        """
        Convert image to box-drawing character art using edge detection

        Args:
            image: PIL Image object
            width: Width in characters

        Returns:
            Box-drawing character art as string
        """
        # Convert to numpy array
        img_array = np.array(image)

        # Convert to grayscale based on number of channels
        if len(img_array.shape) == 2:
            # Already grayscale
            gray = img_array
        elif img_array.shape[2] == 4:
            # RGBA
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGBA2GRAY)
        elif img_array.shape[2] == 3:
            # RGB
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else:
            # Unknown format, convert via PIL
            gray = np.array(image.convert('L'))

        # Calculate height maintaining aspect ratio
        aspect_ratio = gray.shape[0] / gray.shape[1]
        height = int(width * aspect_ratio * 0.5)  # 0.5 for character aspect

        # Resize
        resized = cv2.resize(gray, (width, height), interpolation=cv2.INTER_AREA)

        # Edge detection
        edges = cv2.Canny(resized, 50, 150)

        # Convert to box-drawing characters
        result = []
        for y in range(height):
            row = []
            for x in range(width):
                if edges[y, x] > 128:
                    # Check neighbors to determine box character
                    has_top = y > 0 and edges[y-1, x] > 128
                    has_bottom = y < height-1 and edges[y+1, x] > 128
                    has_left = x > 0 and edges[y, x-1] > 128
                    has_right = x < width-1 and edges[y, x+1] > 128

                    # Vertical or horizontal line
                    if (has_top or has_bottom) and not (has_left or has_right):
                        row.append(self.BOX_CHARS['vertical'])
                    elif (has_left or has_right) and not (has_top or has_bottom):
                        row.append(self.BOX_CHARS['horizontal'])
                    elif has_top and has_bottom and has_left and has_right:
                        row.append(self.BOX_CHARS['cross'])
                    elif has_top and has_left:
                        row.append(self.BOX_CHARS['bottom_right'])
                    elif has_top and has_right:
                        row.append(self.BOX_CHARS['bottom_left'])
                    elif has_bottom and has_left:
                        row.append(self.BOX_CHARS['top_right'])
                    elif has_bottom and has_right:
                        row.append(self.BOX_CHARS['top_left'])
                    elif has_top or has_bottom:
                        row.append(self.BOX_CHARS['vertical'])
                    elif has_left or has_right:
                        row.append(self.BOX_CHARS['horizontal'])
                    else:
                        row.append('•')
                else:
                    # Use density for non-edge pixels
                    if resized[y, x] < 50:
                        row.append('█')
                    elif resized[y, x] < 100:
                        row.append('▓')
                    elif resized[y, x] < 150:
                        row.append('▒')
                    elif resized[y, x] < 200:
                        row.append('░')
                    else:
                        row.append(' ')
            result.append(''.join(row).rstrip())

        return '\n'.join(result)

    def extract_tables_from_page(self, page_num: int) -> List[Dict]:
        """
        Extract tables from a PDF page (both text and visual tables)

        Args:
            page_num: Page number (0-indexed)

        Returns:
            List of table dicts with data and position
        """
        if not self.enable_tables:
            return []

        tables = []

        # Try pdfplumber first (for text-based tables)
        page = self.plumber_pdf.pages[page_num]
        page_tables = page.extract_tables()

        for table_idx, table_data in enumerate(page_tables):
            if not table_data or len(table_data) == 0:
                continue

            # Clean up table data
            cleaned_table = []
            for row in table_data:
                cleaned_row = []
                for cell in row:
                    if cell is None:
                        cleaned_row.append('')
                    else:
                        # Clean up cell text
                        cleaned_cell = str(cell).strip().replace('\n', ' ')
                        cleaned_row.append(cleaned_cell)
                cleaned_table.append(cleaned_row)

            # Filter out empty tables
            if any(any(cell for cell in row) for row in cleaned_table):
                tables.append({
                    'data': cleaned_table,
                    'page': page_num,
                    'index': table_idx,
                    'y_position': 0  # pdfplumber doesn't give position easily
                })

        # Also try PyMuPDF's visual table detection (for OCR'd/image tables)
        fitz_page = self.fitz_doc[page_num]
        try:
            # Find tables visually
            fitz_tables = fitz_page.find_tables()

            for table_idx, table in enumerate(fitz_tables):
                # Extract table data
                table_data = table.extract()

                if table_data and len(table_data) > 0:
                    # Clean up table data
                    cleaned_table = []
                    for row in table_data:
                        cleaned_row = []
                        for cell in row:
                            if cell is None:
                                cleaned_row.append('')
                            else:
                                cleaned_cell = str(cell).strip().replace('\n', ' ')
                                cleaned_row.append(cleaned_cell)
                        cleaned_table.append(cleaned_row)

                    # Filter out empty tables
                    if any(any(cell for cell in row) for row in cleaned_table):
                        tables.append({
                            'data': cleaned_table,
                            'page': page_num,
                            'index': len(tables),
                            'y_position': table.bbox[1]  # Top y position
                        })
        except Exception as e:
            print(f"Warning: Could not extract visual tables from page {page_num}: {e}")

        return tables

    def table_to_markdown(self, table_data: List[List[str]]) -> str:
        """
        Convert table data to Markdown pipe table

        Args:
            table_data: 2D list of table cells

        Returns:
            Markdown table as string
        """
        if not table_data or len(table_data) == 0:
            return ""

        # Determine column widths
        num_cols = max(len(row) for row in table_data)
        col_widths = [0] * num_cols

        # Normalize rows to same length
        normalized_table = []
        for row in table_data:
            normalized_row = row + [''] * (num_cols - len(row))
            normalized_table.append(normalized_row)
            for i, cell in enumerate(normalized_row):
                col_widths[i] = max(col_widths[i], len(str(cell)))

        # Build markdown table
        lines = []

        # First row as header
        header = normalized_table[0]
        header_line = '| ' + ' | '.join(
            str(cell).ljust(col_widths[i]) for i, cell in enumerate(header)
        ) + ' |'
        lines.append(header_line)

        # Separator
        separator = '|' + '|'.join('-' * (w + 2) for w in col_widths) + '|'
        lines.append(separator)

        # Data rows
        for row in normalized_table[1:]:
            row_line = '| ' + ' | '.join(
                str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)
            ) + ' |'
            lines.append(row_line)

        return '\n'.join(lines)

    def extract_images_from_page(self, page_num: int) -> List[Dict]:
        """
        Extract images from a PDF page

        Args:
            page_num: Page number (0-indexed)

        Returns:
            List of image dicts with data and position
        """
        page = self.fitz_doc[page_num]
        images = []

        image_list = page.get_images(full=True)

        for img_index, img_info in enumerate(image_list):
            xref = img_info[0]

            # Get image position
            img_rects = page.get_image_rects(xref)
            if not img_rects:
                continue

            bbox = img_rects[0]

            try:
                base_image = self.fitz_doc.extract_image(xref)
                image_bytes = base_image["image"]
                image = Image.open(io.BytesIO(image_bytes))

                # Filter tiny images
                if image.width < 30 or image.height < 30:
                    continue

                images.append({
                    'image': image,
                    'bbox': bbox,
                    'y_position': bbox.y0,
                    'page': page_num,
                    'index': img_index,
                    'width': image.width,
                    'height': image.height
                })
            except Exception as e:
                print(f"Warning: Could not extract image {img_index} from page {page_num}: {e}")
                continue

        return images

    def extract_text_blocks(self, page_num: int) -> List[Dict]:
        """
        Extract text blocks with formatting

        Args:
            page_num: Page number (0-indexed)

        Returns:
            List of text blocks with formatting info
        """
        page = self.plumber_pdf.pages[page_num]

        # Get words with formatting
        words = page.extract_words(extra_attrs=['fontname', 'size', 'object_type'])

        if not words:
            return []

        # Group words into lines
        lines = []
        current_line = {
            'words': [],
            'y_position': words[0]['top'],
            'x_start': words[0]['x0'],
        }

        for word in words:
            # Check if new line (y position changed significantly)
            if abs(word['top'] - current_line['y_position']) > 2:
                if current_line['words']:
                    lines.append(current_line)
                current_line = {
                    'words': [word],
                    'y_position': word['top'],
                    'x_start': word['x0'],
                }
            else:
                current_line['words'].append(word)

        if current_line['words']:
            lines.append(current_line)

        # Convert lines to blocks
        blocks = []
        for line in lines:
            words_list = line['words']
            text = ' '.join(w['text'] for w in words_list)

            # Calculate average font size
            font_sizes = [w.get('size', 12) for w in words_list]
            avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 12

            # Check if bold
            font_names = [w.get('fontname', '') for w in words_list]
            is_bold = any('bold' in fn.lower() or 'heavy' in fn.lower() or 'black' in fn.lower()
                         for fn in font_names if fn)

            blocks.append({
                'text': text.strip(),
                'y_position': line['y_position'],
                'x_start': line['x_start'],
                'font_size': avg_font_size,
                'is_bold': is_bold,
                'page': page_num
            })

        return blocks

    def detect_heading_level(self, block: Dict, avg_font_size: float) -> int:
        """
        Detect heading level

        Args:
            block: Text block
            avg_font_size: Average font size in document

        Returns:
            Heading level (1-6) or 0 if not a heading
        """
        font_size = block['font_size']
        is_bold = block['is_bold']
        text = block['text']

        if not text:
            return 0

        # Check for numbered sections
        if re.match(r'^\d+\.\s+[A-Z]', text):
            return 2
        if re.match(r'^\d+\.\d+\s+[A-Z]', text):
            return 3
        if re.match(r'^\d+\.\d+\.\d+\s+[A-Z]', text):
            return 4

        # Check font size
        size_ratio = font_size / avg_font_size

        is_short = len(text) < 80
        is_title_case = text[0].isupper()

        if size_ratio > 1.5 and (is_bold or is_title_case):
            return 1
        elif size_ratio > 1.3 and is_bold and is_short:
            return 2
        elif size_ratio > 1.15 and is_bold and is_short:
            return 3
        elif is_bold and is_short and is_title_case and len(text) < 50:
            return 4

        return 0

    def is_list_item(self, text: str) -> bool:
        """Check if text is a list item"""
        return bool(re.match(r'^\s*[-•*]\s+', text) or re.match(r'^\s*\d+\.\s+', text))

    def detect_table_from_layout(self, blocks: List[Dict]) -> Optional[List[List[str]]]:
        """
        Try to detect table structure from text block positions

        Args:
            blocks: List of text blocks with position info

        Returns:
            Table data as 2D list if table detected, None otherwise
        """
        if len(blocks) < 3:  # Need at least a few blocks for a table
            return None

        # Group blocks by y position (rows)
        rows = {}
        for block in blocks:
            y = round(block['y_position'] / 5) * 5  # Snap to 5pt grid
            if y not in rows:
                rows[y] = []
            rows[y].append(block)

        # Sort rows by y position
        sorted_rows = sorted(rows.items())

        # Check if this looks like a table (multiple rows with similar x positions)
        if len(sorted_rows) < 2:
            return None

        # Collect all x positions across rows
        all_x_positions = set()
        for y, row_blocks in sorted_rows:
            for block in row_blocks:
                x = round(block['x_start'] / 10) * 10  # Snap to 10pt grid
                all_x_positions.add(x)

        # If we have consistent columns, this might be a table
        if len(all_x_positions) < 2:
            return None

        # Sort x positions to create columns
        x_positions = sorted(all_x_positions)

        # Build table
        table = []
        for y, row_blocks in sorted_rows:
            row = [''] * len(x_positions)
            for block in row_blocks:
                x = round(block['x_start'] / 10) * 10
                if x in x_positions:
                    col_idx = x_positions.index(x)
                    row[col_idx] = block['text']
            table.append(row)

        # Check if it looks like a real table (not just random text)
        non_empty_cells = sum(1 for row in table for cell in row if cell)
        if non_empty_cells < len(table) * 2:  # At least 2 cells per row
            return None

        return table

    def convert_to_markdown(self) -> str:
        """
        Convert PDF to Markdown

        Returns:
            Markdown content as string
        """
        markdown_lines = []

        # Add title
        title = self.pdf_path.stem.replace('-', ' ').replace('_', ' ')
        markdown_lines.append(f"# {title}\n")
        markdown_lines.append(f"*Converted from PDF: {self.pdf_path.name}*\n")
        markdown_lines.append("---\n")

        # Calculate average font size
        all_font_sizes = []
        for page_num in range(len(self.plumber_pdf.pages)):
            blocks = self.extract_text_blocks(page_num)
            all_font_sizes.extend([b['font_size'] for b in blocks])

        avg_font_size = np.mean(all_font_sizes) if all_font_sizes else 12

        # Process each page
        for page_num in range(len(self.fitz_doc)):
            print(f"Processing page {page_num + 1}/{len(self.fitz_doc)}...")

            # Extract content
            text_blocks = self.extract_text_blocks(page_num)
            tables = self.extract_tables_from_page(page_num)
            images = self.extract_images_from_page(page_num)

            # Process tables first (they take priority)
            if tables:
                markdown_lines.append("\n")
                for table in tables:
                    table_md = self.table_to_markdown(table['data'])
                    markdown_lines.append(table_md)
                    markdown_lines.append("\n")

            # Process text blocks
            prev_was_heading = False
            for block in text_blocks:
                text = block['text']
                if not text:
                    continue

                # Skip text that's part of tables (heuristic)
                if len(text) < 3:
                    continue

                # Detect heading
                heading_level = self.detect_heading_level(block, avg_font_size)

                if heading_level > 0:
                    markdown_lines.append(f"\n{'#' * heading_level} {text}\n")
                    prev_was_heading = True
                elif self.is_list_item(text):
                    markdown_lines.append(f"{text}\n")
                    prev_was_heading = False
                else:
                    # Regular paragraph
                    if not prev_was_heading:
                        markdown_lines.append("\n")
                    markdown_lines.append(f"{text}\n")
                    prev_was_heading = False

            # Process images/diagrams
            for img_data in images:
                image = img_data['image']

                # Generate box-drawing diagram
                try:
                    diagram = self.image_to_box_drawing(image, width=self.diagram_width)

                    # Save diagram
                    diagram_filename = f"page{page_num + 1}_img{img_data['index']}.txt"
                    diagram_path = self.pdf_ascii_dir / diagram_filename

                    with open(diagram_path, 'w', encoding='utf-8') as f:
                        f.write(diagram)

                    # Add to markdown
                    markdown_lines.append(f"\n```text\n{diagram}\n```\n")
                    markdown_lines.append(f"*Figure from page {page_num + 1} "
                                        f"({img_data['width']}x{img_data['height']} px)*\n")
                except Exception as e:
                    print(f"Warning: Could not convert image to diagram: {e}")
                    markdown_lines.append(f"\n*[Image: page {page_num + 1}, "
                                        f"{img_data['width']}x{img_data['height']} px]*\n")

            # Page separator
            if page_num < len(self.fitz_doc) - 1:
                markdown_lines.append("\n---\n")

        return '\n'.join(markdown_lines)

    def save_markdown(self, markdown_content: str) -> Path:
        """
        Save markdown to file

        Args:
            markdown_content: Markdown string

        Returns:
            Path to saved file
        """
        output_file = self.output_dir / f"{self.pdf_path.stem}.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"✓ Markdown saved to: {output_file}")
        return output_file


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Advanced PDF to Markdown converter with tables and diagrams"
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
        help="Directory for diagram files (default: ascii)"
    )
    parser.add_argument(
        "--diagram-width",
        type=int,
        default=100,
        help="Width of diagrams in characters (default: 100)"
    )
    parser.add_argument(
        "--no-tables",
        action="store_true",
        help="Disable table extraction"
    )

    args = parser.parse_args()

    # Validate PDF exists
    if not Path(args.pdf_path).exists():
        print(f"Error: PDF file not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)

    # Convert PDF
    print(f"Converting {args.pdf_path}...")

    with AdvancedPDFConverter(
        pdf_path=args.pdf_path,
        output_dir=args.output_dir,
        ascii_dir=args.ascii_dir,
        diagram_width=args.diagram_width,
        enable_tables=not args.no_tables
    ) as converter:
        markdown = converter.convert_to_markdown()
        output_file = converter.save_markdown(markdown)

    print(f"✓ Conversion complete!")
    print(f"  Markdown: {output_file}")
    print(f"  Diagrams: {converter.pdf_ascii_dir}")


if __name__ == "__main__":
    main()
