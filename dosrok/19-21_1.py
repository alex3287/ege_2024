# +1 *2  123  s1 = 13,  1<=s2<=109

# def F(s1, s2, pos):
#     if s1+s2 >= 123 and pos == 3: return True
#     if s1+s2 < 123 and pos == 3: return False
#     if s1+s2 >= 123: return False
#
#     if pos % 2 == 1:
#         return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)
#     return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)
#28

def F(s1, s2, pos):
    if s1+s2 >= 123 and (pos == 3 or pos == 5): return True
    if s1+s2 < 123 and pos == 5: return False
    if s1+s2 >= 123: return False

    if pos % 2 == 1:
        return F(s1+1, s2, pos+1) and F(s1*2, s2, pos+1) and F(s1, s2+1, pos+1) and F(s1, s2*2, pos+1)
    return F(s1+1, s2, pos+1) or F(s1*2, s2, pos+1) or F(s1, s2+1, pos+1) or F(s1, s2*2, pos+1)
# 28
# 48
# 54
# 47

for s2 in range(1, 110):
    if F(13, s2, 1):
        print(s2)