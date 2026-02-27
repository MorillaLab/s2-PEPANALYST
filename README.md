<div align="center">

# 🌿 S<sup>2</sup>-PEPANALYST

### Small Signalling Peptide Analysis in Plant Systems

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://choosealicense.com/licenses/gpl-3.0/)
[![DOI](https://img.shields.io/badge/DOI-10.1111%2Fpbi.70536-blue)](https://doi.org/10.1111/pbi.70536)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/MorillaLab/s2-PEPANALYST/graphs/commit-activity)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MorillaLab/s2-PEPANALYST/blob/main/code/)

**S<sup>2</sup>-PEPANALYST** is a deep learning pipeline for predicting and functionally classifying small signalling peptides (SSPs) in plant genomes — combining protein language model embeddings (TAPE & ESM), topological data analysis (TDA), and a LeNet-inspired convolutional neural network.

📄 Published in *Plant Biotechnology Journal* · 🌱 Validated on *Arabidopsis*, tomato, avocado · 🔬 Scale-invariant functional annotation

[📄 Paper](#-citation) · [🚀 Quick Start](#-quick-start) · [🏗️ Architecture](#️-architecture) · [🌱 Supported Species](#-supported-species) · [⚙️ Methods](#️-methods)

</div>

---

## 🔍 Overview

Small signalling peptides (SSPs) are short secreted proteins that act as ligands in plant cell-to-cell communication, regulating development, immunity, and stress responses. Their computational identification remains challenging due to high sequence diversity, short length (≤ 200 aa), and the need to distinguish truly *functional* signalling domains from background sequence.

**S<sup>2</sup>-PEPANALYST** tackles this by:

1. **Embedding** protein sequences using TAPE (768-dim) and ESM (high-dim) protein language models
2. **Optimisation** embedding best selection based on an agentic reinforcement learning model
3. **Converting** embeddings to 2D image representations (28×28 and 32×32) for spatial feature capture
4. **Enriching** with **GeoTop** topological accuracy assessment via persistence diagrams
5. **Classifying** with a CNN (LeNet architecture, improved from ProtConv) on the concatenated embedding images
6. **Detecting functional domains** using Wasserstein distances between persistence diagrams — scale-invariant, analogous to BLAST but topology-aware

<p align="center">
  <img src="s2-pepanalyst images/Fig1_2.png" alt="S2-PEPANALYST workflow" width="820"/>
  <br/>
  <em>Full S2-PEPANALYST pipeline: from raw sequence to functional SSP classification.</em>
</p>

---

## 🏗️ Architecture

```
Protein Sequence (≤ 200 aa, N-terminal signal peptide)
          │
          ├────────────────────────┐
          ▼                        ▼
   TAPE Embedding             ESM Embedding  --> optimal by RL agent
   (768-dim)                  (high-dim)
          │                        │
          ▼                        ▼
  Image 28×28               Image 32×32
          │                        │
          └──────────┬─────────────┘
                     ▼
          GeoTop Topological Assessment
          (Persistence Diagrams PD₀,₁,₂)
                     │
                     ▼
          Concatenated Embedding Image
                     │
                     ▼
          ┌──────────────────────┐
          │  LeNet-based CNN     │
          │  (ProtConv improved) │
          └──────────────────────┘
                     │
                     ▼
          SSP Family Classification
          (CEP, CRP, SCOOP, RALF, ...)
```

### Functional Domain Detection (Scale-Invariant)

For each protein sequence *i*, the pipeline computes persistence diagrams PD₀,₁,₂(*Xᵢ*) from its geometric representation. The **Wasserstein distance W₀** between persistence diagrams is used as a scale-invariant similarity measure:

- **W₀ = 0** between two sequences → identical functional topology → same functional domain
- Scale invariance means domain detection is robust to insertions, deletions, and length variation — unlike BLAST

---

## 🌱 Supported Species

| Species | Common name | Role in study |
|---|---|---|
| *Arabidopsis thaliana* | Thale cress | Primary model organism |
| *Solanum lycopersicum* | Tomato | Validation species |
| *Persea americana* cv. Hass | Avocado Hass | Validation species |
| *Persea americana* cv. Gwen | Avocado Gwen | Validation species |

---

## ⚙️ Methods

### SSP Identification Criteria
Building on Tasnim *et al.* (2021):
- Protein length **≤ 200 amino acids**
- Presence of an **N-terminal signal peptide** (Teufel *et al.*, 2022 — new class)
- Topological accuracy validation via **GeoTop** (Abaach *et al.*, 2023)

### Signalling Families (Arabidopsis)
CEP · CRPs · SCOOPs · RALFs · PEP1 · and newly identified families via data mining of NCBI

### Embeddings
- **TAPE** — Transformer-based protein embedding (768-dim geometric representation)
- **ESM** — Evolutionary Scale Modeling protein embedding (higher-dim)

Both are independently converted to 2D image form and then **concatenated** before CNN input, enriching the feature space beyond what either embedding alone provides.

### CNN
LeNet-based architecture from [ProtConv](https://github.com/swakkhar/ProtConv), significantly extended with reinforcement learning-based feature embedding selection that dynamically picks the most effective embedding for each prediction.

---

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/MorillaLab/s2-PEPANALYST.git
cd s2-PEPANALYST
pip install -r requirements.txt
```

### Predict SSPs from a FASTA file

```python
# Open and run the main prediction notebook
# code/ contains all analysis and prediction notebooks
```

Or launch in Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MorillaLab/s2-PEPANALYST/blob/main/code/)

### Run the full pipeline

```bash
# Step 1 — Prepare sequence data
jupyter nbconvert --to notebook --execute code/01_data_preparation.ipynb

# Step 2 — Generate TAPE & ESM embeddings
jupyter nbconvert --to notebook --execute code/02_embeddings.ipynb

# Step 3 — GeoTop topological assessment
jupyter nbconvert --to notebook --execute code/03_geotop.ipynb

# Step 4 — CNN classification
jupyter nbconvert --to notebook --execute code/04_classification.ipynb
```

---

## 📁 Repository Structure

```
s2-PEPANALYST/
├── code/                       # All analysis and prediction notebooks
├── data/                       # Sequence data and pre-processed embeddings
├── s2-pepanalyst images/       # Figures and workflow diagrams
│   └── FigS1.png               # Main pipeline figure
├── s2PEPANALYST.png            # Tool logo / overview figure
├── requirements.txt            # Python dependencies
├── LICENSE                     # GPL-3.0
└── README.md
```

---

## 📦 Dependencies

Key packages (see `requirements.txt` for full list):

| Package | Purpose |
|---|---|
| `tape-proteins` | TAPE protein language model embeddings |
| `fair-esm` | ESM protein embeddings (Meta AI) |
| `torch` / `torchvision` | CNN training and inference |
| `giotto-tda` / `gudhi` | Topological data analysis (persistence diagrams) |
| `scikit-learn` | Feature processing and evaluation |
| `biopython` | Sequence parsing (FASTA, GenBank) |
| `matplotlib` / `seaborn` | Visualisation |

---

## 🔗 Related Tools & References

- **GeoTop** (Abaach *et al.*, 2023) — topological accuracy assessment
- **ProtConv** (Swakkhar *et al.*) — base CNN architecture: https://github.com/swakkhar/ProtConv
- **TAPE** (Rao *et al.*, 2019) — protein language model
- **ESM** (Lin *et al.*, 2022) — evolutionary scale modelling
- **SignalP-6** (Teufel *et al.*, 2022) — signal peptide detection

---

## 🌐 Web Tool

A web interface for S2-PEPANALYST is described in the paper. For online access, contact the corresponding author.

---

## 🎈 Citation

If you use S2-PEPANALYST in your research, please cite:

```bibtex
@article{VomoDonfack2026s2pepanalyst,
  title   = {S2-PepAnalyst: A Web Tool for Predicting Plant Small Signalling Peptides},
  author  = {Vomo-Donfack, Kelly L. and Abaach, Mariem and Luna, Ana M. and
             Ginot, Grégory and Doblas, Verónica G. and Morilla, Ian},
  journal = {Plant Biotechnology Journal},
  year    = {2026},
  doi     = {10.1111/pbi.70536},
  url     = {https://onlinelibrary.wiley.com/doi/10.1111/pbi.70536},
  publisher = {Wiley}
}
```

---

## 🤝 Contributing

We welcome contributions — new species support, alternative embeddings, improved CNN architectures. Please open an issue first. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

---

## 📜 License

This project is licensed under the GNU General Public License v3.0 — see [`LICENSE`](LICENSE) for details.

> **Note:** The License badge URL in the original README contained a typo (`Gchoosealicense.com`) — fixed here. The Colab badge was also pointing to the wrong repo — corrected.

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/MorillaLab">MorillaLab</a>
  <br/>
  <sub>Published in <em>Plant Biotechnology Journal</em>, 2026 · Wiley</sub>
</div>

