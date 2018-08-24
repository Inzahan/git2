def hanoi(num_tray, _from, _by, _to):
    if num_tray==1:
        print('{}번째 원반을 {}에서 {}로 이동'.format(num_tray, _from, _to))
        return
    hanoi(num_tray-1, _from, _to, _by)
    print('{}번째 원반을 {}에서 {}로 이동'.format(num_tray, _from, _to))
    hanoi(num_tray-1, _by, _from, _to)
while 1:
    num_tray=int(input('쟁반숫자를 입력하삼(종료:0):'))
    if num_tray==0:
        break
    hanoi(num_tray, 'A', 'B', 'C')
