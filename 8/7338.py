ABC = 'КАТЕР'
count = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    for f in ABC:
                        word = a+b+c+d+e+f
                        if a == 'Р' and f == 'К':
                            print(word)
                            count += 1
print(count)