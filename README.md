# s<sup>2</sup>-PEPANALYST
<p align="left">
  <a href="https://choosealicense.com/licenses/gpl-3.0/">
    <img src="https://img.shields.io/badge/License-GPLv3-green" alt="">
  </a>
</p>

Small Signalling Peptide Analysis in Plant Systems

This repository encompasses everything required for predicting small peptides in tomato (i.e., _Solanum lycopersicum_), avogado hass, avogado gwen and arabidpsis employing it as a plant-system model. The foundation of the model is derived from Tasnim _et al_., 2021, with added criteria including a size restriction of less than or equal to 200 amino acids. Furthermore, it incorporates the identification of an N-terminal signal peptide as a novel class (Teufel _et al_., 2022). The accuracy assessment is performed using GeoTop (Abaach _et al_., 2023). Moreover, the implementation involves the utilisation of a bespoke reinforcement learning to dynamically control the selection of the most effective feature embedding for the prediction. 

In this study, we utilize TAPE (i) and ESM (ii) embeddings. Each embedding is transformed into images of dimensions 28x28 and 32x32, respectively, upon which we apply Geotop accuracy assessment. Subsequently, we concatenate (i) and (ii) to enrich the information obtained. The resulting data is then converted into images before being inputted into a convolutional neural network (CNN) from LeNet. We opt for a CNN due to its effectiveness in computer vision tasks, leveraging concepts such as noise tolerance, distortion handling through sub-sampling, local receptive fields, and shared weights.

The architecture of the CNN employed in ProtConv is utilised (https://github.com/swakkhar/ProtConv).

The other aspect of our approach involves employing reinforcement learning techniques. This allows for the selection of the best embedding at each iteration, thereby enabling the creation of a highly effective predictive model.

![workflow_s2pepanalyst](https://github.com/MorillaLab/s2-PEPANALYST/blob/main/s2PEPANALYST.png)

The other part of this work focuses on classifying small peptides from different signalling families. The methodology employed consists of:

  1. A comprehensive literature compilation covering all known signalling peptide families from _Arabidopsis thaliana_ (i.e., CEP, CRPs, SCOOPs, RALFs, etc.), along with newly identified signalling peptides, which were incorporated into these families through data mining in well-established databases, including NCBI.

  2. Construct the geometric representation, in 768 dimensions for TAPE and more for ESM, of each protein sequence i to obtain a finite set of points X<sub>i</sub>.

  3. Compute the persistence diagrams of the sets X<sub>i</sub> to obtain the persistence diagrams for dimensions 0, 1, and 2, denoted as PD<sub>0,1,2</sub>(X<sub>i</sub>). This feature also facilitates the identification of behavioural peptides that lack a signal peptide region, such as PEP1, and potentially others.

  4. Calculate the distance matrix of dimensions n x n, where the entry (i, j) is the Wasserstein distance W<sub>0</sub> between the persistence diagrams of dimension 0, W<sub>0</sub>(PD<sub>0</sub>(X<sub>i</sub>), PD<sub>0</sub>(X<sub>j</sub>)). 

  5. Thus, if such a distance in Step 4 is null for a given pair, this is akin to using BLAST but invariant to changes of scale. Scale invariance helps in detecting functional domains accurately, regardless of their length, leading to better functional annotation of proteins.

