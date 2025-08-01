import time

# 데코레이터 함수 정의
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()  # 시작 시각
        result = func(*args, **kwargs)  # 원래 함수 실행
        end = time.time()  # 종료 시각
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result  # 결과 반환
    return wrapper

# 테스트용 함수
@measure_time
def slow_function():
    time.sleep(1.5)  # 1.5초 지연
    return "완료!"

# 실행
result = slow_function()
print("함수 결과:", result)
