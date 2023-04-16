def gcd(x: int, y: int) -> int :
    if y == 0 :
        return x
    else :
        return gcd(y, x % y)

if __name__ == '__main__' :
    print('두 자연수의 GCD를 구합니다')
    x = int(input('첫 번째 수를 입력해주세요'))
    y = int(input('두 번째 수를 입력해주세요'))

    print(f'두 수의 GCD는 {gcd(x, y)}입니다.')
