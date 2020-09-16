#exercise according to video of codebasics
e=[2200, 2350, 2600, 2130, 2190]
print(e[1]-e[0]," dollors spent more in feb compare to jan.")
print(e[0]+e[1]+e[2], " total spent of first three months.")
#for i in range(len(e)):
    #if e[i] == 2000:
        #print(e[i])

print("did i spent exactly 2000$?", 2000 in e)
e.append(1980)
print(e)
e[3]-=200
print(e)