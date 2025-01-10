revenue = {
    'Johnver': {'Tea': 190, 'Coffee': 325, 'Water': 682, 'Milk': 829},
    'Vanston': {'Tea': 140, 'Coffee': 19, 'Water': 14, 'Milk': 140},
    'Danbree': {'Tea': 1926, 'Coffee': 293, 'Water': 852, 'Milk': 609},
    'Vansey': {'Tea': 14, 'Coffee': 1491, 'Water': 56, 'Milk': 120},
    'Mundyke': {'Tea': 143, 'Coffee': 162, 'Water': 659, 'Milk': 87}
}

expenses = {
    'Johnver': {'Tea': 120, 'Coffee': 300, 'Water': 50, 'Milk': 67},
    'Vanston': {'Tea': 65, 'Coffee': 10, 'Water': 299, 'Milk': 254},
    'Danbree': {'Tea': 890, 'Coffee': 23, 'Water': 1290, 'Milk': 89},
    'Vansey': {'Tea': 54, 'Coffee': 802, 'Water': 12, 'Milk': 129},
    'Mundyke': {'Tea': 430, 'Coffee': 235, 'Water': 145, 'Milk': 76}
}

commission_rate = 0.062

def calculate_profit(person, item):
    return revenue[person][item] - expenses[person][item]

commissions = {}

for person in revenue:
    total_profit = 0
    for item in revenue[person]:
        profit = calculate_profit(person, item)
        if profit > 0:
            total_profit += profit
    commission = total_profit * commission_rate
    commissions[person] = commission

names = list(commissions.keys())
commission_values = [f"{commissions[name]:.0f}" for name in names]

print(" ".join(commission_values))
