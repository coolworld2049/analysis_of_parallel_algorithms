import threading
import time
from collections import Counter

from utils.partition import data_to_chunks

resultList = []


def count_char_sync(data: str, unique_data: set):
    resultList.append({item: data.count(item) for item in unique_data})


def mth_method(data: str, unique_data: set, thread_cnt: int):
    start = time.perf_counter()
    for ch in data_to_chunks(data, thread_cnt):
        th = threading.Thread(target=count_char_sync, args=(ch, unique_data))
        th.start()
        th.join()
    end = time.perf_counter()
    rep_char_count = Counter()
    for d in resultList:
        rep_char_count.update(d)

    return rep_char_count, start, end
