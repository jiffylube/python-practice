def isAnagram(n):
    if len(n) <= 1:
        print('true')

    newString = n.lower()
    import re
    newString = re.sub('[^0-9a-zA-Z]+', '', newString)
    # print(newString)
    length = int(len(newString) / 2)
    print(length)

    for i in range(0, length+1):
        print(i, -i)
        print(newString[i], newString[-i - 1])
        if i == length:
            print('true')
        if newString[i] == newString[-i - 1]:
            continue
        elif newString[i] != newString[-i - 1]:
            print('false')


isAnagram("ab_a")
