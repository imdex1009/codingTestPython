def solution(n, lost, reserve):

    nlost = set(lost) - set(reserve)
    nreserve = set(reserve) - set(lost)

    answer = n - len(nlost)

    for l in nlost:
        front = l - 1
        back = l + 1

        if front in nreserve:
            answer += 1
            nreserve.remove(front)

        elif back in nreserve:
            answer += 1
            nreserve.remove(back)

        else:
            continue

    return answer





output1 = solution(8, [2, 4, 7, 8], [1, 3, 5])
print('output1', output1)
output2 = solution(10, [8, 9], [9])
print('output2',output2)


