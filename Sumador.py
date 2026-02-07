

def NOT(a):
    return 1 if a == 0 else 0

def AND(a, b):
    return 1 if a == 1 and b == 1 else 0

def OR(a, b):
    return 1 if a == 1 or b == 1 else 0










def XOR(a, b):
    return OR(AND(a, NOT(b)), AND(NOT(a), b))


def SumadorCompleto (A, B, Cin):
    X1 = XOR(A, B)
    S = XOR(X1, Cin)

    C1 = AND(A, B)
    C2 = AND(Cin, X1)
    Cout = OR(C1, C2)

    return S, Cout

def Sumador4Bits (A, B, MODE):
    # MODE = 0  suma
    # MODE = 1  resta

    result = []
    carry = MODE  # acarreo inicial

    for i in range(4):
        B_mod = XOR(B[i], MODE)  # invierte B si es resta
        s, carry = SumadorCompleto(A[i], B_mod, carry)
        result.append(s)

    return result, carry

A = [1, 0, 1, 0]  # 0101 = 5
B = [1, 1, 0, 0]  # 0011 = 3

resultado, carry = Sumador4Bits(A, B, 0)

print("Suma A + B:", resultado[::-1], "Carry:", carry)

resultado, carry = Sumador4Bits(A, B, 1)

print("Resta A - B:", resultado[::-1], "Carry:", carry)



A = [1, 1, 0, 0]  # 0011 = 3
B = [1, 0, 1, 0]  # 0101 = 5

resultado, carry = Sumador4Bits(A, B, 1)

print("Resta A - B:", resultado[::-1], "Carry:", carry)
