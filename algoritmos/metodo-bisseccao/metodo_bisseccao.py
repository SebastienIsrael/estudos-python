def square_root_bisection(number, maximum=0.1, max_iterations=10):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 1 or number == 0:
        print(f"The square root of {number} is {number}")
        return number
    
    low = 0
    high = 1 if number < 1 else number
    # while i in range(max_iterations):
    for _ in range(max_iterations):

        # if high < 1:
        #     high = 1
        
        
        mid = (low+ high)/ 2
        if mid == number**0.5:
            print(f"The square root of {number} is approximately {mid}")
            return mid
            
            
        elif mid > number**0.5:
   
            high = mid
        else:
            low = mid

        if abs(mid - number**0.5) < maximum:
            print(f'The square root of {number} is approximately {mid}')
            return mid
    
    print(f"Failed to converge within {max_iterations} iterations")
    return None

list_number = (1,25, 64, 81, 144)
# for n in list_number:
#     print(square_root_bisection(n))

n = 25

print(square_root_bisection(n))
print(square_root_bisection(0.001, 1e-7, 500))
print(square_root_bisection(0.25, 1e-7, 50))
print(square_root_bisection(81, 1e-3, 50))
print(square_root_bisection(225, 1e-3, 100))
print(square_root_bisection(225, 1e-7, 100))
print(square_root_bisection(225, 1e-7, 10))