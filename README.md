# s<sup>2</sup>-PEPANALYST
[![License](https://img.shields.io/badge/License-GPLv3-green)](https://Gchoosealicense.com/licenses/gpl-3.0/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/MorillaLab/TopoTransformers/)
[![Doi](https://img.shields.io/badge/Doi-10.1101-blue)](https://www.biorxiv.org/content/10.1101/2024.08.02.606319v1.abstract)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

Small Signalling Peptide Analysis in Plant Systems

This repository encompasses everything required for predicting small peptides in tomato (i.e., _Solanum lycopersicum_), avogado hass, avogado gwen and arabidpsis employing it as a plant-system model. The foundation of the model is derived from Tasnim _et al_., 2021, with added criteria including a size restriction of less than or equal to 200 amino acids. Furthermore, it incorporates the identification of an N-terminal signal peptide as a novel class (Teufel _et al_., 2022). The accuracy assessment is performed using GeoTop (Abaach _et al_., 2023). Moreover, the implementation involves the utilisation of a bespoke reinforcement learning to dynamically control the selection of the most effective feature embedding for the prediction. 

In this study, we utilize TAPE (i) and ESM (ii) embeddings. Each embedding is transformed into images of dimensions 28x28 and 32x32, respectively, upon which we apply Geotop accuracy assessment. Subsequently, we concatenate (i) and (ii) to enrich the information obtained. The resulting data is then converted into images before being inputted into a convolutional neural network (CNN) from LeNet. We opt for a CNN due to its effectiveness in computer vision tasks, leveraging concepts such as noise tolerance, distortion handling through sub-sampling, local receptive fields, and shared weights.

The architecture of the CNN employed in ProtConv is utilised (https://github.com/swakkhar/ProtConv).

The other aspect of our approach involves employing reinforcement learning techniques. This allows for the selection of the best embedding at each iteration, thereby enabling the creation of a highly effective predictive model.

![workflow_s2pepanalyst](https://github.com/MorillaLab/s2-PEPANALYST/blob/main/s2PEPANALYST.png)

# Family classification 
#### Classifying small peptides from different `signalling families` 
```ruby
1. **Comprehensive Literature Compilation**: A thorough collection of existing literature encompassing all known signalling peptide families from _Arabidopsis thaliana_ (e.g., CEP, CRPs, SCOOPs, RALFs, etc.), along with newly identified signalling peptides. These additions were integrated into these families through data mining in well-established databases, including NCBI.&#8203;:contentReference[oaicite:0]{index=0}

2. **Geometric Representation Construction**: :contentReference[oaicite:1]{index=1}&#8203;:contentReference[oaicite:2]{index=2}

3. **Persistence Diagrams Computation**: :contentReference[oaicite:3]{index=3}&#8203;:contentReference[oaicite:4]{index=4}

4. **Distance Matrix Calculation**: :contentReference[oaicite:5]{index=5}&#8203;:contentReference[oaicite:6]{index=6}

5. **Functional Domain Detection**: :contentReference[oaicite:7]{index=7}&#8203;:contentReference[oaicite:8]{index=8}

```



