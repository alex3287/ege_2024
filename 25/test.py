from fnmatch import *


for i in range(0, 10**10, 2024):
    if fnmatch(str(i), '1?2157*4'):
        print(i, i / 2024)