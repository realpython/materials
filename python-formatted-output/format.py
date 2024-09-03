print(f"{257:b}")
print("{:b}".format(257))

print(f"{42:c}")
print("{:c}".format(42))

print(f"{3.14159:g}")
print(f"{-123456789.8765:g}")
print("{:g}".format(3.14159))
print("{:g}".format(-123456789.8765))

print(f"{-123456789.8765:G}")
print("{:G}".format(-123456789.8765))

infinite = float("inf")
not_a_number = infinite * 0
print(f"{infinite:g}")
print(f"{not_a_number:g}")
print(f"{infinite:G}")
print(f"{not_a_number:G}")
print("{:g}".format(infinite))
print("{:g}".format(not_a_number))
print("{:G}".format(infinite))
print("{:G}".format(not_a_number))

print(f"{'Hi':8s}")
print(f"{123:8d}")
print("{0:8s}".format("Hi"))
print("{0:8d}".format(123))

print("{0:2s}".format("Pythonista"))

print(f"{'Hi':<8s}")
print(f"{123:<8d}")
print("{0:<8s}".format("Hi"))
print("{0:<8d}".format(123))

print(f"{'Hi':>8s}")
print(f"{123:>8d}")
print("{0:>8s}".format("Hi"))
print("{0:>8d}".format(123))

print(f"{'Hi':^8s}")
print(f"{123:^8d}")
print("{0:^8s}".format("Hi"))
print("{0:^8d}".format(123))

print(f"{123:+8d}")
print(f"{-123:+8d}")
print("{0:+8d}".format(123))
print("{0:+8d}".format(-123))

print(f"{123:=+8d}")
print(f"{-123:=+8d}")
print("{0:=+8d}".format(123))
print("{0:=+8d}".format(-123))

print(f"{'Hi':->8s}")
print(f"{123:#<8d}")
print(f"{'Hi':*^8s}")
print("{0:->8s}".format("Hi"))
print("{0:#<8d}".format(123))
print("{0:*^8s}".format("Hi"))

print(f"{123:+6d}")
print(f"{-123:+6d}")
print("{0:+6d}".format(123))
print("{0:+6d}".format(-123))

print(f"{123:-6d}")
print(f"{-123:-6d}")
print("{0:-6d}".format(123))
print("{0:-6d}".format(-123))

print(f"{123:*> 6d}")
print(f"{-123:*> 6d}")
print("{0:*> 6d}".format(123))
print("{0:*> 6d}".format(-123))

value = 16
print(f"{value:b}, {value:#b}")
print(f"{value:o}, {value:#o}")
print(f"{value:x}, {value:#x}")
print("{0:b}, {0:#b}".format(value))
print("{0:o}, {0:#o}".format(value))
print("{0:x}, {0:#x}".format(value))

print(f"{123:.0f}, {123:#.0f}")
print(f"{123:.0e}, {123:#.0e}")
print("{0:.0f}, {0:#.0f}".format(123))
print("{0:.0e}, {0:#.0e}".format(123))

print(f"{123:05d}")
print(f"{12.3:08.1f}")
print("{0:05d}".format(123))
print("{0:08.1f}".format(12.3))

print(f"{'Hi':>06s}")
print("{0:>06s}".format("Hi"))

print(f"{123:*>05d}")
print("{0:*>05d}".format(123))

print(f"{1234567:,d}")
print(f"{1234567:_d}")
print(f"{1234567.89:,.2f}")
print(f"{1234567.89:_.2f}")
print("{0:,d}".format(1234567))
print("{0:_d}".format(1234567))
print("{0:,.2f}".format(1234567.89))
print("{0:_.2f}".format(1234567.89))

print(f"{0b111010100001:_b}")
print(f"{0b111010100001:#_b}")
print(f"{0xae123fcc8ab2:_x}")
print(f"{0xae123fcc8ab2:#_x}")
print("{0:_b}".format(0b111010100001))
print("{0:#_b}".format(0b111010100001))
print("{0:_x}".format(0xAE123FCC8AB2))
print("{0:#_x}".format(0xAE123FCC8AB2))

print(f"{1234.5678:8.2f}")
print(f"{1.23:8.4f}")
print(f"{1234.5678:8.2e}")
print(f"{1.23:8.4e}")
print("{0:8.2f}".format(1234.5678))
print("{0:8.4f}".format(1.23))
print("{0:8.2e}".format(1234.5678))
print("{0:8.4e}".format(1.23))

print(f"{'Pythonista':.6s}")
print("{0:.6s}".format("Pythonista"))

width = 10
prec = 2
print(f"{123.4567:{width}.{prec}f}")
print("{2:{0}.{1}f}".format(width, prec, 123.4567))
print(
    "{number:{width}.{prec}f}".format(width=width, prec=prec, number=123.4567)
)
