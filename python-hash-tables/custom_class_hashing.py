class CustomClass:
  def __init__(self, name, type_, size):
    self.name = name
    self.type_ = type_
    self.size = size
    
  @property
  def _key(self):
    return (self.name, self.type_, self.size)

  def __hash__(self):
      return hash(self._key)

  def __eq__(self, other):
    if isinstance(other, CustomClass):
        return self._key == other._key
    return NotImplemented
