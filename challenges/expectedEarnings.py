investment, expected_interest = input("Input your investment and expected interest").split()

investment = float(investment)
expected_interest = float(expected_interest)

for i in range(1, 11):
    investment = investment + (investment * expected_interest)
    print("Year {} , earnings {:.2f}€".format(i, investment))



