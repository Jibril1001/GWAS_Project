# GWAS Project — Population Genetics with 1000 Genomes

[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org)
[![PLINK](https://img.shields.io/badge/PLINK-1.9-informational)](https://www.cog-genomics.org/plink/1.9/)
[![bcftools](https://img.shields.io/badge/bcftools-1.19-informational)](http://www.htslib.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A self-training project exploring population genetics and GWAS (Genome-Wide Association
Study) fundamentals, using real data from the [1000 Genomes Project](https://www.internationalgenome.org/).

## 📖 Overview

This repo documents an end-to-end pipeline for:

1. **Population structure analysis (PCA)** — detecting ancestry clusters from chromosome 1
   genotype data for 2,504 individuals, with no ancestry labels given to the analysis.
2. **GWAS association analysis** *(in progress)* — association testing, Manhattan/QQ plots.
3. **Post-GWAS analysis** *(planned)* — LD Score Regression (LDSC) and variant annotation.

Full narrative walkthroughs with explanations (written for a beginner to genetics) are in
[`notebooks/`](notebooks/).

## 🗂️ Repository Structure

```
├── notebooks/
│   ├── 01_PCA_1000Genomes.ipynb     ← full PCA pipeline, explained + reproducible
│   └── 02_GWAS_Association.ipynb    ← association analysis (in progress)
├── results/
│   ├── pca/                          ← PCA plots and output files
│   └── maf/                          ← minor allele frequency distribution
├── docs/
│   ├── PCA_Writeup.docx              ← detailed write-up with glossary
│   └── PCA_Presentation.pptx         ← slide deck
├── requirements.txt
└── README.md
```

## ⚙️ Setup

```bash
git clone https://github.com/Jibril1001/GWAS_Project.git
cd GWAS_Project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Running the full pipeline from raw data also requires:
- [bcftools](http://www.htslib.org/download/) ≥ 1.19
- [PLINK](https://www.cog-genomics.org/plink/1.9/) 1.9
- Raw 1000 Genomes data (chr1 VCF, reference genome, ancestry panel, strict mask) —
  download links and commands are in `notebooks/01_PCA_1000Genomes.ipynb`.

> Raw genomic data files (VCF, BCF, `.bed`/`.bim`/`.fam`, reference FASTA) are not committed
> to this repo due to size (multiple GB). Only code, notebooks, and result plots are tracked.

## 📊 Key Results

**PCA (chromosome 1, 2,504 individuals, 17,840 pruned SNPs):**
- PC1 explains 51.9% of variance, PC2 explains 24.1% (~76% combined)
- Individuals cluster clearly by continental ancestry (AFR, AMR, EAS, EUR, SAS),
  recovered with no labels given to the analysis

**MAF distribution (chromosome 1, pre-filtering):**
- Rare (MAF<1%): 83.5% · Low-frequency (1–5%): 7.0% · Common (MAF>5%): 9.5%

See [`notebooks/01_PCA_1000Genomes.ipynb`](notebooks/01_PCA_1000Genomes.ipynb) for full
methodology, code, and interpretation.

## 🧰 Tools Used

| Tool | Purpose |
|---|---|
| [bcftools](http://www.htslib.org/) | VCF normalization and cleaning |
| [PLINK 1.9](https://www.cog-genomics.org/plink/1.9/) | Format conversion, QC, pruning, PCA |
| Python (pandas, matplotlib) | Data merging and visualization |
| WSL2 (Ubuntu 24.04) | Linux environment for bioinformatics tooling |

## 📚 Reference

Data source: [1000 Genomes Project Consortium. "A global reference for human genetic
variation." *Nature* 526.7571 (2015): 68.](https://www.nature.com/articles/nature15393)

Tutorial followed: [Cloufield/GWASTutorial](https://github.com/Cloufield/GWASTutorial)

## 📝 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.