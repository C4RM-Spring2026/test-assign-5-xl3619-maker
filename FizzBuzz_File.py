import numpy as np

def FizzBuzz(a, b):
    x = np.arange(a, b + 1)
    out = x.astype(object)

    m3 = (x % 3 == 0)
    m5 = (x % 5 == 0)

    out[m3] = "fizz"
    out[m5] = "buzz"
    out[m3 & m5] = "fizzbuzz"

    return out.tolist()
