def euclid(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a > b:
            return euclid(a % b, b)
        else:
            return euclid(a, b % a)


def main():
    a, b = map(lambda x: int(x.strip()), input().strip().split())
    print(euclid(a, b))

if __name__ == '__main__':
    main()
