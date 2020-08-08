# 변수 정의
previous = 0
current = 1
i = 1

while i <= 50:
    print(current)

    temp = previous         # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp    # temp에는 기존 previous 값이 저장되어 있음.

    # previous, current = current, current + previous 이렇게 한 줄로 표현할 수 있음.

    i += 1









