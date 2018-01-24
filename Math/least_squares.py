import numpy as np


def solver(matrix):
    if (matrix.shape[0] > 1) and (matrix.shape[1] > 1):
        if abs(matrix[0, 0]) < 0.000001:
            for i in range(1, matrix.shape[0]):
                if abs(matrix[i, 0]) > 0.000001:
                    temp = matrix[0, :]
                    temp = list(temp)
                    matrix[0, :] = matrix[i, :]
                    matrix[i, :] = np.array(temp)
                    return solver(matrix)
            ans, roots = solver(matrix[1:, 1:])
            if ans == 'NO':
                return ans, []
            else:
                return 'INF', []
        else:
            for i in range(1, matrix.shape[0]):
                matrix[i, :] -= matrix[0, :]*(matrix[i, 0]/matrix[0, 0])
            ans, roots = solver(matrix[1:, 1:])
            if ans == 'NO':
                return ans, []
            elif ans == 'INF':
                return ans, []
            else:
                matrix[0, :] = matrix[0, :]/matrix[0, 0]
                root1 = matrix[0, matrix.shape[1]-1]
                for i in range(1, matrix.shape[1]-1):
                    root1 -= roots[i-1]*matrix[0, i]
                return ans, [root1] + roots
    else:
        if matrix.shape[1] == 1:
            for i in range(0, matrix.shape[0]):
                if abs(matrix[i, 0]) > 0.0000001:
                    return 'NO', []

            return 'YES', []
        elif matrix.shape[0] == 1:
            if matrix.shape[1] == 2:
                if abs(matrix[0, 0]) > 0.000001:
                    return 'YES', [matrix[0, 1]/matrix[0, 0], ]
                elif abs(matrix[0, 1]) > 0.000001:
                    return 'NO', []
                else:
                    return 'INF', []
            else:
                for i in range(0, matrix.shape[1]-1):
                    if abs(matrix[0, i]) > 0.0000001:
                        return 'INF', []
                if abs(matrix[0, matrix.shape[1]-1]) > 0.000001:
                    return 'NO', []
                else:
                    return 'INF', []
    return ans, matrix


def estimator(matrix):
    f = np.copy(matrix[:, -1])

    X = np.copy(matrix[:, :-1])
    mt1 = X.T.dot(X)
    f1 = X.T.dot(f)
    ans = solver(np.hstack((mt1, f1.reshape(-1,1))))
    return ans[1]


def data_handler():
    data = input()
    n = int(data.split(' ')[0].strip())
    m = int(data.split(' ')[1].strip())
    matrix = []
    for i in range(n):
        data1 = input()
        try:
            data_spl = list(map(lambda x: float(x.strip()), data1.strip().split(' ')))
        except ValueError:
            raise ValueError(data1.split(' '))
        matrix.append(data_spl)
    matrix1 = np.array(matrix)
    return estimator(matrix1)

result = data_handler()
print(*result)
