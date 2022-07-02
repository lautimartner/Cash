ch = None
while(type(ch) != float or ch<0):
    try:
        ch = float(input("Change owed: "))
    except:
        print("Input not valid")
ch = int(ch*100)
divs = [25,10,5,1]
res = 0
for div in divs:
    aux = ch//div
    if(aux>0):
        res += aux
        ch -= div*aux
print(res)
