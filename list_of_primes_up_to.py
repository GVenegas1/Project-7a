# project-7a

# Author: Gabriel Venegas
# GitHub username: GVenegas1
# Date: 11/12/2025
#Description: This program returns all prime numbers. Prime numbers are
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
    #Sieve process, go thru all the numbers starting from 2 up to the square root of the limit
    for devisor in range(2,int(limit**0.5)+1):
        #if the number is still marked as prime
        #mark all multiples of this number as not prime
        if prime[devisor]:
            for multiple in range(devisor*devisor, limit + 1, devisor):
                prime[multiple] = False

    #Step-3
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