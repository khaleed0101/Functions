# optional vs reguired parameter
# ALL PARAMETERA ARE REQUIRED
def add_it(a,b,c,d,e):
    return a + b + c + d + e

ans = add_it(3, 5, 6, 8, 2)
print (ans)
# F AND G ARE REQUIRED PAPRAMETERS
# H is an optional parameter
# required parameters fisrt then optional parameter
def mult_it(f,g,h=3):
    return f * g * h

ans2 = mult_it(2,6)

print(ans2)
ans3 = mult_it(2,4,5)           # 5 will override the optional parameter

print (ans3)