# Reinforcement Learning for Protein Signal Peptide Classification

## 📖 Project Overview

This project implements a **reinforcement learning (RL) framework** to intelligently select between two different deep learning classifiers for predicting signal peptides in protein sequences. The system combines sequence embeddings from both **TAPE (Task Assessing Protein Embeddings)** and **ESM (Evolutionary Scale Modeling)** with topological-morphological features extracted using **persistent homology** and **Lipschitz-Killing Curvatures** (GeoTop), creating a robust ensemble classification system.

## 🧬 Biological Context: Signalling Peptides

Signalling peptides are short functional peptide sequences that act as crucial mediators of intercellular communication in plants. Accurate identification of these peptides is crucial for understanding protein function and localisation. Traditional machine learning approaches typically rely on single-model predictions, but this project explores whether we can improve performance by dynamically selecting the most appropriate classifier for each protein sequence.

## 🏗️ System Architecture

### 1. **Feature Extraction Pipeline**

#### Sequence-Based Features:
- **Amino acid composition** (20 standard amino acids)
- **Physicochemical properties**:
  - Hydrophobicity (Kyte-Doolittle scale)
  - Cysteine count and patterns
  - GC content
  - Net charge
  - Aromaticity
  - Presence of dibasic protease sites

#### Embedding Representations:
- **TAPE embeddings**: 768-dimensional protein sequence representations
- **ESM-2 embeddings**: 1280-dimensional evolutionary-scale model representations

#### Topological Data Analysis:
- **Persistent homology** applied to embedding matrices reshaped as 2D images
- Captures topological features and shape characteristics of the protein representations
- Combined with original embeddings to create enriched feature representations

### 2. **Classifier Models**

Two independent CNN classifiers were trained:

- **ESM-based Classifier**: Processes ESM embeddings combined with topological features
- **TAPE-based Classifier**: Processes TAPE embeddings combined with topological features

Both classifiers were pre-trained for 50 epochs and achieved high accuracy (>97%) on the validation set.

### 3. **Reinforcement Learning Agent**

The core innovation is a **policy network** that learns to dynamically select between the two classifiers based on protein sequence features:

```python
class PolicyNetwork(tf.keras.Model):
    def __init__(self, state_dim, hidden=(128, 64), dropout_rate=0.1):
        super().__init__()
        self.norm = layers.LayerNormalization()
        self.h1 = layers.Dense(hidden[0], activation=tf.nn.gelu)
        self.do1 = layers.Dropout(dropout_rate)
        self.h2 = layers.Dense(hidden[1], activation=tf.nn.gelu)
        self.do2 = layers.Dropout(dropout_rate)
        self.logit = layers.Dense(1, activation=None)
```

## 🎯 Reinforcement Learning Formulation

### State Representation:
- 27-dimensional feature vector containing physicochemical properties and sequence characteristics

### Action Space:
- **Action 0**: Use ESM classifier
- **Action 1**: Use TAPE classifier

### Reward Function:
The agent receives rewards based on:
- **Accuracy bonus**: +1 for correct classification
- **Negative cross-entropy loss**: Encourages confident correct predictions
- **Relative performance penalty**: Penalizes choosing a classifier that performs worse than the alternative

### Training Strategy:
- **Policy Gradient** method with advantage estimation
- **Value network** for baseline subtraction to reduce variance
- **Entropy regularization** to encourage exploration
- **70 training episodes** with experience replay

## 📊 Results and Performance

The system was evaluated on a test set of 1,010 protein sequences:

| Model | Accuracy | AUC | Loss |
|-------|----------|-----|------|
| ESM Classifier Only | 0.9703 | - | 0.1741 |
| TAPE Classifier Only | 0.9723 | - | 0.1547 |
| **RL Combined System** | **0.9743** | **0.9856** | **0.1423** |

### Key Findings:
1. **Improved Performance**: The RL-based ensemble outperforms both individual classifiers
2. **Intelligent Selection**: The policy network learns to leverage the strengths of each classifier
3. **Robustness**: Combined system shows better generalization and reduced loss

## 🛠️ Technical Implementation

### Dependencies:
```python
TensorFlow 2.x, scikit-learn, BioPython, NumPy, Pandas
giotto-tda (for topological data analysis)
```

### Key Components:
1. **Data Preprocessing**: Feature extraction and normalization
2. **Topological Analysis**: Persistent homology computation
3. **Classifier Training**: CNN architecture with embedding inputs
4. **RL Training**: Policy and value network optimization
5. **Evaluation**: Comprehensive performance metrics and confusion matrices

## 💡 Scientific Contributions

1. **Novel Feature Integration**: Combines sequence embeddings with topological data analysis
2. **Dynamic Classifier Selection**: RL-based approach adapts to sequence characteristics
3. **Interpretable Decisions**: Policy choices can be analyzed to understand which features drive classifier selection
4. **Generalizable Framework**: Can be extended to other bioinformatics classification tasks

## 🚀 Future Directions

- Incorporate additional protein language models
- Extend to multi-class protein localization problems
- Develop attention mechanisms for interpretable decision-making
- Apply to other bioinformatics tasks requiring ensemble methods

## 📚 Citation

If you use this work in your research, please cite:

```bibtex
@software{rl_protein_classification,
  title = {Reinforcement Learning for Protein Signal Peptide Classification},
  author = {MLiMO},
  year = {2025},
  url = {https://github.com/MorillaLab/s2-PEPANALYST/tree/main/code/reinforcement_learning}
}
```

