# mày code vào branch_write
# code xong chạy ngon thì pull request đấy để t còn xem đc code m

def my_abs(value):
    return value if value >= 0 else -value

def my_sqrt(x):
    if x < 0:
        return 0
    if x == 0:
        return 0

    ok = 1e-12
    kq = x if x >= 1 else 1
    while abs(kq * kq - x) / x >= ok:
        kq = (x / kq + kq) / 2
    return kq

def hypotenuse(a, b):
    c=a*a+b*b
    return  my_sqrt(c)

    pass

def main():
    print(my_sqrt(9))
    pass

if __name__ == "__main__":
    main()
