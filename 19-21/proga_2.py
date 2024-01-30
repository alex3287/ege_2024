# +5 *3 => 435      1 <= S <= 434
from functools import lru_cache
def move(s):
    return s+5, s*3

@lru_cache()
def game(s):
    if any(x > 434 for x in move(s)): return 'win_1'
    if all(game(x) == 'win_1' for x in move(s)): return 'win_2'
    if any(game(x) == 'win_2' for x in move(s)): return 'win_3'
    if all(game(x) == 'win_1' or game(x) == 'win_3' for x in move(s)): return 'win_4'


for s in range(1, 435):
    if game(s) == 'win_4':
        print(s)