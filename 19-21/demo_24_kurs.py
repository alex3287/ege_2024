# +1 *2  129   1<=s<=128
# задача 19
def F(s, pos):
    if s >= 129 and pos == 3: return True
    if s < 129 and pos == 3: return False
    if s >= 129: return False

    if pos % 2 == 1:
        return F(s+1, pos+1) and F(s*2, pos+1)
    return F(s+1, pos+1) or F(s*2, pos+1)

# задача 20
# def F(s, pos):
#     if s >= 129 and pos == 4: return True
#     if s < 129 and pos == 4: return False
#     if s >= 129: return False
#
#     if pos % 2 == 0:
#         return F(s+1, pos+1) and F(s*2, pos+1)
#     return F(s+1, pos+1) or F(s*2, pos+1)


# задача 21
def F(s, pos):
    if s >= 129 and (pos == 3 or pos == 5): return True
    if s < 129 and pos == 5: return False
    if s >= 129: return False

    if pos % 2 == 1:
        return F(s+1, pos+1) and F(s*2, pos+1)
    return F(s+1, pos+1) or F(s*2, pos+1)


for s in range(1, 129):
    if F(s, 1):
        print(s)