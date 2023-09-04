import math

def can_represent(n, p, q, depth):
    moduli = []

    # Generate a list of moduli that are co-prime to both p and q
    m = 2
    while len(moduli) < 5:
        if math.gcd(m, p) == 1 and math.gcd(m, q) == 1:
            moduli.append(m)
        m += 1

    def dfs(remaining, p_power, q_power, terms):
        if abs(remaining) > (p ** depth) and abs(remaining) > (q ** depth):
            return False, []
        if p_power + q_power > depth:
            return False, []
        if remaining == 0:
            return True, terms

        for coef in [-1, 0, 1]:
            success, new_terms = dfs(remaining - coef * (p ** p_power), p_power + 1, q_power, terms + [(coef, p, p_power)])
            if success:
                return True, new_terms
            success, new_terms = dfs(remaining - coef * (q ** q_power), p_power, q_power + 1, terms + [(coef, q, q_power)])
            if success:
                return True, new_terms

        return False, []

    success, terms = dfs(n, 0, 0, [])
    return success, terms, moduli

# Get user input
p = int(input("Enter value for p: "))
q = int(input("Enter value for q: "))
n = int(input("Enter the integer to be represented: "))

depth = 1
while True:
    print(f"Checking depth: {depth}")
    success, terms, moduli_used = can_represent(n, p, q, depth)
    if success:
        representation = " + ".join([f"{coef} * {base}^{power}" for coef, base, power in terms if coef != 0])
        print(f"{n} can be represented as: {representation} (using moduli {', '.join(map(str, moduli_used))})")
        break
    depth += 1
