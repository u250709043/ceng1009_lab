def digit_sum(n: int) -> int:
  if n < 0:
    raise ValueError("n must be a non-negative whole number")

  total = 0
  while n > 0:
    total += n % 10
    n //= 10
  return total

digit_sum(11)