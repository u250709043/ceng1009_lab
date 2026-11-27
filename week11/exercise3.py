def alternate_case(s: str) -> str:
  result = []
  for i, ch in enumerate(s):
    if i % 2 == 0:
      result.append(ch.upper())
    else:
      result.append(ch.lower())
  return "".join(result)

alternate_case("hello")