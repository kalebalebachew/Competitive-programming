# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def dcn(d):
    if d == 0:
        return 0
    else:
        return (d % 2 + 10 * dcn(d // 2))