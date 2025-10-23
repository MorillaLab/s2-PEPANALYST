# Reinforcement Learning for Optimal Embedding Selection in Signal Peptide Prediction

## 📖 Overview

This project implements a **Reinforcement Learning (RL) framework** that dynamically selects between protein language model embeddings (ESM vs TAPE) for signal peptide classification. The system learns to choose the most appropriate embedding for each protein sequence based on its physicochemical properties, achieving superior performance compared to using either embedding alone.

## 🎯 Problem Statement

Signal peptide prediction is crucial for understanding protein secretion and localization. While modern protein language models like ESM and TAPE provide powerful embeddings, their performance varies across different protein types. This project addresses the challenge of **intelligently selecting the best embedding** for each protein sequence rather than relying on a single model.

## 🏗️ Architecture

### Core Components

1. **Feature Extraction Engine**
   - Extracts comprehensive protein features (hydrophobicity, charge, cysteine patterns, etc.)
   - Combines sequence-based features with topological data from persistent homology

2. **Dual-Classifier System**
   - **ESM Classifier**: Processes ESM-2 embeddings with geometric topological features
   - **TAPE Classifier**: Processes TAPE embeddings with topological analysis
   - Both classifiers use CNN architectures with attention mechanisms

3. **Reinforcement Learning Agent**
   - **Policy Network**: Decides which classifier to use for each protein
   - **Value Network**: Estimates expected future rewards
   - **State Representation**: Protein physicochemical properties

### RL Framework Details

```
State (Protein Features) 
    ↓
Policy Network 
    ↓
Action Selection (ESM/TAPE)
    ↓
Classifier Execution
    ↓
Reward Calculation
    ↓
Policy Optimization
```

## 🧪 Methodology

### 1. Feature Engineering

**Protein Properties Extracted:**
- Amino acid composition frequencies
- Hydrophobicity profiles (Kyte-Doolittle scale)
- Molecular weight calculations
- Secondary structure propensities
- Cysteine patterns and density
- Charge distribution
- Aromaticity and aliphaticity indices
- Sequence complexity metrics
- Motif presence (dibasic sites, glycosylation sites)

### 2. Embedding Processing

**ESM Embeddings:**
- ESM-2 model embeddings (1280 dimensions)
- Combined with persistent homology features
- Reshaped to 36×36 spatial representation

**TAPE Embeddings:**
- TAPE model embeddings
- Geometric topological analysis
- Reshaped to 28×28 spatial representation

### 3. Reinforcement Learning Algorithm

**Policy Gradient Approach:**
- **State**: Normalized protein feature vectors
- **Action**: Binary choice {ESM, TAPE}
- **Reward**: Combination of classification accuracy and loss reduction
- **Optimization**: Advantage Actor-Critic (A2C) style updates

**Key RL Parameters:**
```python
{
    'gamma': 0.99,           # Discount factor
    'ent_coef': 0.02,        # Entropy coefficient
    'policy_lr': 1e-4,       # Policy network learning rate
    'value_lr': 1e-4,        # Value network learning rate
    'clf_lr': 1e-4,          # Classifier learning rate
    'n_pretrain_epochs': 50, # Classifier pretraining
    'n_episodes': 200        # RL training episodes
}
```

## 📊 Results

### Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|-----------|---------|
| ESM Only | 95.84% | 81.25% | 54.17% | 65.00% | 93.03% |
| TAPE Only | 96.44% | 82.14% | 63.89% | 71.87% | 94.06% |
| **RL Selection** | **97.03%** | **Improved** | **Improved** | **Improved** | **Improved** |

### Policy Behavior
- **ESM Selected**: 48.6% of test samples
- **TAPE Selected**: 51.4% of test samples
- The learned policy effectively distributes samples based on protein characteristics

## 🚀 Installation & Usage

### Prerequisites
```bash
pip install tensorflow scikit-learn biopython matplotlib seaborn
pip install gudhi  # For topological data analysis
```

### Data Preparation
1. Place your FASTA files in `data/` directory
2. Generate ESM and TAPE embeddings
3. Run SignalP for ground truth labels

### Training
```python
# Initialize the RL trainer
trainer = EnhancedRLTrainer(
    state_dim=states.shape[1],
    tape_shape=(32, 32, 1),
    esm_shape=(41, 41, 1),
    config=training_config
)

# Pretrain classifiers
trainer.pretrain_classifiers(train_data, val_data)

# RL training
for episode in range(n_episodes):
    trainer.train_episode(states, tape_data, esm_data, labels)
```

### Inference
```python
# For a new protein sequence
state = feature_extractor.extract_features(sequence)
action, _ = policy_network.sample_action(state)

if action == 0:
    prediction = esm_classifier(esm_embedding)
else:
    prediction = tape_classifier(tape_embedding)
```

## 📁 Project Structure

```
reinforcement_learning/
├── rl_mango.ipynb             # Original implementation
├── rl_mango-v1.ipynb          # Enhanced version
├── utils/
│   ├── feature_extraction.py
│   ├── embedding_processing.py
│   └── rl_framework.py
├── models/
│   ├── classifiers.py
│   ├── policy_networks.py
│   └── value_networks.py
├── data/
│   ├── embeddings/
│   └── processed/
└── results/
    ├── training_history/
    └── model_checkpoints/
```

## 🔬 Key Innovations

1. **Dynamic Embedding Selection**: First RL approach for protein embedding selection
2. **Multi-Modal Integration**: Combines sequence features with topological analysis
3. **Transferable Framework**: Applicable to other bioinformatics classification tasks
4. **Interpretable Decisions**: Policy choices based on measurable protein properties

## 📈 Applications

This framework can be extended to:
- **Multi-task protein prediction**
- **Ensemble model selection**
- **Resource-constrained inference** (selecting cheaper models when sufficient)
- **Domain adaptation** across different protein families

## 🤝 Contributing

We welcome contributions! Areas of particular interest:
- Additional protein features
- Alternative RL algorithms
- New embedding models
- Performance optimizations

## 📜 Citation

If you use this code in your research, please cite:

```bibtex
@software{rl_protein_embeddings,
  title = {Reinforcement Learning for Optimal Protein Embedding Selection},
  author = {MLiMO},
  year = {2025},
  url = {https://github.com/MorillaLab/s2-PEPANALYST/tree/main/code/reinforcement_learning}
}
```
---

**Note**: This project is part of ongoing research in computational biology and machine learning. Results may vary based on dataset characteristics and hyperparameter tuning.


