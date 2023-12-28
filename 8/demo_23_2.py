ABC = '01234567'
count = 0
for a in ABC:
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    word = a+b+c+d+e
                    # if a != '0' and len(set(word)) == 5 and int(a) % 2 != int(b) % 2 and int(b) % 2 != int(c) % 2 \
                    #         and int(c) % 2 != int(d) % 2 and int(d) % 2 != int(e) % 2:
                    if a != '0'
                        '6' and int(b) % 2 != 0):
                        print(word)
                        count += 1
print(count)