# Attempt at calculating prime numbers.
primes = [2]

limit = input('Calculate prime numbers up to what number?')


def checkprime(number, primes):
    for prime_number in primes:
        if number % prime_number == 0:
            return False
    return True


for n in range(3, int(limit)):
    if checkprime(n, primes):
        primes.append(n)

print('\n')
print('Primes between 2 and ' + limit + ':\n' + str(primes))
print('Found ' + str(len(primes)) + ' Prime Numbers.')
place = input('Show which place prime number? (Enter a number up to ' + str(len(primes)) + '): ')
print('Prime number No ' + place + ': ' + str(primes[int(place) - 1]))
