"""
Task 3: Build Practical Decorators
===================================

You are building a small toolkit of reusable decorators.

Requirements:
    1. `@timer` — measures and prints execution time of a function.
    2. `@retry(max_attempts, delay)` — retries a function up to `max_attempts`
       times if it raises an exception, waiting `delay` seconds between attempts.
       Must be a decorator factory (takes parameters).
    3. `@cache` — memoizes function results based on arguments.
       If the function is called with the same args again, return cached result
       instead of re-computing.

All decorators must:
    - Preserve the original function's __name__ and __doc__ (use functools.wraps).
    - Work with functions that accept any *args and **kwargs.

Expected output:
    - @timer prints elapsed time
    - @retry retries on failure, eventually succeeds or raises
    - @cache returns cached result on second call (no recomputation)
"""

import functools
import time
import random


# ---------------------------------------------------------------------------
# Decorator 1: @timer
# ---------------------------------------------------------------------------
def timer(func):
    """Measure and print execution time of the decorated function."""
    # TODO: your code here
    pass


# ---------------------------------------------------------------------------
# Decorator 2: @retry(max_attempts, delay)
# ---------------------------------------------------------------------------
def retry(*, max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator factory: retry the function up to `max_attempts` times.
    Wait `delay` seconds between attempts.
    If all attempts fail, re-raise the last exception.
    """
    # TODO: your code here
    pass


# ---------------------------------------------------------------------------
# Decorator 3: @cache
# ---------------------------------------------------------------------------
def cache(func):
    """
    Cache (memoize) function results based on arguments.
    On repeated calls with the same args — return stored result.

    Hint: use a dict to store results, with (args, tuple(kwargs.items())) as key.
    """
    # TODO: your code here
    pass


# ---------------------------------------------------------------------------
# Test functions
# ---------------------------------------------------------------------------

@timer
def slow_sum(a, b):
    """Adds two numbers slowly."""
    time.sleep(0.5)
    return a + b


@retry(max_attempts=5, delay=0.3)
def unreliable_api_call():
    """Simulates an API that fails randomly."""
    if random.random() < 0.7:
        raise ConnectionError("Server unavailable")
    return {"status": "ok", "data": [1, 2, 3]}


@cache
def expensive_computation(n):
    """Simulates a heavy computation."""
    print(f"  Computing for n={n}...")
    time.sleep(0.5)
    return n ** 2 + n + 1


# ---------------------------------------------------------------------------
# Run & verify
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== 1. @timer ===")
    result = slow_sum(10, 20)
    print(f"Result: {result}")
    print(f"Function name preserved: {slow_sum.__name__}")
    print()

    print("=== 2. @retry ===")
    try:
        result = unreliable_api_call()
        print(f"API response: {result}")
    except ConnectionError as e:
        print(f"All attempts failed: {e}")
    print()

    print("=== 3. @cache ===")
    print("First call with n=5:")
    r1 = expensive_computation(5)
    print(f"  Result: {r1}")
    print("Second call with n=5 (should be instant, no 'Computing...' message):")
    r2 = expensive_computation(5)
    print(f"  Result: {r2}")
    print("Call with n=10 (new computation):")
    r3 = expensive_computation(10)
    print(f"  Result: {r3}")

