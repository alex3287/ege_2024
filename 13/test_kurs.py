# x.x.x.x =>  0 <= x <= 255 ==> 11111111
# Mask -> 11111...11000...0
# NetworkAdres = IP & Mask
# print(int('11111111', 2))
print(10 & 255, 8 & 255, 248 & 224, 131 & 0)