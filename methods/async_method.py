import asyncio
import time
from collections import Counter

from utils.partition import data_to_chunks


def async_method(data: str, unique_data: set, chunk_sz: int):
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

    return rep_char_count, st, end
