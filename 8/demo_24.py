ABC = '0234567'
count = 0
for a in '234567':
    for b in ABC:
        for c in ABC:
            for d in ABC:
                for e in ABC:
                    number = a + b + c + d + e
                    if len(number) == len(set(number)):
                        # if all([int(number[i]) % 2 != int(number[i+1]) % 2 for i in range(len(number)-1)]):
                        if int(a) % 2 == 0 and int(b)%2==1 and int(c) % 2 == 0 and int(d)%2==1 and int(e)%2==0:
                            count += 1
                        if int(a) % 2 == 1 and int(b) % 2 == 0 and int(c) % 2 == 1 and int(d) % 2 == 0 and int(e) % 2 == 1:
                            count += 1
print(count)


A = [i for i in range(16)]
B = [i for i in range(16) if i > 9]
C = [i for i in range(16) if i % 2 == 0]
print(A)
print(B)
print(C)
print(any(i%2==1 for i in C))
