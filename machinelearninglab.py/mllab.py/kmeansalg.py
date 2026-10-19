from sklearn.cluster import KMeans
import numpy as np
X = np.array([[15, 39], [16, 81], [85, 6], [88, 77]])
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(X)
print(f"Unsupervised Cluster Assignments: {clusters}")
print("\n--- Cluster Assignments Breakdown ---")
for i, (features, cluster_id) in enumerate(zip(X, clusters)):
    print(f"Customer {i+1} {features} -> Assigned to Cluster: {cluster_id}")
print("\nCluster Centers:")
print(kmeans.cluster_centers_)