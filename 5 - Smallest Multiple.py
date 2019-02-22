'''
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

nums = [x for x in range(20,0,-1)]
num = 0
while True:
    num += 1
    #print(num)
    for x in nums:
        if num % x == 0:
            if x == 1:
                print(num)
                exit()

        else:
 #           print('else')
            break

 #       print(num)
 #   print('while')


