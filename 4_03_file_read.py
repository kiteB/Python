
with open('chicken.txt', 'r', encoding="UTF-8") as f:    # 읽어들인 파일을 f에 저장!
    print(type(f))      # for 문을 쓰면 리스트 같이 동작함.
    for line in f:
        print(line)