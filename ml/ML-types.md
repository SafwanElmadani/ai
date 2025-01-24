

## There are two types of machine learning:
- Supervised learning: type of ML where the algorithm is trained on labeled data. For every input, there is a corresponding output.
- Unsupervised learning: type of ML where the algorithm is given unlabeled data. The goal is to discover hidden patterns or distributions.

### **Supervised learning** can be broadly categorized into two main types: 
 - regression
 - classification

1. Regression:
	 Regression models are used when the output variable is a real value, such as "salary" or "weight". These models are best for predicting continuous outcomes.
	 
	 - Linear Regression: Predicts a dependent variable value (y) based on a given independent variable (x) by fitting a linear equation to observed data.
	 - Polynomial Regression: Extends linear regression by considering polynomial features of the input.
	 - Ridge/Lasso Regression: Variations of linear regression that include regularization to prevent overfitting.

2. Classification:
	 Classification models are used when the output variable is a category, such as "spam" or "not spam". These models are best for categorizing inputs into two or more classes.
	
	 - Logistic Regression: Despite its name, it's used for binary classification problems (e.g., yes/no predictions).
	 - Decision Trees: Models that predict the value of a target variable by learning simple decision rules inferred from the data features.
	 - Random Forests: An ensemble of decision trees, typically used for classification problems. It improves model accuracy by averaging multiple trees.
	 - Support Vector Machines (SVM): A robust classification method that finds the best boundary between classes.
	 - K-Nearest Neighbors (KNN): A simple, instance-based learning where the class of a sample is determined by the majority class among its k nearest neighbors.
	 - Naive Bayes: A simple probabilistic classifier based on applying Bayes' theorem with strong (naïve) independence assumptions between the features.

### **Unsupervised Learning** 
In the unsupervised learning, we are trying to find some interesting patterns in unlabeled data.
The main types of unsupervised learning:
1. Clustering
	 Clustering involves grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups
	 - K-Means Clustering: Divides the data into K clusters, where each observation belongs to the cluster with the nearest mean.
	 - Hierarchical Clustering: Builds a multilevel hierarchy of clusters by creating a dendrogram, which can be useful for understanding the data's similarity structure.
	 - DBSCAN (Density-Based Spatial Clustering of Applications with Noise): Finds core samples of high density and expands clusters from them. Good for data with clusters of similar density.
2. Dimensionality Reduction
	 Dimensionality reduction is used to reduce the number of input variables in a dataset, simplifying the dataset while retaining its essential characteristics.
	 - **Principal Component Analysis (PCA):** Linear dimensionality reduction technique that seeks to maximize variance and uncover the principal components of the data.
	 - **t-Distributed Stochastic Neighbor Embedding (t-SNE):** Non-linear technique primarily used for exploring high-dimensional data and visualizing it in low-dimensional spaces (usually 2D or 3D).
	 - **Autoencoders:** Neural networks used for learning efficient codings of unlabeled data; the network aims to learn a compressed, distributed representation (encoding) for a set of data
3. Association
4. Anomaly Detection
5. Neural Networks and Deep Learning

