# sum_squares.py

# A 버전: 타입 힌트 없는 함수
def sum_of_squares_no_type(lst):
    return sum(x * x for x in lst)

# B 버전: 타입 힌트 있는 함수
from typing import List

def sum_of_squares_typed(lst: List[int]) -> int:
    return sum(x * x for x in lst)