try:
    y = lambda t: t**2-2*t-5
    print(max(y(x) for x in range(100) if y(x) % 3 == 0))
except ValueError:
    print("ninguno")
