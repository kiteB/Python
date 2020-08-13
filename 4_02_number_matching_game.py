import random

# 상수 정의
ANSWER = random.randint(1, 20)  # 게임의 정답
LIFE = 4                        # 총 기회 수

# 변수 정의
guess = -1          # 사용자가 입력한 값
tries = 0           # 사용자 시도 횟수

while guess != ANSWER and tries < LIFE:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ".format(LIFE - tries)))
    tries += 1

    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")

if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞추셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))