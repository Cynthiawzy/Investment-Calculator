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
    if init_money == "X":
        init_temp = investment_return
        for i in range(year):
            money_temp = (init_temp / (1 + interest_rate))
            init_temp = money_temp
        return init_temp
    if interest_rate == "X":
        money_temp = 0
        for i_r in range(100):
            init_temp = init_money
            del money_temp
            for i in range(year + 2):
                money_temp = (init_temp * (i_r / 10)) + init_temp
                init_temp = money_temp
                if money_temp == investment_return:
                    return i_r / 10
    if investment_return == "X":
        for i in range(year):
            invest_temp = (init_money * interest_rate) + init_money
            init_money = invest_temp
        return invest_temp
