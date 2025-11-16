# PDF to Markdown Conversion Pipeline

Automated pipeline that converts PDF manuals to Markdown format with ASCII art representations of embedded images and diagrams.

## Features

- **Automatic Conversion**: Upload a PDF and get Markdown automatically
- **ASCII Art Diagrams**: All images converted to ASCII art
- **Structure Preservation**: Headings, paragraphs, and lists maintained
- **Position-Aware**: Images inserted at correct positions
- **GitHub Actions Integration**: Fully automated workflow

## Directory Structure

```
project-manual/
├── scripts/
│   └── convert_manual.py       # Main conversion script
├── ascii/
│   └── <pdf-name>/             # ASCII art files per PDF
│       ├── page1_img0.txt
│       ├── page2_img0.txt
│       └── ...
├── output/
│   └── <pdf-name>.md           # Converted Markdown files
├── .github/
│   └── workflows/
│       └── convert-pdf.yml     # GitHub Actions workflow
└── requirements.txt            # Python dependencies
```

## Usage

### Automatic (via GitHub Actions)

1. **Upload a PDF file** to the repository
2. **Push to GitHub** - the workflow triggers automatically
3. **Wait for conversion** - GitHub Actions runs the pipeline
4. **Results committed** - Markdown and ASCII files auto-committed

### Manual (command line)

```bash
# Install dependencies
pip install -r requirements.txt

# Convert a single PDF
python scripts/convert_manual.py INPUT.pdf

# Custom options
python scripts/convert_manual.py INPUT.pdf \
  --output-dir output \
  --ascii-dir ascii \
  --ascii-width 100 \
  --ascii-height 40
```

### Manual Trigger (GitHub Actions)

You can manually trigger the workflow from the Actions tab:
1. Go to **Actions** → **Convert PDF to Markdown**
2. Click **Run workflow**
3. Optionally specify a PDF file to convert

## Command Line Options

| Option | Default | Description |
|--------|---------|-------------|
| `pdf_path` | - | Path to PDF file (required) |
| `--output-dir` | `output` | Directory for Markdown files |
| `--ascii-dir` | `ascii` | Directory for ASCII art files |
| `--ascii-width` | `80` | Width of ASCII art in characters |
| `--ascii-height` | `auto` | Height (auto maintains aspect ratio) |

## How It Works

### 1. PDF Analysis
- Extracts text blocks with font and position information
- Extracts embedded images with bounding boxes
- Analyzes document structure

### 2. Heading Detection
- Identifies headings by font size, bold text, and numbering
- Converts to Markdown heading levels (#, ##, ###, etc.)
- Preserves document hierarchy

### 3. ASCII Art Conversion
- Converts images to grayscale
- Resizes to target character dimensions
- Maps pixel brightness to ASCII characters: `@%#*+=-:. `
- Saves each diagram as a separate .txt file

### 4. Markdown Reconstruction
- Merges text and images by vertical position
- Inserts ASCII art in code blocks at correct locations
- Preserves lists, paragraphs, and formatting
- Adds page separators

### 5. Output Generation
```markdown
# Document Title

## Section Heading

Regular paragraph text...

```text
ASCII art diagram here...
```
*Figure from page 2*

---
```

## Dependencies

- **PyMuPDF (fitz)**: PDF text and image extraction
- **pdfplumber**: Enhanced text extraction with font info
- **Pillow**: Image processing
- **OpenCV**: Advanced image operations
- **NumPy**: Numerical operations

## GitHub Actions Workflow

The workflow automatically:
1. Triggers on any `.pdf` file push
2. Sets up Python 3.11 environment
3. Installs dependencies
4. Detects changed PDF files
5. Converts each PDF to Markdown
6. Commits results back to the repository

## Customization

### ASCII Art Density

Adjust the character set in `convert_manual.py`:
```python
ASCII_CHARS = "@%#*+=-:. "  # Dense to sparse
```

### Heading Detection

Tune font size ratios in `detect_heading_level()`:
```python
if size_ratio > 1.5:  # Adjust threshold
    return 1  # H1
```

### Image Filtering

Change minimum image size to filter decorative elements:
```python
if image.width < 50 or image.height < 50:  # Adjust threshold
    continue
```

## Examples

### Input PDF
- Technical manual with diagrams
- Circuit diagrams
- Flowcharts
- Tables and figures

### Output Markdown
- Fully structured document
- ASCII representations of all visuals
- Searchable and version-controllable
- Human-readable diagrams

## Troubleshooting

### No output files generated
- Check GitHub Actions logs for errors
- Ensure PDF is not corrupted
- Verify dependencies are installed

### Poor ASCII art quality
- Increase `--ascii-width` for more detail
- Check source image quality in PDF
- Adjust ASCII_CHARS for better contrast

### Incorrect heading detection
- PDFs must have font size/style information
- OCR'd PDFs may need manual heading markers
- Tune detection thresholds in code

## Contributing

Improvements welcome:
- Better heading detection algorithms
- Enhanced ASCII art quality
- Table extraction support
- Multi-column layout handling

## License

MIT License - See repository for details
