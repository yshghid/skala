import random
import time
import math
from multiprocessing import Pool, cpu_count

# 소수 판별 함수
def is_prime(n):
    if n < 2: # 0, 1, 음수는 소수가 아니므로 
        return False # False로 종료
    for i in range(2, int(math.isqrt(n)) + 1): # 나눠볼 후보 약수: 2부터 √n.
        if n % i == 0: # 나누어떨어지는 i를 찾으면 합성수이므로 
            return False # 바로 False로 종료
    return True # √n까지 어떤 i로도 나누어떨어지지 않으면 소수

# 단일 프로세스 소수 세기
def count_primes_single(numbers):
    start = time.perf_counter() # 시작 시간 기록
    count = sum(1 for num in numbers if is_prime(num)) # 소수 판별 결과가 True인지 확인, True이면 더해서 count를 구함
    end = time.perf_counter() # 종료 시간 기록
    return count, end - start # 경과 시간 계산 (소수 개수, 걸린 시간초 반환)

# 멀티 프로세스 소수 세기
def count_primes_multi(numbers):
    start = time.perf_counter() # 시작 시간 기록
    with Pool(processes=cpu_count()) as pool: # CPU 코어 수만큼 프로세스를 띄워 Pool 구성
        results = pool.map(is_prime, numbers) # numbers 리스트를 프로세스들에 분할 배정해 병렬 처리: 워커 프로세스에서 is_prime 검사를 각 정수에 수행
    count = sum(results) # results 내 True(1)의 합으로 소수 개수 구하기
    end = time.perf_counter() # 종료 시간 기록
    return count, end - start # 경과 시간 계산

if __name__ == "__main__":
    N = 10_000_000  
    numbers = [random.randint(1, 10_000_000) for _ in range(N)] # 1 ≤ x ≤ 10,000,000 범위에서 난수 리스트 생성

    # 단일 프로세스
    sp_count, sp_time = count_primes_single(numbers) # numbers에 대해 단일 프로세스로 소수 판별 -> 소수 개수, 경과 시간 반환
    print(f"[단일] 소수 개수: {sp_count}, 시간: {sp_time:.2f}초") # 소수점 둘째 자리까지 출력

    # 멀티 프로세스
    mp_count, mp_time = count_primes_multi(numbers) # numbers에 대해 multi processing으로 소수 판별 -> 소수 개수, 경과 시간 반환
    print(f"[멀티] 소수 개수: {mp_count}, 시간: {mp_time:.2f}초") # 소수점 둘째 자리까지 출력