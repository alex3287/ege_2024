# +1 *2    win = 77    s1 = 7      1 <= s2 <= 69

# task 19
# def F(s1, s2, pos):
#     if s1 + s2 >= 77 and pos == 3: return True
#     if s1 + s2 < 77 and pos == 3: return False
#     if s1 + s2 >= 77: return False
#
#     if pos % 2 == 1:
#         return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)
#     return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)


# task 20
# def F(s1, s2, pos):
#     if s1 + s2 >= 77 and pos == 4: return True
#     if s1 + s2 < 77 and pos == 4: return False
#     if s1 + s2 >= 77: return False
#
#     if pos % 2 == 0:
#         return F(s1+1, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+1, pos+1) and F(s1, s2*2, pos+1)
#     return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)
# ответ 31 34

# task 21
def F(s1, s2, pos):
    if s1 + s2 >= 77 and (pos == 3 or pos == 5): return True
    if s1 + s2 < 77 and pos == 5: return False
    if s1 + s2 >= 77: return False

    if pos % 2 == 1:
        return F(s1+1, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+1, pos+1) and F(s1, s2*2, pos+1)
    return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)

for s2 in range(1, 70):
    if F(7, s2, 1):
        print(s2)