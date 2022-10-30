import asyncio
import time
from collections import Counter, defaultdict
from multiprocessing import cpu_count, Pool

import psutil
from loguru import logger
from matplotlib import pyplot as plt


def sort_result(data: dict, reverse: bool = None):
    return sorted(data.items(), key=lambda x: x[1], reverse=reverse if reverse else True)


def count_char(data: str):
    return {item: data.count(item) for item in set(data)}


def sync_method(data: str):
    st = time.perf_counter()
    rep_char_count = count_char(data)
    end = time.perf_counter()

    return rep_char_count, st, end, psutil.cpu_percent(4)


def data_to_chunks(_data: str, _chunk_sz: int):
    chunks = []
    for ch_index in range(0, len(_data), _chunk_sz):
        smpl = _data[ch_index - _chunk_sz:ch_index]
        if smpl != "":
            chunks.append(smpl)
        if len(_data) - ch_index <= _chunk_sz:
            dt_ch = _data[ch_index:]
            chunks.append(dt_ch)
    return chunks


def async_method(data: str, chunk_sz: int):
    unique_data = set(data)

    async def async_char_count():
        async def async_char_count_func(_data_chunk: str, _uq_data: set):
            return {item: _data_chunk.count(item) for item in _uq_data}

        tasks = [asyncio.create_task(async_char_count_func(ch, unique_data)) for ch in data_to_chunks(data, chunk_sz)]
        return await asyncio.gather(*tasks)

    st = time.perf_counter()
    res = asyncio.run(async_char_count())
    end = time.perf_counter()

    rep_char_count = Counter()
    for d in res:
        rep_char_count.update(d)

    return rep_char_count, st, end, psutil.cpu_percent(4)


def mpp_method(data: str, chunk_sz: int):
    with Pool(cpu_count() - 1) as p:
        chunks = [(ch,) for ch in data_to_chunks(data, chunk_sz)]
        start = time.perf_counter()
        result = p.starmap(count_char, chunks, chunksize=len(chunks))
        end = time.perf_counter()

    rep_char_count = Counter()
    for d in result:
        rep_char_count.update(d)

    return rep_char_count, start, end, psutil.cpu_percent(4)


if __name__ == "__main__":
    with open("input/dataset.txt", "r", encoding='utf-8') as rf:
        raw = rf.read()

    input_str: str = raw[0:10000000]
    step = 1000000
    divisor = 100
    exp_result = defaultdict(list)
    exp = 0

    logger.add('log.log', level="INFO", colorize=True, enqueue=True)
    logger.info(f"Общее количество символов в исходных данных: {len(input_str)}. Экспериментов: {len(input_str)//step}")

    for sample_size in range(step, len(input_str), step):
        if sample_size > 0:
            sample = input_str[:sample_size]
            chunk_size = len(sample) // divisor

            logger.info(f"\tЭксперимент №: {exp}, количество символов: {len(sample)}, размер куска данных при разбиении: {chunk_size}")

            SYNC_METHOD, SYNC_METHOD_startime, SYNC_METHOD_endtime, s_CPU = \
                sync_method(sample)
            logger.info(f"\t\tПоследовательный метод (сек.): {SYNC_METHOD_endtime - SYNC_METHOD_startime}")

            ASYNC_METHOD, ASYNC_METHOD_startime, ASYNC_METHOD_endtime, a_CPU = \
                async_method(input_str[:sample_size], chunk_size)
            logger.info(f"\t\tАсинхронный метод (сек.): {ASYNC_METHOD_endtime - ASYNC_METHOD_startime}")

            MPP_METHOD, MPP_METHOD_startime, MPP_METHOD_endtime, mpp_CPU = \
                mpp_method(sample, chunk_size)
            logger.info(f"\t\tМультипроцессорный метод time: {MPP_METHOD_endtime - MPP_METHOD_startime}")

            var = {
                exp: {
                    'sync_method': {
                        "timedelta": SYNC_METHOD_endtime - SYNC_METHOD_startime,
                        "consumption": s_CPU,
                    },
                    'async_method': {
                        "timedelta": ASYNC_METHOD_endtime - ASYNC_METHOD_startime,
                        "consumption": a_CPU,
                    },
                    'mpp_method': {
                        "timedelta": MPP_METHOD_endtime - MPP_METHOD_startime,
                        "consumption": mpp_CPU,
                    },
                    'common_consumption': psutil.cpu_percent(4),
                    'chunk_size': chunk_size,
                    'sample_size': len(sample),
                }
            }
            exp_result.update(var)
            exp += 1
    '''repo = "https://raw.githubusercontent.com/nicoguaro/matplotlib_styles/master"
    style = repo + "/styles/neon.mplstyle"'''

    x = range(len(exp_result))
    names = list(exp_result.keys())

    values_sm_timedelta = [x['sync_method']['timedelta'] for x in exp_result.values()]
    values_am_timedelta = [x['async_method']['timedelta'] for x in exp_result.values()]
    values_mp_timedelta = [x['mpp_method']['timedelta'] for x in exp_result.values()]

    # plt.style.use(style)
    plt.grid(zorder=3, alpha=0.2)
    plt.plot(x, values_sm_timedelta)
    plt.plot(x, values_am_timedelta)
    plt.plot(x, values_mp_timedelta)

    plt.title('Counting the frequency of repeated characters')
    plt.legend(['sync_method', 'async_method', 'multiproccesing_method'], loc='upper left')
    plt.xlabel("experiment number")
    plt.ylabel("time, s")
    plt.savefig("output/method_calculation_time.png", dpi=100)
    plt.close()

    # ---

    values_sm_consumption = [x['sync_method']['consumption'] for x in exp_result.values()]
    values_am_consumption = [x['async_method']['consumption'] for x in exp_result.values()]
    values_mp_consumption = [x['mpp_method']['consumption'] for x in exp_result.values()]

    # plt.style.use(style)
    plt.grid(zorder=3, alpha=0.2)
    common_consumption = [x['common_consumption'] for x in exp_result.values()]
    plt.plot(x, values_sm_consumption)
    plt.plot(x, values_am_consumption)
    plt.plot(x, values_mp_consumption)
    plt.plot(x, common_consumption, linestyle='--', linewidth=2)
    plt.title('CPU usage')
    plt.legend(['sync_method', 'async_method', 'multiproccesing_method', 'common_cpu'], loc='upper left')
    plt.xlabel("experiment number")
    plt.ylabel("cpu, %")
    plt.savefig("output/resource_consumption.png", dpi=100)
    plt.close()
