# +5 *3 => 435      1 <= S <= 434

def win_1(s):
    return s + 5 >= 435 or s * 3 >= 435


def win_2(s):
    return not(win_1(s)) and win_1(s+5) and win_1(s*3)


def win_3(s):
    return win_2(s+5) or win_2(s*3)


def win_4(s):
    return win_1(s*3) and win_3(s+5) or win_1(s+5) and win_3(s*3)


for s in range(1, 435):
    if win_4(s):
        print(s)