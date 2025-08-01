import time
import sys

# 1. 일반 리스트 방식
numbers = list(range(1_000_000))
print("리스트 합:", sum(numbers))
print("리스트 메모리 사용량:", sys.getsizeof(numbers))  # 리스트 전체를 메모리에 올림

# 2. 제너레이터 방식
def number_gen():
    for i in range(1_000_000):
        yield i

gen = number_gen()
print("제너레이터 합:", sum(gen))
print("제너레이터 메모리 사용량:", sys.getsizeof(gen))  # 제너레이터 객체만 메모리 차지

# 1. 짝수의 제곱을 생성하는 제너레이터
def even_square_gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i * i

# 2. 실행 및 시간 측정
start = time.time()
result = sum(even_square_gen(1_000_000))
end = time.time()

print("짝수 제곱 총합:", result)
print("실행 시간:", end - start)

# 3. 메모리 사용량 측정
gen_obj = even_square_gen(1_000_000)
print("제너레이터 메모리 사용량:", sys.getsizeof(gen_obj))  # 보통 수십~수백 바이트
