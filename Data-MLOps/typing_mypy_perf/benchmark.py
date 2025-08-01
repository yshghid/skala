# benchmark.py

import timeit
import random
from sum_squares import sum_of_squares_no_type, sum_of_squares_typed

# 테스트 데이터 생성
test_data = [random.randint(1, 100) for _ in range(100000)]

# 타입 힌트 없는 함수 실행 시간
time_no_type = timeit.timeit(
    "sum_of_squares_no_type(test_data)",
    globals=globals(),
    number=100
)

# 타입 힌트 있는 함수 실행 시간
time_typed = timeit.timeit(
    "sum_of_squares_typed(test_data)",
    globals=globals(),
    number=100
)

# 결과 출력
print(f"No Type Hint Time: {time_no_type:.4f} sec")
print(f"With Type Hint Time: {time_typed:.4f} sec")
