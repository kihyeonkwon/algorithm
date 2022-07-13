from datetime import datetime

now = datetime.now()
a = 0
a = now.year - 1900
b = a + now.month - 1
c = b + now.day

print(f"{a} {b} {c}")

