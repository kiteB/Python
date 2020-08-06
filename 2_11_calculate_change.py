def calculate_change(payment, cost):
    change = payment - cost

    fifty = change // 50000
    ten = (change % 50000) // 10000
    five = (change % 10000) // 5000
    one = (change % 5000) // 1000
    print("{}원 지폐: {}장".format(50000, fifty))
    print("{}원 지폐: {}장".format(10000, ten))
    print("{}원 지폐: {}장".format(5000, five))
    print("{}원 지폐: {}장".format(1000, one))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)