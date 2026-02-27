# Contributing to S<sup>2</sup>-PEPANALYST

Thank you for your interest! Contributions that extend S<sup>2</sup>-PEPANALYST to new species, improve embeddings, or enhance the CNN are very welcome.

## 🐛 Reporting Bugs

Open a [GitHub Issue](https://github.com/MorillaLab/s2-PEPANALYST/issues) with:
- The notebook or script where the error occurs
- Your environment (OS, Python version, PyTorch version, TAPE/ESM version)
- The full error traceback
- A minimal example if possible (sequence, input format)

## 💡 Suggesting Features

Open an issue tagged `enhancement`. Good examples:
- Support for a new plant species / genome
- Alternative protein embedding (ProtTrans, AlphaFold representations)
- Improved topological feature extraction
- Web tool integration

## 🔧 Submitting Code

1. Fork the repository and create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install flake8
   ```
3. Make your changes. For new species, add sequences to `data/` and document the source (NCBI accession, database version).
4. Lint Python files:
   ```bash
   flake8 code/*.py --max-line-length=127
   ```
5. Clear notebook outputs before committing.
6. Open a pull request against `main` with a clear description and any relevant biological context.

## 📋 Data Contributions

If contributing new sequence data, please ensure:
- Sequences are from a publicly available database (NCBI, UniProt, TAIR)
- Accession numbers are documented
- No proprietary or restricted data is included

## 📜 License

By contributing, you agree your work will be released under GPL-3.0.
