from numba import jit, cuda
import numpy as np
from timeit import default_timer as timer


def cpufunction(a):
    for i in range(10_000_000):
        a[i] += 1


@jit(nopython=True) # uzywa LLVM
def gpufunction(a):
    for i in range(10_000_000):
        a[i] += 1


if __name__ == '__main__':
    n = 10_000_000
    a = np.ones(n, dtype=np.float64)

    start = timer()
    cpufunction(a)
    print(f"Czas wykonania na CPU: {timer() - start}")

    start = timer()
    gpufunction(a)
    print(f"Czas wykonania na GPU: {timer() - start}")
# Czas wykonania na CPU: 2.3635735000134446
# Czas wykonania na GPU: 0.37068240001099184
