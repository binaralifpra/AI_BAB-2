#Exercise 2.5
import math

s = input("Input a list of float numbers (separated by space): ")
numbers = list(map(float, s.split()))

print("Sine values:")
for num in numbers:
    sine_val = math.sin(num)
    print("sin(" + str(num) + ") = " + str(sine_val))
