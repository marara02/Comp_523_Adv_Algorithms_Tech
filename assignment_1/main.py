def pylonsConstruction(a, b, k):
    pylons = [a]
    d_0 = a
    d_next = a + k
    while d_next < b:
        if d_next - d_0 <= k:
            d_next += k
        d_0 = d_next - k
        pylons.append(d_0)
    pylons.append(b)
    return pylons


a = 0
b = 669
k = 123
print(pylonsConstruction(a, b, k))


# [0, 123, 246, 369, 492, 615, 669]

def maxProfit(l_m_earnings, c):
    n = len(l_m_earnings)
    # initialize opt_city 2d array, i - monthly earning  in city j
    opt_city = [[0, 0] for _ in range(n + 1)]
    opt_city[0][0] = 0
    opt_city[0][1] = 0
    # initialize cities 2d array to add selected city for business in i month
    cities = [[-1, -1] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(2):
            stayProfit = opt_city[i - 1][j] + l_m_earnings[i - 1][j]
            moveProfit = opt_city[i - 1][1 - j] + l_m_earnings[i - 1][j] - c
            if stayProfit >= moveProfit:
                opt_city[i][j] = stayProfit
                cities[i][j] = j
            else:
                opt_city[i][j] = moveProfit
                cities[i][j] = 1 - j

    # creating chosen city list
    opt_cities = []
    j = opt_city[n].index(max(opt_city[n]))
    for i in range(n, 0, -1):
        opt_cities.append(j)
        j = cities[i][j]
    profit = max(opt_city[n][0], opt_city[n][1])
    return opt_cities[::-1], profit,


cities_earning = [[5, 21], [7, 8], [30, 15], [9, 8]]  # example 1
cities_earning_1 = [[5, 7], [21, 8], [12, 15], [10, 8]]  # example for C.I part
cities_earning_2 = [[5, 41], [3, 16], [30, 15], [12, 25]]  # example for C.II part
cost = 14
max_profit, selected_cities = maxProfit(cities_earning, cost)
max_profit_1, selected_cities_1 = maxProfit(cities_earning_1, cost)
max_profit_2, selected_cities_2 = maxProfit(cities_earning_2, cost)

print(selected_cities, "--", max_profit)
print(selected_cities_1, "--", max_profit_1)
print(selected_cities_2, "--", max_profit_2)

# Result:
# 54 -- [1, 1, 0, 0]
# 48 -- [0, 0, 0, 0]
# 97 -- [1, 1, 1, 1]
