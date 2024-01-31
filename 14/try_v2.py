from sys import set_int_max_str_digits


set_int_max_str_digits(0)
number = 4*3125**2019 + 3*625**2020 - 2*125**2021 + 25**2022 - 4*5**2023 - 2024
print(number)

count = 0
while number:
    if number % 25 > 10:
        count += 1
    number //= 25

print(count)