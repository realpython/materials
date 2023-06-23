def split_list(a_list, chunk_size):
    chunks = []
    for start in range(0, len(a_list), chunk_size):
        stop = start + chunk_size
        chunks.append(a_list[start:stop])
    return chunks
