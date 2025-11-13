# project-5a

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 11/12/2025
#Description: This program returns all of the prime numbers. Prime numbers are
            #is a number greater than 1 that can be divided evenly by 1 and itself.
            #For example 2,3,5,7

def list_of_primes_up_to(limit=100):
    """
    Return a list of all prime numbers up to the given limit. Using the "Sieve of Eratosthenes"
    function. By assuming all the numbers are prime and then marking false the numbers that aren't prime
    """

    # Create a list of true values for all numbers from 0 to limit
    prime = [True] * (limit + 1)

    # 0 and 1 are not prime , so we mark them false right away
    prime[0] = False
    prime[1] = False

    #Step-2
    #Eliminate all even numbers greater than 2(they cant be prime)
    #stating at 4 and go up to limit, skipping by 2
    for number in range(4, limit+1, 2):
        prime[number] = False

    #Step-3
    #Loop to find the next prime number by checking numbers up to the sq-root
    divisor = 3
    while divisor <= limit ** 0.5:

        #if the number is still marked as true, its prime
        if prime[divisor]:
            #start from divisor * divisor

            for multiple in range(divisor, limit + 1, divisor):
                prime[multiple] = False
        #Move on to next odd number
        divisor += 2

    #Step-4
    #Build a list of numbers that are still marked True(prime)
    prime_numbers = []
    for i in range(len(prime)):
        if prime[i]:
            prime_numbers.append(i)

    #return final list of prime numbers
    return prime_numbers

#Example Test Run
if __name__ == '__main__':
    result = list_of_primes_up_to(1000)
    print("prime number up to 100 are:")
    print(result)