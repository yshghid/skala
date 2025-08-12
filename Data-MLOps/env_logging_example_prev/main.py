import logging
import os
from dotenv import load_dotenv

# 1. 환경변수 로딩
load_dotenv()
log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
app_name = os.getenv("APP_NAME", "DefaultApp")

# 2. 로그 레벨 문자열을 logging 모듈 상수로 매핑
level_dict = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}
log_level = level_dict.get(log_level_str, logging.INFO)

# 3. 로그 설정
log_format = "%(asctime)s | %(levelname)s | %(message)s"
log_handlers = [
    logging.StreamHandler(),  # 콘솔 출력
    logging.FileHandler("app.log", encoding="utf-8")  # 파일 저장
]
logging.basicConfig(level=log_level, format=log_format, handlers=log_handlers)

# 4. 로그 출력 테스트
logging.info(f"[{app_name}] 앱 실행 시작")
logging.debug("환경 변수 로딩 완료")
logging.error("예외 발생 예시")