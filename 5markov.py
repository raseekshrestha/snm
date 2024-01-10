transMat = [[0.9, 0.1], [0.5, 0.5]]
vect = [[1, 0]]
result = [[0, 0]]

# Matrix multiplication
for i in range(len(vect)):
    for j in range(len(transMat[0])):
        for k in range(len(transMat)):
            result[i][j] += vect[i][k] * transMat[k][j]

# Display the result
print("\nWeather of next day using Markov chain\n")
for i in range(len(result)):
    for j in range(len(result[0])):
        print(f"{result[i][j]:.6f}\t", end="")
    print()
