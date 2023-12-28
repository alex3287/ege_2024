
ABC = 'АКРУ'
counter = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    word = a+b+c+d+e
                    counter += 1
                    print(counter, word)
print(counter)