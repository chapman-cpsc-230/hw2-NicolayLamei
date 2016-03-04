t = 0
Ttea = 100.0
Tair = 20.0
k = 0.055
while t < 20:
    Ttea -= k * (Ttea - Tair)
    t += 1
    print (t, Ttea)
