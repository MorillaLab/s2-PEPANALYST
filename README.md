# s<sup>2</sup>-PEPANALYST
<p align="left">
  <a href="https://choosealicense.com/licenses/gpl-3.0/">
    <img src="https://img.shields.io/badge/License-GPLv3-green" alt="">
  </a>
</p>

Small Signalling Peptide Analysis in Plant Systems

This repository encompasses everything required for predicting small peptides in tomato (i.e., _Solanum lycopersicum_), avogado hass, avogado gwen and arabidpsis employing it as a plant-system model. The foundation of the model is derived from Tasnim _et al_., 2021, with added criteria including a size restriction of less than or equal to 200 amino acids. Furthermore, it incorporates the identification of an N-terminal signal peptide as a novel class (Teufel _et al_., 2022). The accuracy assessment is performed using GeoTop (Abaach _et al_., 2023). Moreover, the implementation involves the utilisation of a bespoke reinforcement learning to dynamically control the selection of the most effective feature embedding for the prediction. 

In this study, we utilize TAPE (i) and ESM (ii) embeddings. Each embedding is transformed into images of dimensions 28x28 and 32x32, respectively, upon which we apply Geotop accuracy assessment. Subsequently, we concatenate (i) and (ii) to enrich the information obtained. The resulting data is then converted into images before being inputted into a convolutional neural network (CNN) from LeNet. We opt for a CNN due to its effectiveness in computer vision tasks, leveraging concepts such as noise tolerance, distortion handling through sub-sampling, local receptive fields, and shared weights.

The architecture of the CNN employed in ProtConv is utilized.

The other aspect of our approach involves employing reinforcement learning techniques. This allows for the selection of the best embedding at each iteration, thereby enabling the creation of a highly effective predictive model.

![workflow_s2pepanalyst](https://github.com/MorillaLab/s2-PEPANALYST/blob/main/sPEPANALYST.png)

The other part of this work consist of classifying the small peptides of differents famillies. The methodology used here consist of:

  1. A collection of n protein sequences from Arabidopsis, belonging to different gene peptide families (Data Mining).

  2. Construct the geometric representation, in 768 dimensions for TAPE and more for ESM, of each protein sequence i to obtain a finite set of points X_i.

  3. Compute the persistence diagrams of the sets X_i to obtain the sets of persistence diagrams of dimensions 0, 1, and 2, PD0(X<sub>i</sub>).

  4. Calculate the distance matrix of dimensions n x n, where the entry (i, j) is the Wasserstein distance W0 between the persistence diagrams of dimension 0, W0(PD0(X_i), PD0(X_j)).

  5. Construct the phylogenetic tree of the protein sequences from the distance matrix in Step 4, using the UPGMA algorithm.

