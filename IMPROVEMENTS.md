# PDF Converter Improvements

## Problem with Original Version

The basic pixel-to-ASCII conversion was producing **garbage output**:
- Unreadable diagrams using only `@%#*+=-:. `
- No table support
- Broken text extraction
- Poor quality for technical CNC manuals

## New Advanced Converter

### ✨ Key Improvements

#### 1. **Box-Drawing Character Diagrams**
Uses proper Unicode box-drawing characters for clean technical diagrams:

```
┌───────────────┐
│  Component A  │
├───────────────┤
│  Component B  │
└───────────────┘
```

**Characters used:**
- Lines: `─│┌┐└┘`
- Intersections: `┼┬┴├┤`
- Shading: `█▓▒░`
- Points: `•`

#### 2. **Edge Detection for Diagrams**
- Uses OpenCV Canny edge detection
- Analyzes neighbors to choose correct box characters
- Produces crisp, readable technical schematics
- Much better for CNC control panels, state diagrams, flowcharts

#### 3. **Table Detection (Multiple Methods)**
- **pdfplumber**: Extracts text-based tables
- **PyMuPDF visual detection**: Finds table structure in images
- **Spatial layout analysis**: Reconstructs tables from text positions
- Outputs proper Markdown pipe tables:

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |
```

#### 4. **Better Text Extraction**
- Uses pdfplumber for word-level extraction with font info
- Preserves spatial layout
- Better heading detection (font size, bold, numbering)
- Proper paragraph reconstruction

### 🔧 Technical Details

**Libraries:**
- `PyMuPDF (fitz)` - PDF parsing, image extraction, visual table detection
- `pdfplumber` - Word-level text extraction, text-based table detection
- `opencv-python` - Edge detection (Canny algorithm)
- `Pillow` - Image processing
- `numpy` - Array operations

**Algorithms:**
1. **Edge Detection:**
   ```python
   edges = cv2.Canny(image, 50, 150)  # Detect edges
   # Analyze 4-neighbors to determine box character
   ```

2. **Box Character Selection:**
   - Check if pixel is an edge
   - Examine top/bottom/left/right neighbors
   - Select appropriate Unicode character (corner, line, cross, etc.)

3. **Density Shading:**
   - For non-edge pixels, map brightness to shading chars
   - `< 50: █, < 100: ▓, < 150: ▒, < 200: ░, else: space`

4. **Table Detection:**
   - Try pdfplumber's built-in table extraction
   - Try PyMuPDF's visual `find_tables()`
   - Fallback to spatial layout analysis (group by y-pos, align by x-pos)

### 📊 Results

**OLD Output:**
```
::::  ::::: ::::
 --   +***  --
  ::    ::  +++
```
Completely unreadable.

**NEW Output:**
```
┌──────────────┐
│   ░░░░░░░░   │
├──────┬───────┤
│  ██  │  ▒▒  │
└──────┴───────┘
```
Clean, structured, readable.

### 🎯 Best For

- CNC machine manuals
- Technical specifications with tables
- Control panel layouts
- State diagrams and flowcharts
- Circuit diagrams
- Any technical documentation with structured data

### 💡 Usage Tips

**For maximum quality:**
```bash
python scripts/convert_manual.py manual.pdf --diagram-width 120
```

**Wider diagrams = more detail:**
- 80 chars: Compact (default)
- 100 chars: Balanced
- 120 chars: Detailed (recommended)
- 150+ chars: Maximum detail

**For text-heavy docs (disable diagrams):**
```bash
python scripts/convert_manual.py manual.pdf --no-tables
```

### ⚠️ Limitations

**OCR'd PDFs:**
- Tables embedded as images are hard to extract
- May not detect all table structures
- Text extraction depends on OCR quality

**Complex Diagrams:**
- Very detailed schematics may still be hard to represent in text
- Color information is lost (converted to grayscale)
- 3D diagrams flatten to 2D

**Solutions:**
- For tables: Spatial layout analyzer tries to reconstruct structure
- For complex diagrams: Increase width to 150+ characters
- For color: Represented as density/shading

### 🔄 Future Improvements

Potential enhancements:
- [ ] Add pytesseract for re-OCR of table images
- [ ] Better math equation detection/rendering
- [ ] Chart/graph specific rendering (bar charts, line graphs)
- [ ] Multi-column text layout handling
- [ ] Improved CNC G-code formatting detection
- [ ] Table header detection and preservation

### 📚 Example Files

Test the converter on the included PDFs:
- `COVER-OCR.PDF` - Logo rendering
- `I-SECTION-1.-OSP7030M-730M-SPECIFICATIONS-OCR.PDF` - Tables and diagrams
- `II-SECTION-3-MANUAL-FUNCTIONS-OCR.PDF` - Control panel layouts

Each produces:
- `output/<name>.md` - Markdown file
- `ascii/<name>/page*.txt` - Individual diagrams

---

**Bottom line:** The new converter is **massively better** for technical manuals with tables, charts, and CNC diagrams.
