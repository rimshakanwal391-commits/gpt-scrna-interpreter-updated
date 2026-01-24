# 🧬 GPT-Based scRNA-seq Marker Gene Interpreter

**Created at:** Tsinghua University Generative AI Summer School, Beijing, China  
**Date:** July 2025  
**Author:** Rimsha Kanwal  
**Affiliation:** University of Lahore, Bioinformatics Department

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📋 Overview

This project uses GPT-4's API to interpret gene marker lists from single-cell RNA-seq (scRNA-seq) data and identify cell types in accessible, non-specialist language. The tool bridges the gap between complex genomic data and clinical understanding—a critical need in healthcare settings where genetic expertise is limited.

**Key Innovation:** Applying large language models to democratize genomic data interpretation.

---

## 🎯 Problem Statement

Single-cell RNA-seq generates massive datasets identifying cell populations through marker genes. However:

- ❌ Gene symbols (CD3D, IL7R, MS4A1) are technical and opaque
- ❌ Non-specialists struggle to interpret biological meaning
- ❌ Clinical translation requires accessible explanations
- ❌ Manual interpretation is time-consuming and inconsistent

**Solution:** Use GPT-4's biological knowledge to automatically interpret marker genes and explain them in plain language.

---

## ✨ Features

✅ **Automated Cell Type Identification** - Input gene list → Get cell type  
✅ **Plain Language Explanations** - Technical genes → Understandable functions  
✅ **Biological Context** - What does this cell type do in the body?  
✅ **Clinical Relevance** - Disease implications and health significance  
✅ **Batch Processing** - Analyze multiple cell populations efficiently  
✅ **Extensible Design** - Easy to modify for other applications  

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/rimshakanwal/gpt-scrna-interpreter.git
cd gpt-scrna-interpreter

# Install dependencies
pip install openai
```

### Setup API Key

Get your OpenAI API key from [platform.openai.com](https://platform.openai.com/)

```bash
# Set environment variable
export OPENAI_API_KEY='your-api-key-here'
```

### Basic Usage

```python
from marker_interpreter import interpret_marker_genes, format_output

# Analyze Helper T cell markers
genes = ["CD3D", "CD4", "IL7R"]
result = interpret_marker_genes(genes)
print(format_output(result))
```

**Output:**
```
======================================================================
MARKER GENES: CD3D, CD4, IL7R
IDENTIFIED CELL TYPE: Helper T cells (CD4+ T cells)
======================================================================

INTERPRETATION:
1. Cell Type: Helper T cells (CD4+ T cells)
   These are immune cells that coordinate the body's response to infections.

2. Gene Functions:
   - CD3D: Essential component of the T cell receptor, enabling T cells to 
     recognize foreign invaders
   - CD4: Surface protein that defines helper T cells and helps them interact 
     with other immune cells
   - IL7R: Receptor for interleukin-7, crucial for T cell survival and development

3. Biological Role:
   Helper T cells act as coordinators of the immune system. They activate B cells 
   to produce antibodies, stimulate cytotoxic T cells to kill infected cells, and 
   regulate overall immune responses.

4. Clinical Relevance:
   Deficiency in helper T cells (as seen in HIV/AIDS) severely compromises immunity. 
   These cells are also targeted by some autoimmune diseases and immunotherapies.
```

---

## 📊 Command Line Interface

```bash
# Analyze specific genes
python marker_interpreter.py --genes CD3D CD4 IL7R

# Run demonstration mode
python marker_interpreter.py --demo

# Use custom API key
python marker_interpreter.py --genes CD19 MS4A1 --api-key YOUR_KEY
```

---

## 📓 Jupyter Notebook Tutorial

Open `tutorial.ipynb` for interactive examples covering:

1. ✅ Helper T cells identification
2. ✅ B cells analysis
3. ✅ NK cells characterization
4. ✅ Custom gene lists
5. ✅ Batch processing multiple populations
6. ✅ Reference table of common cell types

---

## 🧪 Supported Cell Types

The system can identify any cell type but has been validated on these common immune cells:

| Cell Type | Marker Genes | Key Function |
|-----------|-------------|--------------|
| Helper T cells | CD3D, CD4, IL7R | Coordinate immune responses |
| Cytotoxic T cells | CD3D, CD8A, CD8B | Kill infected cells |
| B cells | CD19, MS4A1, CD79A | Produce antibodies |
| NK cells | NCAM1, GNLY, NKG7 | Innate immune defense |
| Monocytes | CD14, LYZ, S100A8 | Phagocytosis, inflammation |
| Dendritic cells | FCER1A, CD1C, CLEC10A | Antigen presentation |
| Macrophages | CD68, CD163, MSR1 | Tissue resident immunity |
| Plasma cells | MZB1, SDC1, JCHAIN | Antibody secretion |

---

## 💻 Code Structure

```
gpt-scrna-interpreter/
├── marker_interpreter.py    # Main Python script
├── tutorial.ipynb           # Jupyter notebook with examples
├── requirements.txt         # Package dependencies
├── README.md               # This file
├── LICENSE                 # MIT license
└── examples/
    └── sample_output.txt   # Example GPT responses
```

---

## 🔬 Technical Details

### How It Works

1. **Input:** List of gene symbols (e.g., `["CD3D", "CD4", "IL7R"]`)
2. **Prompt Engineering:** Structured prompt guides GPT-4 to:
   - Identify cell type from markers
   - Explain gene functions
   - Describe biological role
   - Highlight clinical relevance
3. **API Call:** Query sent to GPT-4 via OpenAI API
4. **Parsing:** Extract cell type and formatted interpretation
5. **Output:** Structured, accessible explanation

### System Prompt

```python
SYSTEM_PROMPT = """You are an expert in single-cell biology and genomics. 
Your role is to interpret gene marker lists and identify cell types in 
clear, accessible language suitable for non-specialists.

For each gene list provided:
1. Identify the most likely cell type(s)
2. Explain what these genes do in simple terms
3. Describe the biological function of the identified cell type
4. If relevant, mention clinical or disease implications

Keep explanations concise (2-3 sentences per point) and avoid excessive 
jargon. When using technical terms, briefly explain them."""
```

### Configuration

- **Model:** GPT-4 (`gpt-4`)
- **Temperature:** 0.3 (consistent, factual responses)
- **Max Tokens:** 500 (concise explanations)

---

## 🎓 Learning Outcomes from Tsinghua

### Technical Skills
- ✅ Prompt engineering for scientific domains
- ✅ OpenAI API integration with Python
- ✅ Structuring complex biological information for AI interpretation
- ✅ Error handling and result parsing

### Key Insight
**AI can democratize access to complex scientific information.** This has direct applications to my diabetes genomics work in Pakistan, where healthcare workers often lack specialized genetics training. The same approach can explain:
- Genetic risk scores (TCF7L2, PPARG variants)
- Epigenetic modifications
- Personalized diabetes risk assessments

---

## 🌍 Real-World Applications

### 1. **Clinical Genetics**
Explain genetic test results to patients and non-specialist doctors

### 2. **Research Communication**
Help biologists interpret scRNA-seq clustering results

### 3. **Education**
Teaching tool for students learning cell biology

### 4. **Diabetes Research** (My Focus)
Adapt this approach to explain:
- Why certain genetic variants increase diabetes risk
- How epigenetic changes from diet affect disease
- Personalized risk scores for Pakistani populations

---

## 📈 Future Enhancements

Potential extensions of this project:

- [ ] **Multi-omics Integration:** Combine gene expression with protein markers
- [ ] **Disease-Specific Contexts:** Specialized prompts for cancer, diabetes, etc.
- [ ] **Visual Outputs:** Generate diagrams showing cell type relationships
- [ ] **Multi-Language Support:** Translate to Urdu for Pakistani healthcare workers
- [ ] **Web Interface:** Deploy as accessible web application
- [ ] **Validation Dataset:** Compare GPT predictions to expert annotations

---

## 🤝 Contributing

Contributions welcome! Areas for improvement:

1. Additional cell type markers (especially non-immune cells)
2. Better prompt engineering for specific tissues
3. Integration with common scRNA-seq analysis tools (Seurat, Scanpy)
4. Validation against benchmark datasets

---

## 📝 Citation

If you use this tool in your research, please cite:

```
Kanwal, R. (2025). GPT-Based scRNA-seq Marker Gene Interpreter. 
Developed at Tsinghua University Generative AI Summer School. 
GitHub: https://github.com/rimshakanwal/gpt-scrna-interpreter
```

---

## ⚖️ License

MIT License - See LICENSE file for details

---

## 📧 Contact

**Rimsha Kanwal**  
- Email: rimshakanwal391@gmail.com
- GitHub: [@rimshakanwal](https://github.com/rimshakanwal)
- Portfolio: [rimshakanwal.github.io](https://rimshakanwal.github.io)

---

## 🙏 Acknowledgments

- **Tsinghua University** - Generative AI Summer School, July 2025
- **OpenAI** - GPT-4 API and excellent documentation
- **scRNA-seq Community** - For marker gene databases and resources

---

## 📚 Related Projects

- [Diabetes Genomics Pipeline](https://github.com/rimshakanwal/diabetes-genomics-pakistan) - My main research project
- [Seurat](https://satijalab.org/seurat/) - Popular scRNA-seq analysis toolkit
- [Scanpy](https://scanpy.readthedocs.io/) - Python-based scRNA-seq analysis

---

## ⚠️ Disclaimer

This tool is for research and educational purposes. While GPT-4 has extensive biological knowledge, always validate interpretations with literature and domain experts before making clinical decisions.

---

**🌟 Star this repo if you find it useful!**

Built with ❤️ in Beijing | For accessible genomics worldwide