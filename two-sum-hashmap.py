#----------------------------------------
#  Implementation: two-sum hashmap
#  Reference: https://www.youtube.com/watch?v=KLlXCFG5TnA&t=486s
#----------------------------------------
def twosum(nums,sum):
    hashmap = dict()
    for index, num in enumerate(nums):
        diff = sum - num
        if diff in hashmap:
            print("Index pair:",hashmap[diff], index)
        else:
            hashmap[num] = index


#----------------------------------------
#  Example: random numbers / random sum
#----------------------------------------
import random

length = 10
maximal_value = 10

random_nums = random.sample(range(maximal_value),k=length)
random_sum  = random.randrange(maximal_value)


#----------------------------------------
#  Application: two-sum => example
#----------------------------------------
print("Numbers:",random_nums,"Sum:",random_sum)
twosum(random_nums,random_sum)