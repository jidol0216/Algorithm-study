import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")

g = sns.FacetGrid(tips,col="time",hue="sex")
g = sns.FacetGrid(tips, col="sex")
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_titles(row_template="{row_name}", col_template="{col_name}")
g.set(xlim=(0,60), ylim=(0,12))
g.add_legend()
g.savefig("rokey\python\ch21\seaborn\facet_plot.png")

# g.map_dataframe(sns.histplot,x ="total_bill",y = "tip")
# g.add_legend()
plt.tight_layout()
plt.show()