DUMMY = -2
def generate_probes(hash_: int, mask: int) -> Iterable[int]:
  # STEP 1 - calculate index
  index = hash_ & mask
  yield index
  perturb = hash_
  while True:
    # STEP 6: hash collision. compute the new hash
    new_hash = (index * 5 + 1 + perturb)
    yield new_hash & mask
    perturb >>= 5

def lookup(key: Any, hash_: int) -> Tuple[int, Any]:
  mask = len(indices) - 1
  freeslot = None
  for index in generate_probes(hash_, mask):
    entry_index = indices[index]
    elem = entries[entry_index]
    if elem is None:
      # STEP 2 & 3 - empty element
      return (index, None) if freeslot is None else (freeslot, DUMMY)
    elif elem == DUMMY:
      # STEP 3 - dummy element
      if freeslot is None:
        freeslot = index
    # STEP 4 & 5: compare identity and hashes
    elif elem.key is key or (elem.hash == hash_ and elem.key == key):
      return (index, elem)
