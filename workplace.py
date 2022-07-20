def C_to_F(C):
    F = (C * (9 / 5)) + 32
    return F


def F_to_C(F):
    C = (F - 32) * (5 / 9)
    return C


def CF_Solver(C, F):
    if C == "X":
        C_Result = F_to_C(F)
        print(C_Result)
    if F == "X":
        F_Result = C_to_F(C)
        print(F_Result)


CF_Solver("X", 73)
