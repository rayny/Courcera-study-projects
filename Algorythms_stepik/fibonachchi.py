def main():
    n = int(input())
    n_1 = 0
    n_2 = 1
    if n < 2:
        print(n)
        return
    for i in range(2, n+1):
        n_3 = n_2 + n_1
        n_1 = n_2
        n_2 = n_3
    print(n_3)


if __name__ == "__main__":
    main()
