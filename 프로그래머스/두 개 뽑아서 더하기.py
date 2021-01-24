def solution (numbers) :
    result = []
    array_position = 0

    for i in numbers :
        for j in range(len(numbers)) :
            if j != array_position :
                result.append(i+numbers[j])
        array_position += 1

    result = set(result)
    result = list(result)
    result.sort()
    return result