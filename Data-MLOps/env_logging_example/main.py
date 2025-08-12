import os
import logging
from logging import StreamHandler, FileHandler
from dotenv import load_dotenv

def configure_logging(level, filename="app.log"):
    """
    콘솔과 파일 모두에 로그를 출력하도록 설정하는 함수
    """
    # 로그 메시지 포맷 지정: 시간, [로그레벨], 메시지
    fmt = "%(asctime)s [%(levelname)s] %(message)s"
    formatter = logging.Formatter(fmt, "%Y-%m-%d %H:%M:%S")

    # 콘솔 출력 핸들러 생성
    sh = StreamHandler()
    sh.setFormatter(formatter)

    # 파일 출력 핸들러 생성
    fh = FileHandler(filename, encoding="utf-8")
    fh.setFormatter(formatter)

    # 루트 로거에 핸들러 적용 (기본 설정)
    logging.basicConfig(level=level, handlers=[sh, fh])

def main():
    # 1) .env 파일 로드
    load_dotenv()

    # 2) 환경 변수에서 로그 레벨과 앱 이름 읽기
    # .env에서 LOG_LEVEL을 읽어와 logging 모듈 상수로 변환
    log_level = getattr(logging, os.getenv("LOG_LEVEL"), logging.INFO)
    app_name = os.getenv("APP_NAME", "MyApp")

    # 3) 로깅 설정 적용
    configure_logging(log_level)

    # 4) 로그 메시지 출력
    logging.info("앱 실행 시작")  # INFO 레벨
    logging.debug(f"환경 변수 로딩 완료 (APP_NAME={app_name})")  # DEBUG 레벨

    # 5) 예외 발생 예시
    try:
        1 / 0  # ZeroDivisionError
    except ZeroDivisionError:
        # ERROR 레벨로 예외 메시지와 스택 트레이스 출력
        logging.error("예외 발생 예시", exc_info=True)

if __name__ == "__main__":
    # main() 함수 실행
    main()