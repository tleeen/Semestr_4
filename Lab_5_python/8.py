def mirror(arr):
    mirrored_part = list(reversed(arr))
    for i in range(len(arr)):
        arr.append(mirrored_part[i])


arr = [1, 2]
mirror(arr)
print(*arr)