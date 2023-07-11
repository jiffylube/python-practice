# find factorial

def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i

    print(answer)


factorial(3)
