ABC = '0123456'
count = 0
for a in ABC[1:]:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    for f in ABC:
                        for g in ABC:
                            number = a+b+c+d+e+f+g
                            even = len([i for i in number if int(i)%2==0])
                            # number = number.replace('2', '0').replace('4','0').replace('6','0')
                            if even == 2:
                                count += 1
print(count)
