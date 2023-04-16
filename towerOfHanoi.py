def move(num : int, x : int, y : int) -> None :
    if num > 1 :
        move(num - 1, x, 6 - x - y)

    print(f'원반 [{num}을 {x}기둥에서 {y}기둥으로 옮깁니다]')

    if num > 1 :
        move(num - 1, 6 - x - y, y)

print('하노이의 탑을 구현합니다')
n = int(input('원반의 갯수를 입력해주세요 : '))

move(n, 1, 3)
