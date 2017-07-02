def nim_game(stones):
    # assume that you win, before that there are 4 stone remaining & your friends pick first
    # so we subtract amount_of_stone for 4 until amount <= 4
    # SO amount_of_stones % 4 == 0    ==>   YOU NEVER WIN

    if stones % 4 != 0:
        return 'MAY BE YOU WIN'
    else:
        return 'YOU NEVER WIN'


if __name__ == '__main__':
    amount_of_stones = 1458
    print nim_game(amount_of_stones)
