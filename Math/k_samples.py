def sampler(n, k):
    output1 = []
    if k > 1:
        for i in range(len(n)):
            res = sampler(n[:i] + n[i+1:], k-1)
            for ji in res:
                output1.append([n[i]]+ji)
        return output1
    else:
        for i in range(len(n)):
            output1.append([n[i]])
        return output1


def data_handler():
    data = input()
    n = int(data.split(' ')[0].strip())
    k = int(data.split(' ')[1].strip())
    return n, k

if __name__ == '__main__':
    args = data_handler()
    output = sampler(list(range(args[0])), args[1])
    for i in output:
        print(*i)
