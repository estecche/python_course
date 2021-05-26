"""
These are examples about lists.
"""
temperatures = [10, 25, -1, 0, 5];
print("The size of the temperatures list is = ", len(temperatures))
for temperature in temperatures:
    print("Temperature = ", temperature)

print("The first temperature is = ", temperatures[0])
print("The last temperature is = ", temperatures[len(temperatures) - 1]);

temperatures_two_dimension = [
    [10, 20, 30],
    [-5, -6, -9]
]
print("The 0,0 element is = ", temperatures_two_dimension[0][0])
print("The 1,2 element is = ", temperatures_two_dimension[1][2])

# splat operator
print(*temperatures)

# save each array in variables
t0, t1 = temperatures_two_dimension
print("This is the 0 element of the matrix = ", t0)
print("This is the 1 element of the matrix = ", t1)