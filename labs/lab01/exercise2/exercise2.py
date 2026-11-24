# Lab 01 Exercise 2: Camping Logistics
import math
def calculate_tent_cost(participants, tent_capacity, tent_price):
    tent_amount = math.ceil (participants/tent_capacity)
    total = tent_amount * tent_price
    return total