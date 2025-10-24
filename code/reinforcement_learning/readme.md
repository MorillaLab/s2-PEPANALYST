# Reinforcement Learning Framework for Dynamic Classifier Selection

This repository contains the implementation of a mixed machine learning model that combines **Convolutional Neural Networks (CNNs)** and **Reinforcement Learning (RL)** to dynamically classify small signalling peptides from plants such as *Arabidopsis thaliana*, tomato, mango, avocado hass, and gwen.

## 📖 Overview

The system leverages protein sequence embeddings from two pre-trained models — **ESM** and **TAPE** — and uses a reinforcement learning-based policy network to dynamically select the best-performing classifier for each input sample. This adaptive approach improves overall accuracy, generalisation, and computational efficiency compared to static ensemble methods.

## 🎯 Problem Statement

Small signalling peptides (SSPs) are a class of short, functional peptides that act as crucial mediators of intercellular communication in plants. While modern protein language models like ESM and TAPE provide powerful embeddings, their performance varies across different protein types. This project addresses the challenge of **intelligently selecting the best embedding** for each protein sequence rather than relying on a single model.

## Key Features

- **Dynamic Classifier Selection**: Uses an actor-critic RL framework to choose between ESM and TAPE classifiers per sample.
- **Confidence Penalty**: Incorporated into CNN training to reduce overfitting.
- **Sample-Specific Optimization**: The policy network learns to route inputs to the most suitable classifier.
- **Stable Training**: Value network reduces variance in policy updates via advantage estimation.

##  🏗️ Architecture

### 1. Classifier Networks
Two independent CNNs are trained on ESM and TAPE embeddings:

```
Input (ESM/TAPE matrix)
│
├── Conv2D (8, 3×3) + ReLU
├── AvgPool
├── Conv2D (16, 3×3) + ReLU
├── AvgPool
├── Conv2D (32, 3×3) + ReLU
├── AvgPool
├── Flatten
├── Dense (128) + ReLU
├── Dense (64) + ReLU
└── Dense (1) + Sigmoid
```

### 2. Reinforcement Learning Component
- **Policy Network (Actor)**: Decides which classifier to use.
- **Value Network (Critic)**: Estimates expected reward to stabilize learning.
- **Reward Function**: Balances accuracy and confidence, penalizing poor selections.

## 🧪 Methodology

1. **Input**: Protein sequences are embedded using ESM and TAPE.
2. **State Representation**: Embeddings are fed into the policy network.
3. **Action Selection**: Policy chooses ESM or TAPE classifier.
4. **Reward Calculation**: Based on prediction correctness and confidence.
5. **Policy Update**: Using advantage-based policy gradient.

## Experimental Setup

- **Datasets**: Plant peptide sequences from Arabidopsis, tomato, avocado.
- **Training**:
  - CNNs: 50 epochs, Adam optimizer, LR = 1e-4
  - RL: 200 episodes, γ = 0.99, entropy coefficient = 0.02
- **Evaluation Metrics**:
  - Accuracy
  - AUC
  - F1-Score 
  - MCC

## 📊 Results

The model demonstrates:
- Improved accuracy and AUC over individual classifiers
- Effective policy learning for classifier selection
- Better generalisation and reduced overfitting

## 📁 Project Structure

```
reinforcement_learning/
├── rl_mango.ipynb             # Enhanced version
├── rl_mango-v1.ipynb          # Original implementation
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
  
## License

This project is for academic use. Please cite the authors if you use this code in your research.

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


