from itertools import *


for i in product('01234567', repeat=5):
    s = ''.join(i)
    print(s)



# ABC = '01234567'
# count = 0
# for a in '1234567':
#     for b in ABC:
#         for c in ABC:
#             for d in ABC:
#                 for e in ABC:
#                     number = a + b + c + d + e
#                     if number.count('6') == 1:
#                         if ('16' not in number and '61' not in number and
#     '36' not in number and '63' not in number and '76' not in number
#         and '67' not in number and '56' not in number and '65' not in number):
#                             print(number)
#                             count += 1
# print(count)