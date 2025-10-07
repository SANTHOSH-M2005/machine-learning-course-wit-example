from sklearn.cluster import KMeans

X = [
    [150, 8],
    [160, 7],
    [200, 3],
    [210, 4],
    [400, 8]
]

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

clusters = kmeans.predict(X)
print("Cluster assignments:", clusters)
