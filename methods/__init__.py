from loguru import logger

path = "input/dataset.txt"
char_limit = 1000000

logger.info(f"path_to_data: {path}: char_limit: {char_limit}: reading ...")
with open(path, "r", encoding='utf-8') as rf:
    raw = rf.read()
input_str = raw[0:char_limit] if char_limit else raw
unique_chars = set(input_str)
logger.info(f"data_read: input_str: {len(input_str)}, unique_chars: {len(unique_chars)}")