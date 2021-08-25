n = int(input())
for i in range(n):
    test = input()
    point = 1
    grade = 0
    for i in range(len(test)):
        if test[i] == 'O':
            grade = grade + point
            point = point + 1
        else:
            point = 1
    print(grade)