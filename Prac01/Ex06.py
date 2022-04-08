def functA(input, input2) :
    n, m, k = map(int, input.split(" "))

    data = list(map(int, input2.split(" ")))

    data.sort()
    first = data[n-1]
    second = data[n-2]


    result = 0

    while True:
        for i in range(k):
            if m == 0:
                break
            result += first
            m -= 1
        if m == 0:
            break
        result += second
        m-=1

    print(result)


a = "5 8 3"
b = "2 4 5 4 6"
functA(a, b)

