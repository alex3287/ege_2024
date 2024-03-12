def devisions(number):
    count = 0
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            count += 2
    return count


count_maxi = 10
count_cur = 0
for i in range(10**10, 100_000_000_001):
    count_dev = devisions(i)
    if count_dev > count_maxi:
        print(f'EEEEEEEEEEEEEEEEEEEEEEEEEEeeeeeeeeeeeeee{i}')
    count_maxi = max(count_maxi, count_dev)
    print(f'{i} ->{count_dev} -> {count_maxi}')

