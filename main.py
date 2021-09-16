# Bhaskara's formula in Python (without "Math" library)

# Main function
def main():
    print("")

    # Functions call
    readme()
    a, b, c = def_nums()
    delta = calc_delta(a, b, c)
    a1, a2 = calc_answers(a, b, c, delta)

    # Test the type of each number, to print in a "better" way to user
    if(type(delta) == float):
        print(">> Δ = %.2f"%delta)
    else:
        print(f">> Δ = {delta}")
    if(type(a1) == float and type(a2) == float):
        print(">> X¹ = %.2f"%a1)
        print(">> X² = %.2f"%a2)
    else:
        print(f">> X¹ = {a1}")
        print(f">> X² = {a2}")

# Code title
def readme():
    print(">> BHASKARA RESOLVE CODE <<")

# Read A, B and C (Input example:(>>A [SPACE] B [SPACE] C))
def def_nums():
    abc = input(">> ")
    abc_list = abc.split(" ")
    a = float(abc_list[0])
    b = float(abc_list[1])
    c = float(abc_list[2])

    # Try to transform a, b and c in "int"
    a = int(a) if a == int(a) else a
    b = int(b) if b == int(b) else b
    c = int(c) if c == int(c) else c

    return(a, b, c)

# Calculate delta(Δ)
def calc_delta(a, b, c):
    delta = (b**2)-(4*a*c)

    # Try to transform delta in "int"
    delta = int(delta) if delta == int(delta) else delta

    return(delta) 

# Calculate the two possible answers
def calc_answers(a, b, c, delta):
    if(delta<0):
        # Verify if delta(Δ) is negative
        a1 = (f"-{b} + ²√{delta} / {2*a}")
        a2 = (f"-{b} - ²√{delta} / {2*a}")
    else:
        # Normal calculate
        a1 = (-b + delta**0.5)/(2*a)
        a2 = (-b - delta**0.5)/(2*a)
        
    return(a1, a2)

main()
