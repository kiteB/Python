# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    return krw / 1000       # 1,000원 당 1달러

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    return usd / 8 * 1000   # 1,000 / 8 달러 당 1엔

# 원화(￦)으로 각각 얼마인가요?
amounts = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(amounts))

# amounts를 원화(￦)에서 달러($)로 변환하기
# 코드를 입력하세요.
i = 0
while i < len(amounts):
    amounts[i] = krw_to_usd(amounts[i])
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
# 코드를 입력하세요.
i = 0
while i < len(amounts):
    amounts[i] = usd_to_jpy(amounts[i])
    i += 1

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))