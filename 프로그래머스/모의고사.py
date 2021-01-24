def solution (answer) :
    one = 0
    two = 0
    three = 0

    first = [1, 2, 3, 4, 5] * 2000
    second = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    for i in zip(answer, first, second, third) :
        if i[0] == i[1] :
            one += 1
        if i[0] == i[2] :
            two += 1
        if i[0] == i[3] :
            three += 1

    count = [one, two, three]
    result = []

    for i, j in enumerate(count, 1) :
        if j == max(count) :
            result.append(i)

    return result
    
answer = [1,3,2,4,2]
print(solution(answer))