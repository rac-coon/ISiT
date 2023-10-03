# на 03.10.23 Реализован k-means
import random
import math
# pip install matplotlib
import matplotlib.pyplot as plt


def centroids_init() -> list:
    # инициализирование центроидов
    centroids: list = []
    for _ in range(k):
        centroid: list = []
        for _ in range(dim):
            value: float = random.randint(0, 100) / 100
            centroid.append(value)
        centroids.append(centroid)
    # частный пример значений (реальные центроиды) (dim: 2, k: 3)
    # centroids = [[0.12, 0.06], [0.72, 0.293], [0.192, 0.832]]
    return centroids


def calculate_length(vector_a: list, vector_b: list) -> float:
    length = 0
    vector_dim: int = len(vector_a)

    for i in range(vector_dim):
        length += math.pow(vector_a[i] - vector_b[i], 2)

    length = math.sqrt(length)
    return length


def kmeans_iteration(centroids) -> list:
    # расчет длины от значения до центроида
    for i, point in enumerate(data):
        value: float = float('inf')
        cluster: int = -1
        for j, centroid in enumerate(centroids):
            length: float = calculate_length(point, centroid)
            if value > length:
                value = length
                cluster = j
        clusters[i] = cluster

    # пересчет центроидов
    vals: list = [[] for _ in range(k)]
    for i, cluster in enumerate(clusters):
        vals[cluster].append(data[i])
    new_centroids: list = []
    for val in vals:
        val_count = len(val)
        new_centroid = [0 for _ in range(dim)]
        for item in val:
            for pos, element in enumerate(item):
                new_centroid[pos] += element
        for i in range(len(new_centroid)):
            try:
                new_centroid[i] = round(new_centroid[i] / val_count, 3)
            except ZeroDivisionError:
                new_centroid[i] = 0
        new_centroids.append(new_centroid)
    return new_centroids


def draw(vectors: list, clusters: list):
    plt.figure(figsize=(8, 4), dpi=80, facecolor='w', edgecolor='k')
    X = []
    Y = []
    for vector in vectors:
        X.append(vector[0])
        Y.append(vector[1])
    plt.title('k-means')
    plt.scatter(X, Y, c=clusters, cmap='viridis')
    plt.show()


k: int = 3
data: list = [
    [0, 0],
    [0.16, 0],
    [0.24, 0.08],
    [0.08, 0.16],

    [0.64, 0.24],
    [0.8, 0.24],
    [0.72, 0.4],

    [0.24, 0.72],
    [0.24, 0.8],
    [0.08, 0.8],
    [0.32, 0.88],
    [0.08, 0.96],
]
clusters = [-1 for i in range(len(data))]
dim: int = len(data[0])
N: int = 5


centrs = centroids_init()
print(centrs)
print(clusters)
for i in range(N):
    centrs = kmeans_iteration(centroids=centrs)
    print(centrs)
    print(clusters)
    draw(vectors=data, clusters=clusters)
