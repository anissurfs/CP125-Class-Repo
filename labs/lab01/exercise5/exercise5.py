# Lab 01 Exercise 5: Triangle Checker
def is_valid_triangle (a, b ,c):
    if c < (a + b) and a < (b + c) and b <(a + c): 
        return True
    else:
        return False