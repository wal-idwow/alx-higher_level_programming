#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight = 0
    weighted_sum = 0

    for value, weight in my_list:
        total_weight += weight
        weighted_sum += value * weight

    return weighted_sum / total_weight if total_weight != 0 else 0
