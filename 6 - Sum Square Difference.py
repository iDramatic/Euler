
nums = [x for x in range(0,101)]

sums = sum(nums)
sum_squared = sums**2

squares = list(map(lambda x: x**2,nums))
squares_sum = sum(squares)

print(f'sum_squared = {sum_squared}')
print(f'squares_sum = {squares_sum}')

diff = sum_squared-squares_sum
print(f'obj = 25164150')
print(f'diff = {diff}')

