import numpy as np
from numba import cuda
from timeit import default_timer as timer

@cuda.jit
def gpufunction(a):
    i = cuda.grid(1)
    if i < a.size:
        a[i] += 1

n = 10_000_000
a = np.ones(n, dtype=np.float32)

# kopiujemy na GPU
a_gpu = cuda.to_device(a)

threads_per_block = 256
blocks_per_grid = (n + threads_per_block - 1) // threads_per_block

start = timer()
gpufunction[blocks_per_grid, threads_per_block](a_gpu)
cuda.synchronize()
print("GPU time:", timer() - start)

# kopiujemy wynik z powrotem
a = a_gpu.copy_to_host()
