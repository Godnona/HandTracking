# mày code vào branch_write
# code xong chạy ngon thì pull request đấy để t còn xem đc code m

def my_abs(value):
    return value if value >= 0 else -value

def my_sqrt(x):
    ok = 0.000000000000001
    kq = 1
    while my_abs(kq * kq - x) / x >= ok:
        kq = (x / kq + kq) / 2
    return kq

def hypotenuse(a, b):
    c=a*a+b*b
    return  my_sqrt(c)


def main():
    n = 1
    while n <= 100:
        print(my_sqrt(n))
        n += 1

if __name__ == "__main__":
    main()
