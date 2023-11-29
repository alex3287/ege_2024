ABC = 'КРОЙ'
count = 0
for a in 'КРО':
    for b in ABC:
        for c in ABC:
            for d in ABC:
                word = a + b + c + d
                if len(set(word)) == 4 and 'ОЙ' not in word:
                    print(word, set(word), len(set(word)))
                    count += 1

print(count)