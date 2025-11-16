# Quick Start Guide

## Installation

```bash
pip install -r requirements.txt
```

## Basic Usage

### Convert a single PDF

```bash
python scripts/convert_manual.py INPUT.pdf
```

### Convert with custom ASCII width

```bash
python scripts/convert_manual.py INPUT.pdf --ascii-width 120
```

### View all options

```bash
python scripts/convert_manual.py --help
```

## Output

After conversion, you'll find:

- **Markdown file**: `output/<pdf-name>.md`
- **ASCII art files**: `ascii/<pdf-name>/page*.txt`

## Examples

### Example 1: Convert cover page

```bash
python scripts/convert_manual.py COVER-OCR.PDF
```

Output:
- `output/COVER-OCR.md` - Full markdown document
- `ascii/COVER-OCR/page1_img0.txt` - ASCII art logo

### Example 2: Convert technical manual with diagrams

```bash
python scripts/convert_manual.py "I-SECTION-1.-OSP7030M-730M-SPECIFICATIONS-OCR.PDF" --ascii-width 100
```

Output:
- `output/I-SECTION-1.-OSP7030M-730M-SPECIFICATIONS-OCR.md`
- `ascii/I-SECTION-1.-OSP7030M-730M-SPECIFICATIONS-OCR/page*.txt` (9 files)

## Automated Workflow

The GitHub Actions workflow automatically converts PDFs when you:

1. Add a `.pdf` file to the repository
2. Push to GitHub
3. Wait for the action to complete
4. Results are auto-committed back to the repo

## Tips for Best Results

### ASCII Art Quality

- **Higher width = more detail**: Use `--ascii-width 120` or higher for detailed diagrams
- **Aspect ratio**: Height is automatically calculated to maintain proportions
- **Source quality**: Better quality PDF images produce better ASCII art

### Heading Detection

The script automatically detects headings based on:
- Font size (larger = higher level heading)
- Bold text
- Numbered sections (e.g., "1.2 Introduction")

### Custom ASCII Characters

To customize the ASCII character set, edit `scripts/convert_manual.py`:

```python
ASCII_CHARS = "@%#*+=-:. "  # From darkest to lightest
```

Example alternatives:
- High contrast: `"@#%*+=-:. "`
- Blocks: `"█▓▒░ "`
- Simple: `"#*+. "`

## Troubleshooting

### Issue: Poor ASCII quality

**Solution**: Increase ASCII width
```bash
python scripts/convert_manual.py INPUT.pdf --ascii-width 150
```

### Issue: Headings not detected

**Cause**: OCR'd PDFs may lack font size information

**Solution**: The script uses multiple heuristics including:
- Font size analysis
- Bold detection
- Numbered section detection
- Short text with title case

### Issue: Images not appearing

**Cause**: Images smaller than 50x50 pixels are filtered out as decorative

**Solution**: Adjust the threshold in `scripts/convert_manual.py`:
```python
if image.width < 50 or image.height < 50:  # Change these values
    continue
```

## Advanced Usage

### Batch convert all PDFs in directory

```bash
for pdf in *.pdf; do
    python scripts/convert_manual.py "$pdf" --ascii-width 100
done
```

### Convert with specific output directories

```bash
python scripts/convert_manual.py INPUT.pdf \
    --output-dir my_markdown \
    --ascii-dir my_ascii
```

### Generate compact ASCII (smaller files)

```bash
python scripts/convert_manual.py INPUT.pdf --ascii-width 60
```

### Generate detailed ASCII (larger files, better quality)

```bash
python scripts/convert_manual.py INPUT.pdf --ascii-width 140
```

## Markdown Output Format

The generated Markdown includes:

```markdown
# Document Title
*Converted from PDF: filename.pdf*
---

## Detected Heading

Regular paragraph text...

```text
ASCII art diagram
```
*Figure from page 2*

---
(page separator)
```

This format is compatible with:
- GitHub/GitLab rendering
- Static site generators (Jekyll, Hugo, etc.)
- Markdown editors (Typora, Mark Text, etc.)
- Documentation systems (MkDocs, Docusaurus, etc.)

## Performance

Typical conversion times:
- Small PDF (1-5 pages): ~5-10 seconds
- Medium PDF (10-20 pages): ~20-40 seconds
- Large PDF (50+ pages): ~2-5 minutes

Factors affecting speed:
- Number of images
- Image resolution
- ASCII width setting
- Number of pages
