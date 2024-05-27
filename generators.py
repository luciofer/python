
#Generators 

#Generator function
def read_numbers(numbers):
    for number in numbers:
        yield number # Pauses here after yielding the first number


x = [1, 2, 3, 4, 5]

#Creating the generator obejct
#The function body is not executed at this point
gen = read_numbers(x)

for n in gen:
    print(n)

#First Iteration:

#The generator function runs from the beginning up to the first yield statement.
#It yields the first value and then pauses.
# The state of the function (local variables, execution point, etc.) is saved.


# The value 1 is yielded and the function pauses.
# print(n) processes this value by printing 1.

# Second Iteration:

# The generator resumes from where it left off (just after the first yield).
# It continues until it hits the next yield statement.
# It yields the next value and pauses again.

#Subsequent Iterations and complete
#Each iteration resumes the generator function from where it left off, yields the next value, and pauses again.
# After all values have been yielded, the function completes.
# The generator raises a StopIteration exception internally, signaling the end of the iteration.