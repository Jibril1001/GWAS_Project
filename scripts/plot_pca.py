import pandas as pd
import matplotlib.pyplot as plt

# Load PCA results (no header; columns: FID, IID, PC1, PC2, ..., PC20)
pca_cols = ["FID", "IID"] + [f"PC{i}" for i in range(1, 21)]
pca = pd.read_csv("chr1_pca.eigenvec", sep=r"\s+", header=None, names=pca_cols)

# Load ancestry panel (columns: sample, pop, super_pop, gender)
panel = pd.read_csv("integrated_call_samples_v3.20130502.ALL.panel", sep="\t")

# Merge on sample ID (IID in pca == sample in panel)
merged = pca.merge(panel, left_on="IID", right_on="sample", how="left")

# Plot PC1 vs PC2, colored by super population (broad ancestry group)
fig, ax = plt.subplots(figsize=(9, 7))
groups = merged.groupby("super_pop")
colors = plt.cm.tab10.colors

for (name, group), color in zip(groups, colors):
    ax.scatter(group["PC1"], group["PC2"], label=name, alpha=0.6, s=15, color=color)

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_title("1000 Genomes Chr1 PCA - colored by super population")
ax.legend(title="Super Population")
plt.tight_layout()
plt.savefig("chr1_pca_plot.png", dpi=150)
print("Saved plot to chr1_pca_plot.png")

# Also print variance explained by top PCs
eigenval = pd.read_csv("chr1_pca.eigenval", header=None)
total = eigenval[0].sum()
print("\nVariance explained:")
for i in range(5):
    pct = 100 * eigenval[0][i] / total
    print(f"PC{i+1}: {pct:.2f}%")
