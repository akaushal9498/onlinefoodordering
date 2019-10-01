

def countsubarray(array,k):
    count = 0
    for i in range(0, len(array)):
        if array[i] <= k:
            count += 1
        mul = array[i]

        for j in range(i + 1, len(array)):


            mul = mul * array[j]


            if mul <= k:
                count += 1
            else:
                break
    return count



array = [1, 2, 3, 4]
k = 10

countsubarray(array,k)
