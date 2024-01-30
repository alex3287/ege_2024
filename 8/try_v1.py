ABC = '0123456'
count = 0
for a in ABC[1:]:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    for f in ABC:
                        number = a+b+c+d+e+f

                        if number.count('3') == 1:
                            number = number.replace('1', '+').replace('3','+').replace('5', '+')
                            if '++' not in number:

                        #     if int(a)*int(b) % 2 != 1:
                        #         if int(b) * int(c) % 2 != 1:
                        #             if int(c) * int(d) % 2 != 1:
                        #                 if int(d) * int(e) % 2 != 1:
                        #                     if int(e) * int(f) % 2 != 1:
                            # if all(int(number[i])*int(number[i+1])%2 != 1 for i in range(len(number)-1)):
                                count += 1
                                print(number)
print(count)
# 16448