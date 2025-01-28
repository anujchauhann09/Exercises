from utils.primes.sequential import count_primes_sequential
from utils.primes.parallel import count_primes_parallel

if __name__ == "__main__":
    limit = 10**7 

    # prime_count_seq, time_seq = count_primes_sequential(limit)
    # print(f"Sequential: Found {prime_count_seq} primes in {time_seq:.2f} seconds")

    prime_count_par, time_par = count_primes_parallel(limit)
    print(f"Parallel: Found {prime_count_par} primes in {time_par:.2f} seconds")