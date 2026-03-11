length=float(input("Enter length: "))
width=float(input("Enter width: "))

area=length*width
perimeter=2*(length+width)

print(f"Area:{area}")
print(f"Perimeter:{perimeter}")

if area>100:
    print("Large area")