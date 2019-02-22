
def is_prime(num):
    '''
    RETURNS A LIST OF ALL PRIME NUMBER FROM 0 TO X
    '''
    primes = [2]
    x = 3
    count = 1
    #for count in range(num):
    while len(primes)<= (num-1):
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x +=2
        count+=1
    return primes


x=10001
print(f'The {x}º prime is {max(is_prime(x))}')
