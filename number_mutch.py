src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

result = []

for index in range(1, len(src)):
    if src[index] > src[index - 1]:
        result.append(src[index])

print(result)


