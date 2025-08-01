import random
import time
import math
from multiprocessing import Pool, cpu_count

# 1. 소수 판별 함수
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 2. 난수 생성
NUM_COUNT = 10_000_000
random_nums = [random.randint(1, 100_000) for _ in range(NUM_COUNT)]

# 3. 단일 프로세스 처리 함수
def count_primes_sequential(nums):
    start = time.time()
    count = sum(1 for n in nums if is_prime(n))
    end = time.time()
    print(f"[단일 처리] 소수 개수: {count}, 시간: {end - start:.2f}초")
    return count

# 4. 멀티 프로세스 처리 함수 (Pool 사용)
def count_primes_parallel(nums):
    start = time.time()
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(is_prime, nums)
    count = sum(results)
    end = time.time()
    print(f"[병렬 처리] 소수 개수: {count}, 시간: {end - start:.2f}초")
    return count

# 5. 실행
if __name__ == '__main__':
    count_primes_sequential(random_nums)
    count_primes_parallel(random_nums)
