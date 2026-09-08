# Assignment 1: PCA Using the 1000 Genomes Project Dataset

## Overview

This assignment investigates population structure in the 1000 Genomes Project dataset using Principal Component Analysis (PCA).

The goal was to perform quality control, reduce linkage disequilibrium (LD), calculate principal components, and visualize genetic population structure.

Because running the complete genome was computationally demanding, chromosome 1 was used, which is permitted by the assignment instructions.

## Dataset

The analysis used the 1000 Genomes Project Phase 3 dataset.

* Individuals: 2,504
* Chromosome analyzed: chr1
* Reference build: hg19
* Population information: 1000 Genomes super-population labels

The five super-populations were:

* AFR: African
* AMR: Admixed American
* EAS: East Asian
* EUR: European
* SAS: South Asian

## Analysis Workflow

The analysis followed these main steps:

1. Normalize the VCF data and remove duplicate variants.
2. Apply the 1000 Genomes strict accessibility mask.
3. Perform variant quality control.
4. Keep SNPs and variants with MAF >= 0.10.
5. Perform LD pruning using `--indep-pairwise 50 5 0.2`.
6. Calculate principal components using PLINK.
7. Merge PCA results with 1000 Genomes population labels.
8. Plot PC1 against PC2.

## MAF Distribution

Before the final MAF >= 0.10 filtering used for PCA, the chromosome 1 dataset contained a large number of rare variants.

Approximate distribution:

| MAF category         | Number of variants | Proportion |
| -------------------- | -----------------: | ---------: |
| Rare (<1%)           |          4,049,626 |     83.47% |
| Low-frequency (1-5%) |            342,107 |      7.05% |
| Common (>5%)         |            459,651 |      9.47% |

These rare and low-frequency variants were not all included in the final PCA. The PCA analysis applied the MAF >= 0.10 threshold before LD pruning.

## PCA Results

After quality control and LD pruning, 17,840 variants were used for the final PCA.

The analysis calculated 20 principal components.

The first five PCs explained approximately:

| Principal Component | Variance explained |
| ------------------- | -----------------: |
| PC1                 |             22.31% |
| PC2                 |             10.35% |
| PC3                 |              3.06% |
| PC4                 |              2.25% |
| PC5                 |              0.50% |

PC1 and PC2 together explained approximately 32.66% of the variation captured by the analyzed chromosome 1 variants.

## Population Structure

The PC1 vs PC2 plot shows clear population structure.

* AFR individuals show strong separation along PC1 and a broad distribution.
* EAS individuals form a relatively compact cluster.
* EUR individuals form a distinct cluster.
* SAS individuals occupy an intermediate region.
* AMR individuals show a broader distribution, consistent with their admixed ancestry.

The PCA itself was calculated without using ancestry labels. The known 1000 Genomes population labels were added afterward to color and interpret the PCA plot.

## Limitations

This analysis used chromosome 1 rather than the complete genome because of computational limitations.

Therefore, the exact proportion of variance explained by the PCs should not be interpreted as representative of a whole-genome PCA. A whole-genome analysis could produce different variance proportions and potentially finer population structure.

In addition, PCA summarizes genetic variation and population structure. It does not by itself identify disease-associated variants or establish causal relationships.

## Files

* `figures/chr1_pca_plot.png`: PC1 vs PC2 colored by super-population.
* `figures/chr1_maf_distribution.png`: MAF distribution.
* `scripts/plot_pca.py`: Python script used to generate the PCA plot and calculate variance explained.

## Software

* PLINK / PLINK 2
* bcftools
* Python
* pandas
* matplotlib

## Conclusion

PCA successfully captured the major population structure present in the 1000 Genomes chromosome 1 dataset. The clear separation of the major super-populations demonstrates how principal components can be used to summarize genetic ancestry and detect population structure.

This analysis also demonstrates why PCA is an important step in GWAS: population structure can be incorporated into downstream association models to help control for confounding.
