ABC = '014689ACEFG'
count = 0
for a in range(11):
    for b in range(11):
        for c in range(11):
            for d in range(11):
                for e in range(11):
                    for f in range(11):
                        number = ABC[a] + ABC[b] + ABC[c] + ABC[d] + ABC[e] + ABC[f]
                        print(number)
                        # if len(set(number)) == 6:
                        #     if len(number) == 6:
                        #         print(number)
                        #         count += 1
print(count)