def get_min_max(ints):
   """
   Return a tuple(min, max) out of list of unsorted integers.

   Args:
      ints(list): list of integers containing one or more integers
   """
   if len(ints) == 0:
      return (None, None)
   min_ = ints[0]
   max_ = ints[0]
   for num in ints[1:]:
      min_ = min(min_, num)
      max_ = max(max_, num)
   return (min_, max_)


if __name__ == '__main__':
   # Example Test Case of Ten Integers
   print(get_min_max([10, 20, -10, -20, 100, -99999, 2]))
   print(get_min_max([]))
   print(get_min_max([1]))
   print(get_min_max([100, 1]))
   print(get_min_max([-10, 0]))
