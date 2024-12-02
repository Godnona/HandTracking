
PI = 3.14159

def sqrt(x):
    left = 1
    right = x
    res = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            res = mid
        elif mid * mid < x:
            left = mid + 1
            res = mid
        else:
            right = mid - 1
    return res

def hypotenuse(a, b):
    return sqrt(a * a + b * b)


def main():
    a = 3
    b = 4
    print(sqrt(16))

if __name__ == "__main__":
    main()
