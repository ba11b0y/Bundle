from _datetime import datetime

BOND_TYPICAL_YIELD = 7.88/100
T_TYPICAL_YIELD = 6.5/100


def suggest_bundle(years, invested_amount, amount):
    b_allocation = 0.5
    t_allocation = 0.5
    while invested_amount <= amount:
        bond_returns = b_allocation * invested_amount * BOND_TYPICAL_YIELD*years
        t_returns = t_allocation * invested_amount * T_TYPICAL_YIELD*years
        invested_amount += bond_returns + t_returns
        b_allocation += 0.05
        t_allocation -= 0.05
    return round(b_allocation, 2), round(t_allocation, 2)
