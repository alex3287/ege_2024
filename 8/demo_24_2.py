ABC = '0234567'
count = 0
for a in ABC[1:]:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    word = a + b + c + d + e
                    # if len(set(word)) == 5 and (int(a) + int(b)) % 2 != 0 and (int(b) + int(c)) % 2 != 0 \
                    #         and (int(c) + int(d)) % 2 != 0 and (int(d) + int(e)) % 2 != 0:
                    if len(set(word)) == 5 and \
                            all([int(word[i]) % 2 != int(word[i+1]) % 2 for i in range(len(word)-1)]):
                        print([int(word[i]) % 2 != int(word[i+1]) % 2  for i in range(len(word)-1)])
                        print(word)
                        count += 1

print(count)