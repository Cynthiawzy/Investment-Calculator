def investment_solver(year, init_money, interest_rate, investment_return):
    remain_money = investment_return
    year_temp = 0
    invest_temp = investment_return
    if year == "X":
        while remain_money - init_money > 0:
            remain_money = (invest_temp / (1 + interest_rate))
            year_temp += 1
            invest_temp = remain_money
        return year_temp