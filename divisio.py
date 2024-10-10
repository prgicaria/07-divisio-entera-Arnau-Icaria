dividend=int(input("Introdueix el dividend: "))
divisor=int(input("Introdueix el divisor: "))
quoc=int(0)
res=int(0)
while quoc*divisor<=dividend:
    quoc=quoc+1
quoc=quoc-1
res=dividend-(quoc*divisor)
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quoc}")
print(f"Residu: {res}")