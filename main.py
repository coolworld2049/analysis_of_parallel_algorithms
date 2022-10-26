from loguru import logger

from methods import input_str, unique_chars
from methods.async_method import async_method
from methods.mth_method import mth_method
from methods.sync_method import sync_method


def sort(data: dict, reverse: bool = None):
    return sorted(data.items(), key=lambda x: x[1], reverse=reverse if reverse else True)


if __name__ == "__main__":
    SYNC_METHOD, SYNC_METHOD_startime, SYNC_METHOD_endtime = sync_method(input_str, unique_chars)

    chunk_size = len(input_str) // 100
    ASYNC_METHOD, ASYNC_METHOD_startime, ASYNC_METHOD_endtime = async_method(input_str, unique_chars, chunk_size)

    thread_count = len(input_str) // 100
    MTH_METHOD, MTH_METHOD_startime, MTH_METHOD_endtime = mth_method(input_str, unique_chars, thread_count)

    SYNC_method_res = sort(SYNC_METHOD)
    ASYNC_method_res = sort(ASYNC_METHOD)
    MTH_METHOD_method_res = sort(MTH_METHOD)

    assert SYNC_method_res == ASYNC_method_res == MTH_METHOD_method_res, 'The results of different methods do not match'

    log_messages = dict()
    log_messages['SYNC_METHOD_timedelta'] = SYNC_METHOD_endtime - SYNC_METHOD_startime
    log_messages['ASYNC_METHOD_timedelta'] = ASYNC_METHOD_endtime - ASYNC_METHOD_startime
    log_messages['MTH_METHOD_timedelta'] = MTH_METHOD_endtime - MTH_METHOD_startime

    for m in sort(log_messages):
        logger.info(m)

    logger.info(f"SYNC_method_res: result_sample: {SYNC_method_res[:5]}")
    logger.info(f"ASYNC_method_res: result_sample: {ASYNC_method_res[:5]}")
    logger.info(f"MTH_METHOD_method_res: result_sample: {MTH_METHOD_method_res[:5]}")

