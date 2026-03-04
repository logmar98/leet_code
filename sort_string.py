def sort_string(s):
    s.sort(key=len)
    size = 0
    count = 0
    arr = []
    for i in s:
        if size < len(i):
            arr.append([])
            count += 1
            size = len(i)
        arr[count-1].append(i)
    result = []
    for x in arr:
        x.sort()
        result += x

    return result

s = ["bac", "aav", "b", "ad", "a", "cbbdf", "ba"]
print(sort_string(s))
