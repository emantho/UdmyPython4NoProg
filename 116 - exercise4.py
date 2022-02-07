# Circle Area

from cmath import pi
import math

r = float(input("Enter r to calculate area and longitud of one circle: "))

area = math.pi * r**2
longitude = 2 * math.pi * r

print(f"Whit that radio your cicle has an area: {area:.3f} and longitude: {longitude:.2f}")
# {:.3f} are used to limit the decimal numbers in the result

