# 12. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import random
import time
from unittest import result

def getRand(x, y):
    count = y - x
    result = int(time.time()) % count # время начала
    return result + x

print(getRand(25, 100))