# problem19.py

import datetime

sun = 0

for y in range(1901, 2001):
    for m in range(1, 13):
        if datetime.date(y, m, 1).isoweekday() == 7:
            sun += 1

print(sun)
