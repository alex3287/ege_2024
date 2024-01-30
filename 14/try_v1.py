number = 2*729**2019 + 2*243**2020 - 81**2021 + 2*27**2022 - 2*9**2023 - 2024
print(number)
count = 0
while number > 0:
    if number % 9 != 0:
        count += 1
    number //= 9

print(count)