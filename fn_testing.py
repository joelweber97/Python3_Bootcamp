
def multiply_even_numbers(nums):
    product = 0
    for i in nums:
        if i % 2 == 0:
            product = product * i
       return product
        
print(multiply_even_numbers([1,2,4])