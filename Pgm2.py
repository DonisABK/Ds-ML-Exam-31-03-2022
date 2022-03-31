from math import sqrt
def ed(r1, r2):
    d = 0.0
    for i in range(len(r1) - 1):
        d += (r1[i] - r2[i]) ** 2
    return sqrt(d)
dataset_train = [[2.78, 2.55, 0],
                [1.46, 2.36, 0],
                [3.39, 4.40, 0],
                [7.62, 2.75, 1],
                [5.33, 2.08, 1],
                [6.92, 1.77, 1]]
r0 = dataset_train[0]
for r in dataset_train:
    d = ed(r0, r)
    print('Euclidean distance:',d)
def getn(train, test_r, num_n):
    dx = list()
    for train_r in train:
        dist = ed(test_r, train_r)
        dx.append((train_r, dist))
    dx.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_n):
        neighbors.append(dx[i][0])
    return neighbors
neighbors = getn(dataset_train, dataset_train[0], 3)
for neighbor in neighbors:
    print("neighbor:")
    print(neighbor)
def predict(train, test_r, num_n):
    neighbors = getn(train, test_r, num_n)
    output_values = [r[-1] for r in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction
prediction = predict(dataset_train, dataset_train[0], 3)
print('Expected %d,' % (dataset_train[0][-1]))
print('Prediction %d,' %(prediction))
