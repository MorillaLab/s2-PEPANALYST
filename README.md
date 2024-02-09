# s<sup>2</sup>-PEPANALYST
<p align="left">
  <a href="https://choosealicense.com/licenses/gpl-3.0/">
    <img src="https://img.shields.io/badge/License-GPLv3-green" alt="">
  </a>
</p>

Small Signalling Peptide Analysis in Plant Systems

This repository encompasses everything required for predicting small peptides in tomato (i.e., Solanum lycopersicum), employing it as a plant-system model. The foundation of the model is derived from Tasnim et al., 2021, with added criteria including a size restriction of less than or equal to 200 amino acids. Furthermore, it incorporates the identification of an N-terminal signal peptide as a novel embedded feature. 
The accuracy assessment is performed using GeoTop (Abaach et al., 2023). Moreover, the implementation involves the utilisation of a bespoke reinforcement learning to dynamically control the selection of the most effective feature embedding.

![workflow_s2pepanalyst](https://github.com/MorillaLab/s2-PEPANALYST/blob/main/sPEPANALYST.png)
