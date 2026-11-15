"""Decode golden ratio base (base phi) numbers in phi.txt into text."""
PHI = (1 + 5 ** 0.5) / 2
INT_DIGITS = 11

chunks = "".join(open("phi.txt").read().split()).split(".")
integers = [chunks[0]] + [c[-INT_DIGITS:] for c in chunks[1:-1]]
fractions = [c[:-INT_DIGITS] for c in chunks[1:-1]] + [chunks[-1]]

text = ""
for whole, frac in zip(integers, fractions):
    value = sum(PHI ** (len(whole) - 1 - i) for i, d in enumerate(whole) if d == "1")
    value += sum(PHI ** -(i + 1) for i, d in enumerate(frac) if d == "1")
    text += chr(round(value))
print(text)
