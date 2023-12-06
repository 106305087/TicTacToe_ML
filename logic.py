class Board:
  def __init__(self):
    self._rows = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

  def __str__(self):
    s = '-------\n'
    for row in self._rows:
      for cell in row:
        s = s + '|'
        if cell == None:
          s=s+' '
        else:
          s=s+cell
      s = s + '|\n-------\n'
    return s

  def get(self, x, y):
    return self._rows[y][x]

  def set(self, x, y, value):
    self._rows[y][x] = value

  def get_winner(self):
    for row in self._rows:
      if len(set(row)) == 1 and row[0] is not None:
        return row[0]
    for i in range(len(self._rows)):
      column = [self._rows[j][i] for j in range(len(self._rows))]
      if len(set(column)) == 1 and column[0] is not None:
        return column[0]
    top_left_to_bottom_right = [self._rows[i][i] for i in range(len(self._rows))]
    if len(set(top_left_to_bottom_right)) == 1 and top_left_to_bottom_right[0] is not None:
      return top_left_to_bottom_right[0]

    top_right_to_bottom_left = [self._rows[i][len(self._rows)-i-1] for i in range(len(self._rows))]
    if len(set(top_right_to_bottom_left)) == 1 and top_right_to_bottom_left[0] is not None:
      return top_right_to_bottom_left[0]

    return None
