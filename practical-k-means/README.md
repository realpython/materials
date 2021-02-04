# Practical K-Means Clustering in Python

The Jupyter notebooks in this directory follow the code examples in Real Python's [Practical K-Means Clustering in Python](https://realpython.com/k-means-clustering-python/) article. The article is structured such that there are two main sections with code. The first section works with synthetic data. The second section starts when the TCGA cancer gene expression dataset is introduced.

## Getting Started

Follow the instructions below to get up and running with a Jupyter notebook and all the code from the article.

### Install Dependencies

These notebooks have dependencies. One way to install these dependencies is to use the Anaconda Python distribution.

```bash
(base) $ conda install jupyter matplotlib numpy pandas seaborn scikit-learn
(base) $ conda install -c conda-forge kneed
```

You can also install all the requirements using `pip` and the `requirements.txt` file included in this directory.

```bash
$ python3 -m pip install -r requirements.txt
```

### Synthetic Data Notebook

Open the notebook that accompanies the sections of the article that work with synthetic data:

```bash
(base) $ jupyter notebook practical-kmeans-synthetic.ipynb
```

### Cancer Gene Expression Data Notebook

Open the notebook that accompanies the sections of the article that work with TCGA cancer gene expression data:

```bash
(base) $ jupyter notebook practical-kmeans-cancer-gene-expression.ipynb
```
