#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    fact=1
    for i in range(n):
        fact *= i+1

    print(fact)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)