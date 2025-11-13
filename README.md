# project-7a

[Recursion is not required for 7a.]

Write a function named **list_of_primes_up_to** that takes one integer argument - the limit - and returns a list of all primes up to and including the limit. The parameter should have a **default argument** of 100.

The function should do the following:

1. **Initialize a list of booleans:**
   - Create a list of `limit + 1` elements.
   - Set the elements at indices 0 and 1 to `False` (since 0 and 1 are not prime).
   - Set all other elements to `True`.
   - You can use a list like `[True] * (limit + 1)` and then set the first two elements to `False`.

2. **Eliminate multiples of 2:**
   - Set all elements with an index greater than 2 that is evenly divisible by 2 to `False`, since we know that any number divisible by 2 is not prime.

3. **Sieve using successive divisors:**
   - Find the next index greater than 2 that is still `True` (this will be 3), and use it as the next divisor.
   - Set all elements with an index greater than the divisor and evenly divisible by it to `False`.
   - Repeat this step for each successive `True` index, continuing as long as the current divisor is less than or equal to the square root of the limit.
     - You can take the square root by raising to the power of 1/2, e.g. `limit ** 0.5`.
     - We can stop at that point because we'll have already found factors for any non-prime numbers up to, and including, the limit. If a number has any factors larger than its square root, then it also has factors smaller than its square root. For example, if the limit is 99, after passing its square root we don't need to keep going to 33 because we'll have already found its corresponding factor, which is 3.

4. **Extract the primes:**
   - Use a list comprehension to collect all indices that are still marked `True`. These are the prime numbers.

5. **Return the list of all primes up to and including the limit.**

For example, your function could be used like this:

`result = list_of_primes_up_to(1000)`

The file must be named: list_of_primes_up_to.py
