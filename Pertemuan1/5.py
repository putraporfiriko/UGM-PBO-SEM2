r = float(input("Enter the radius of the circle: "))

area = 3.14 * r * r
circumference = 2 * 3.14 * r

# bonus: if result is round, truncate decimal
if area.is_integer():
    area = int(area)
if circumference.is_integer():
    circumference = int(circumference)

print(f"Area: {area}")
print(f"Circumference: {circumference}")
