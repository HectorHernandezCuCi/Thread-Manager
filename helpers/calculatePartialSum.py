import time


def calculate_partial_sum(start, end, results, index, times):
        t0 = time.time()
        results[index] = sum(range(start, end + 1))
        times[index] = time.time() - t0