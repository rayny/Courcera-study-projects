def main():
    n, m = map(lambda x: int(x.strip()), input().strip().split())
    n_1 = 0
    n_2 = 1
    if n < 2:
        print(n % m)
        return
    for i in range(2, n+1):
        n_3 = (n_2 + n_1) % m
        n_1 = n_2
        n_2 = n_3
        if (n_1 == 0) & (n_2 == 1):
            per = i
            break

    try:
        n2 = n % (per - 1)
        n_1 = 0
        n_2 = 1
        if n2 < 2:
            print(n2 % m)
            return
        for i in range(2, n2+1):
            n_3 = (n_2 + n_1) % m
            n_1 = n_2
            n_2 = n_3
    except UnboundLocalError:
        pass
    print(n_3)


if __name__ == "__main__":
    main()
