
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import ast

from sklearn.manifold import TSNE

nodes = pd.read_csv("export.csv")
nodes['louvain'] = pd.Categorical(nodes.louvain)
nodes.louvain.value_counts()

nodes[nodes.louvain==2168]

embedding = nodes.embedding.apply(lambda x: ast.literal_eval(x))
embedding = embedding.tolist()
embedding = pd.DataFrame(embedding)

tsne = TSNE()
X = tsne.fit_transform(embedding)

plt.scatter(
    X[:,0],
    X[:,1],
    c=nodes.louvain,
    cmap=cm.tab20
)
plt.show()
