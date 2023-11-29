ABC = 'КЛОУН'
count = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                word = a + b + c + d
                if word.count('У') > 0:        #'У' in word:
                    print(word)
                    count += 1

print(count)