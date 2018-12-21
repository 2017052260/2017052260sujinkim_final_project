#2017052260 김수진_기말과제 지뢰찾기

import random #random 모듈 포함시키기

print(" *지뢰찾기 게임* \n상단의 지뢰를 보고 빈 셀에 들어갈 번호를 맞추세요.")
print("지뢰는 무작위로 배치되며 *로 표시됩니다.")

print("가로x세로 격자 크기를 각각 입력하세요.")

m = int(input("M:")) # 가로 격자 크기 입력
n = int(input("N:")) # 새로 격자 크기 입력

if (n <= 0 and m >= 100): # 격자가 0보다 작거나 100보다 큰 경우
    print("1~99 사이의 값을 입력해 주세요") # 오류메세지 출력

def socationMines(m,n): # 지뢰와 빈 셀을 랜덤생성
    mn = [[random.choice(['.', '.', '*']) for x in range(n)] for y in range(m)]
    for y in mn: # mn에서 고른 지뢰(*)와 빈 셀(.)을 join하여 나열한다.
        print(''.join(y))
    r = mn.copy() # 지뢰와 빈 셀을 r에 저장
    return r

def getCounts(r): # 빈 셀에 대한 카운트 숫자
    for y, yd in enumerate(r): # r의 항목을 순서대로 y와 yd에 저장
        for x, xd in enumerate(yd): #yd의 항목을 순서대로 x와 xd에 저장
            if r[y][x] == '*': continue # y행 x열 값이 지뢰이면 for문을 나간다
            count = 0
            c = [[''] if y - 1 < 0 else r[y - 1][0 if x - 1 < 0 else x - 1:x + 2], # y행 x열의 전,후 위아래 대각선 지뢰 카운트(결과값을 c에 저장)
                 r[y][0 if x - 1 < 0 else x - 1:x + 2],
                 [''] if y + 1 >= m else r[y + 1][0 if x - 1 < 0 else x - 1:x + 2]]
            for z in c: # c의 결과를 z에 저장
                count += z.count('*') # z에 저장된 지뢰(*)의 갯수를 count함
            r[y][x] = str(count) # count된 지뢰의 갯수를 y행 x열(현위치)에 저장(이 셀은 반드시 지뢰가 아닌 빈 셀임)
    return r

r = socationMines(m, n) # 격자 값을 사용자로부터 입력받아 지뢰 생성
y = getCounts(r) # 지뢰갯수 세기

print("\n \n")
print("정답")
for y in r:
    print(''.join(y))


