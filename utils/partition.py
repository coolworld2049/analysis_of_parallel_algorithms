def data_to_chunks(data: str, chunk_size: int):
    chunks = []
    for ch_index in range(0, len(data), chunk_size):
        sample = data[ch_index - chunk_size:ch_index]
        if sample != "":
            chunks.append(sample)
        if len(data) - ch_index <= chunk_size:
            dt_ch = data[ch_index:]
            chunks.append(dt_ch)
    return chunks
