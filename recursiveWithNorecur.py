def recur(n : int) -> int :
    s = []

    while True :
        if n > 0 :
            s.append(n)
            n = n - 1
            continue
        if s :
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break

x = int(input('정숫값을 입력해주세요 : '))

recur(x)
