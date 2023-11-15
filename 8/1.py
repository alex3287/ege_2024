ABC = 'ЛЕТО'
count = 0
for a in 'ЛТ':
    for b in ABC:
        for c in ABC:
            for d in ABC:
                count += 1
                word = a + b + c + d
                print(word)
print(count)