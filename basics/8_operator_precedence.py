# B-Brackets, O-Orders (powers/indices or roots), D-Division, M-Multiplication, A-Addition, S-Subtraction.

x = 10 + 3 * 2      # order of operations * happens first
print(x)

x = 10 + 3 * 2 ** 2     # order of operations ** happens first, then *, then +
print(x)


x = (10 + 3) * 2        # brackets executed first
print(x)