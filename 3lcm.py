def lcm_random_generator(seed, a, c, m):
    x = seed

    while True:
      if (c == 0):#multiplicative
        x = (a * x) % m
      else: #additive
        x = (a * x + c) % m
      yield x / m

# Example usage
seed = 42  # You can choose any seed value
a = 13
c = 2
m = 2**32

generator = lcm_random_generator(seed, a, c, m)

# Generate 10 random numbers
for _ in range(10):
    random_number = next(generator)
    print(random_number)
