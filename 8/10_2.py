ABC = 'АКРУ'
count = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    word = a + b + c + d + e
                    count += 1
                    if word == 'УКАРА':

                        print(count, word)
