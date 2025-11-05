def my_uniform_random(n, seed=1):
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    random_nums = []

    for _ in range(n):
        x = (a * x + c) % m
        random_nums.append(x / m)
    return random_nums


def f(x):
    return x**2


samples = my_uniform_random(10, seed=42)
f_values = [f(x) for x in samples]
I_estimate = sum(f_values) / len(f_values)

print(
    "Random Samples (x) :\n",
    samples,
    "\nFunction Values f(x) = x^2 :\n",
    f_values,
    f"\nMonte Carlo Estimate of Integral I = {I_estimate:.5f}",
)
