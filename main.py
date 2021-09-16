# Bhaskara's formula in Python (without "Math" library)

# Main function
def main():
    print("")
    readme()
    a, b, c = def_nums()
    delta = calc_delta(a, b, c)
    a1, a2 = calc_answers(a, b, c, delta)
    print(f">> Δ = {delta}")
    print(f">> X¹ = {a1}")
    print(f">> X² = {a2}")
    print("")

# Code title
def readme():
    print(">> BHASKARA RESOLVE CODE <<")

# Read A, B and C
def def_nums():
    a = float(input(">> A = "))
    b = float(input(">> B = "))
    c = float(input(">> C = "))

    # Transform a, b and c in "int"
    a = int(a) if a == int(a) else a
    b = int(b) if b == int(b) else b
    c = int(c) if c == int(c) else c

    return(a, b, c)

# Calculate delta(Δ)
def calc_delta(a, b, c):
    delta = (b**2)-(4*a*c)

    # Transform delta in "int"
    delta = int(delta) if delta == int(delta) else delta

    return(delta) 

# Calculate the two possible answers
def calc_answers(a, b, c, delta):
    if(delta<0):
        # Verify if delta(Δ) is negative
        a1 = (f"-{b} + ²√{delta} / {2*a}")
        a2 = (f"-{b} - ²√{delta} / {2*a}")
    else:
        a1 = (-b + delta**0.5)/(2*a)
        a2 = (-b - delta**0.5)/(2*a)
        
    return(a1, a2)

main()