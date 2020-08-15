def count_matching_numbers(list_1, list_2):
    # 맞은 개수 카운트하는 변수
    count = 0

    # list_1에 있는 변수가
    for n in list_1:
        # 만약 list_2에 있다면
        if n in list_2:
            # count++
            count += 1

    # count 리턴
    return count


# 테스트
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))