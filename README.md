# S<sup>2</sup>-PEPANALYST
[![License](https://img.shields.io/badge/License-GPLv3-green)](https://Gchoosealicense.com/licenses/gpl-3.0/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/MorillaLab/TopoTransformers/)
[![Doi](https://img.shields.io/badge/Doi-10.1101-blue)](https://www.biorxiv.org/content/10.1101/2024.08.02.606319v1.abstract)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

Small Signalling Peptide Analysis in Plant Systems

[Vomo-Donfack et al.  **S<sup>2</sup>-PepAnalyst: A Web Tool for Predicting Plant Small Signalling Peptides**. 2024. *BioRxiv*.](
https://www.biorxiv.org/content/10.1101/2024.08.02.606319v1.abstract) 👁️


This repository encompasses everything required for predicting small peptides in tomato (i.e., _Solanum lycopersicum_), avogado hass, avogado gwen and arabidpsis employing it as a plant-system model. The foundation of the model is derived from Tasnim _et al_., 2021, with added criteria including a size restriction of less than or equal to 200 amino acids. Furthermore, it incorporates the identification of an N-terminal signal peptide as a novel class (Teufel _et al_., 2022). The accuracy assessment is performed using GeoTop (Abaach _et al_., 2023). Moreover, the implementation involves the utilisation of a bespoke reinforcement learning to dynamically control the selection of the most effective feature embedding for the prediction. 

In this study, we utilize TAPE (i) and ESM (ii) embeddings. Each embedding is transformed into images of dimensions 28x28 and 32x32, respectively, upon which we apply Geotop accuracy assessment. Subsequently, we concatenate (i) and (ii) to enrich the information obtained. The resulting data is then converted into images before being inputted into a convolutional neural network (CNN) from LeNet. We opt for a CNN due to its effectiveness in computer vision tasks, leveraging concepts such as noise tolerance, distortion handling through sub-sampling, local receptive fields, and shared weights.

The architecture of the CNN employed in ProtConv is utilised and largely improved (https://github.com/swakkhar/ProtConv).

# ![workflow_s2pepanalyst](https://github.com/MorillaLab/s2-PEPANALYST/blob/main/FigS4.png)

<!-- HTML for image resizing -->
<img src="https://github.com/MorillaLab/s2-PEPANALYST/blob/main/FigS4.png?raw=true" alt="workflow_s2pepanalyst" width="50%"/>


# Functional classification 
> ## Classification of Small Peptides from Different Signalling Families
>
> The methodology employed consists of:
>
> 1. **Comprehensive Literature Compilation**: A thorough collection of existing literature encompassing all known signalling peptide families from _Arabidopsis thaliana_ (e.g., CEP, CRPs, SCOOPs, RALFs), along with newly identified signalling peptides. These additions were integrated into these families through data mining in well-established databases, including NCBI.
>
> 2. **Geometric Representation Construction**: For each protein sequence _i_, construct its geometric representation in 768 dimensions for TAPE and higher dimensions for ESM, resulting in a finite set of points X<sub>i</sub>.
>
> 3. **Persistence Diagrams Computation**: Compute the persistence diagrams of the sets X<sub>i</sub> to obtain the persistence diagrams for dimensions 0, 1, and 2, denoted as PD<sub>0,1,2</sub>(X<sub>i</sub>). This process also facilitates the identification of behavioural peptides that lack a signal peptide region, such as PEP1, among others.
>
> 4. **Distance Matrix Calculation**: Calculate the distance matrix of dimensions _n_ x _n_, where the entry (_i_, _j_) represents the Wasserstein distance W<sub>0</sub> between the persistence diagrams of dimension 0: W<sub>0</sub>(PD<sub>0</sub>(X<sub>i</sub>), PD<sub>0</sub>(X<sub>j</sub>)).
>
> 5. **Functional Domain Detection**: If the distance calculated in Step 4 is zero for a given pair, this is analogous to using BLAST but invariant to changes in scale. Scale invariance aids in accurately detecting _functional_ domains regardless of their length, leading to improved _functional_ annotation of proteins.

