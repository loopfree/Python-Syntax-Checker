def fun(num):
    while num < 100:
        if num < 10:
            num = num + 1
            continue
        if num > 50:
            break
        num = num + 1
    for i in range(num):
        print(i)
    return num