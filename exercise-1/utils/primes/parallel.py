import time
from ..math_utils import isPrime
from multiprocessing import Pool, cpu_count

def count_primes_in_segment(start, end):
    count = 0
    for num in range(start, end + 1):
        if isPrime(num):
            count += 1
            
    return count

def count_primes_parallel(limit, num_processes=None):
    if num_processes is None:
        num_processes = cpu_count()

    segment_size = limit // num_processes
    segments = [(i * segment_size + 1, (i + 1) * segment_size) for i in range(num_processes)]
    segments[-1] = (segments[-1][0], limit) 

    start_time = time.time()
    with Pool(processes=num_processes) as pool:
        results = pool.starmap(count_primes_in_segment, segments)
    end_time = time.time()

    prime_count = sum(results)
    return prime_count, end_time - start_time