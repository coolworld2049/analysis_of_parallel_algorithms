import time


def sync_method(data: str, unique_data: set):
    def count_char_sync():
        return {item: data.count(item) for item in unique_data}

    st = time.perf_counter()
    rep_char_count = count_char_sync()
    end = time.perf_counter()

    return rep_char_count, st, end

