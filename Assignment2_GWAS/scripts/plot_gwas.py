import gwaslab as gl

# Load the plink2 --glm firth output directly (gwaslab knows this format)
mysumstats = gl.Sumstats("1kgeas.B1.glm.firth", fmt="plink2")

# Basic sanity check / standardization (fills in genome build, sorts, etc.)
mysumstats.basic_check()

# Manhattan + QQ plot together
mysumstats.plot_mqq(
    skip=3,                 # skip variants with -log10(P) < 3 for speed
    save="mqq_plot.png",
    save_kwargs={"dpi": 300}
)
