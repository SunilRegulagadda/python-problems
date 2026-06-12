weight = int(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
BMI = weight/(height**2)
match BMI:
    case a if a<18.5:
        print("Underweight")
    case a if a>=18.5 and a<=24.9:
        print("Normal")
    case a if a>=25 and a<=29.9:
        print("Overweight")
    case a if a>=30:
        print("Obesity")
    case _:
        print("...")