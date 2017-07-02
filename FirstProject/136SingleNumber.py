# cho mang so nguyen
# moi~ gia' tri xuat hien 2 lan
# duy nhat 1 gia tri chi xuat hien 1 lan
# tim gia tri do'
# -------------
# 2n+1 gia' tri
# chia doi dua theo gia tri trung vi ==> 2 tap
# tap nao co so luong le? ==> tiep tuc xu? ly'
def single_number(array):
    if len(array) == 1:
        print array
    else:
        print array
        bigger = []
        middle = []
        smaller = []
        # separating into 2 smaller group
        for number in array:
            if number > array[(len(array) - 1) / 2]:
                bigger.extend([number])
            else:
                if number < array[(len(array) - 1) / 2]:
                    smaller.extend([number])
                else:
                    middle.extend([number])

        if len(bigger) % 2 != 0:
            single_number(bigger)
        else:
            if len(smaller) % 2 != 0:
                single_number(smaller)
            else:
                single_number(middle)
    return


if __name__ == '__main__':
    array_number = [2, 5, 4, 3, 6, 4, 5, 2, 3, 8, 6, 12, 14, 16, 14, 16, 12]
    single_number(array_number)
