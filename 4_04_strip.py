# strip
print("     abc   def       ".strip())

# 03 예제 수정 - 공백 사라짐!
with open('chicken.txt', 'r', encoding="UTF-8") as f:    # 읽어들인 파일을 f에 저장!
    for line in f:
        print(line.strip())