import sympy as sp

with open(r"day 13\input.txt", "r") as file:
    data = file.read()
    data = [x.split("\n") for x in data.split("\n\n")]
    # print(data)
    
    def solve_linear_2(a1, b1, c1, a2, b2, c2):
        a, b = sp.symbols('a, b')
        eq1 = sp.Eq(a1* a + b1 * b, c1)
        eq2 = sp.Eq(a2* a + b2 * b, c2)
        ans = sp.solve((eq1, eq2), (a,b))
        return ans
    tokens = 0 
    for machine in data:
        
        A = (machine[0][machine[0].find("+")+1:machine[0].find("+")+3], machine[0][machine[0].find(",")+4:]) # (x,y)
        B = (machine[1][machine[1].find("+")+1:machine[1].find("+")+3], machine[1][machine[1].find(",")+4:])
        prize = (machine[2][machine[2].find("=")+1:machine[2].find(",")], machine[2][machine[2].find(",")+4:])
        
        apress = 0
        bpress = 0 
        
        eq = [int(x) for x in (A[0], B[0], int(prize[0])+10000000000000, A[1], B[1], int(prize[1])+10000000000000)]
        ans = solve_linear_2(*eq)
        a, b = sp.symbols('a, b')
        
        if ans[a]%1 == 0 and ans[b]%1 == 0:
            tokens+= ans[a] * 3
            tokens+= ans[b]
            
    print(tokens)