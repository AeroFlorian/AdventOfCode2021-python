input="""6788383436
5526827441
4582435866
5152547273
3746433621
2465145365
6324887128
8537558745
4718427562
2283324746"""

input_test = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def flash(matrix, i, j):
    if matrix[i][j] < 10:
        return 0
    res = 1
    matrix[i][j] = -1
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x in range(len(matrix)) and y in range(len(matrix[x])) and (x != i or y != j):
                if matrix[x][y] != -1:
                    matrix[x][y] += 1
                    res += flash(matrix, x, y)
    return res


def first_star():
    input_list = list(map(list, input.split('\n')))
    input_num = [list(map(int, x)) for x in input_list]
    res = 0
    for x in range(100):
        for i in range(len(input_num)):
            for j in range(len(input_num[i])):
                if input_num[i][j] != -1:
                    input_num[i][j] += 1
                    res += flash(input_num, i, j)
        for i in range(len(input_num)):
            for j in range(len(input_num[i])):
                if input_num[i][j] == -1:
                    input_num[i][j] = 0
    print(f"First star: {res}")

def check_all(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                return True
    return False


def second_star():
    input_list = list(map(list, input.split('\n')))
    input_num = [list(map(int, x)) for x in input_list]
    x = 0
    while check_all(input_num):
        for i in range(len(input_num)):
            for j in range(len(input_num[i])):
                if input_num[i][j] != -1:
                    input_num[i][j] += 1
                    flash(input_num, i, j)
        for i in range(len(input_num)):
            for j in range(len(input_num[i])):
                if input_num[i][j] == -1:
                    input_num[i][j] = 0
        x += 1
    print(f"Second star: {x}")



if __name__ == '__main__':
   first_star()
   second_star()

