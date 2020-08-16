# 스트라이크 수와 볼 수를 알려줌.
def get_score(guess, solution):     # guess = 유저가 뽑은 번호 3개가 담은 리스트
                                    # solution = 컴퓨터가 뽑은 정답 번호 3개가 담긴 리스트
    strike_count = 0    # 스트라이크 수
    ball_count = 0      # 볼 수

    # 숫자의 값과 위치가 모두 일치하면 스트라이크, 값만 맞으면 볼
    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 테스트
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)
