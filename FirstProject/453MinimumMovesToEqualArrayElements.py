# tang (n-1) gia tri len 1 ~~ giam? gia tri con` lai di 1
# ==> tinh' so lan giam gia tri di 1
# gia tri toi thieu la MIN(array)
def minimum_moves(array):
    array_sum = sum(array)

    print array_sum - len(array) * min(array)

    return 0


if __name__ == '__main__':
    array_number = [1, 2, 3]
    minimum_moves(array_number)
