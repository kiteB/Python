def count_matching_numbers(numbers, winning_numbers):
    # 맞은 개수 카운트하는 변수
    count = 0

    # list_1에 있는 변수가
    for number in numbers:
        # 만약 list_2에 있다면
        if number in winning_numbers:
            # count++
            count += 1

    # count 리턴
    return count


def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0


# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))