def split_list(list_object, chunk_size):
    chunks = []
    for start in range(0, len(list_object), chunk_size):
        stop = start + chunk_size
        chunks.append(list_object[start:stop])
    return chunks
