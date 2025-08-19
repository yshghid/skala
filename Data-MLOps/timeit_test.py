import timeit
import random
from typing import List

# timeit을 사용하여 실행 성능 측정
def measure_time(func): # 함수를 실행하고 소요 시간을 측정
    def wrapper(*args, **kwargs):
        elapsed_time = timeit.timeit(lambda: func(*args, **kwargs), number=100) # 전달받은 함수를 100번 실행하고 총 소요 시간을 반환
        return elapsed_time # 측정된 총 실행 시간 반환
    return wrapper # wrapper 실행, wrapper 내부에서 시간 측정 후 원래 함수를 호출

# A 버전 : 타입 힌트를 사용하지 않은 함수
def sum_of_squares_no_type(lst): # 인자는 lst: 자료형 제한 없음 (타입 힌트 없음)
    return sum(x * x for x in lst) # 각 원소를 제곱하고 모두 더함

# B 버전 : 타입 힌트를 적용한 함수
def sum_of_squares_typed(lst: List[int]) -> int: # 인자 lst는 정수(int) 요소들로 이루어진 리스트, 반환값은 정수 (타입 힌트)
    return sum(x * x for x in lst) # 각 원소를 제곱하고 모두 더함

# 성능 비교용 함수들
@measure_time # 데코레이터: run_no_type 실행시 자동으로 실행 시간을 측정
def run_no_type(test_data): # test data: 성능 측정 대상 데이터(정수 리스트)
    sum_of_squares_no_type(test_data) # test_data 리스트 내 각 원소 제곱 후 합산

@measure_time # 데코레이터: run_typed 실행시 자동으로 실행 시간을 측정
def run_typed(test_data): # test data: 성능 측정 대상 데이터(정수 리스트)
    sum_of_squares_typed(test_data) # test_data 리스트 내 각 원소 제곱 후 합산

if __name__ == "__main__":
    # 테스트 데이터 생성
    test_data = [random.randint(1, 100) for _ in range(1_000_000)]

    # 실행 시간 측정
    time_no_type = run_no_type(test_data) # test_data 내 원소 제곱 후 합산 -> @measure_time 데코레이터로 실행 시간 측정
    time_typed = run_typed(test_data)

    print(f"No Type Hint Time : {time_no_type:.4f} sec") # 타입 힌트 없는 버전 결과 출력 
    print(f"With Type Hint Time : {time_typed:.4f} sec") # 타입 힌트 있는 버전으로 결과 출력