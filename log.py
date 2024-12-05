import os
import datetime
from loguru import logger

dateTime = datetime.datetime.now().strftime('%Y-%m-%d')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(BASE_DIR, f'logs/{dateTime}.log')
logger.add(log_file_path, format="{time:YYYY-MM-DD at HH:mm:ss.SSS.ffff} | {level} | {message}", retention="1 days", encoding='utf-8')  # 一段时间后会清空
