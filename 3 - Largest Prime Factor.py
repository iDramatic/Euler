'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def is_prime(num):
    '''
    RETURNS A LIST OF ALL PRIME NUMBER FROM 0 TO X
    '''
    primes = [2]
    x = 3
    while x <= num:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x +=2
    return primes


primes = [r for r in is_prime(30)]
print(primes)

num = 20
#600851475143
resto = 1
mult = 1
fat=[]
while resto <= num:
    for c in primes:
        if num%c == num//c:
            print(c)
        resto *= c

    print('while')



print(resto)
print(fat)


