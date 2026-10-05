# TODO: shared behavior utilities
import random

def clamp(value, low=0.0, high=10.0):
    return max(low, min(high, value))

def move_toward(current, target, rate):
    if current < target:
        return current + rate
    if current > target:
        return current - rate
    return current

def random_drift(value, scale=0.01):
    return value + (random.random() - 0.5) * scale
