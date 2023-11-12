import math
import csv

fi= [0, 2, 12, 22, 32, 42, 52, 62, 72, 82, 90]
a=6378137
b=6356752.3

mylist=[['fi','n', 'p', 'm', '1fi', '1delta']]

e2= (a**2-b**2)/a**2

for item in fi:
    n=a/((1-e2*(math.sin(math.radians(item)))**2)**(1/2))
    p= n*math.cos(math.radians(item))
    m=(a*(1-e2))/(1-e2*math.sin(math.radians(item))**2)**(3/2)
    fi1= 2*math.pi*m/(360*60*60)
    delta1 = 2*math.pi*p/(360*60*60)
    
    mylist.append([item, n, p, m, fi1, delta1])

with open('C:/Users/krist/OneDrive/Desktop/faks/kart.csv', 'w') as f:
    write = csv.writer(f)
    write.writerows(mylist)

#drugi del naloge

fia = 46.03738
fib = 46.06510417
fic = 46.05131694

deltaa=14.52611861
deltab = 14.53471694
deltac= 14.57088889 

fisr = (fia+fib+fic)/3
deltasr = (deltaa + deltab+ deltac)/3


Nsr= a/((1-e2*(math.sin(math.radians(fisr)))**2)**(1/2))
psr = Nsr*math.cos(math.radians(fisr))
msr=(a*(1-e2))/(1-e2*math.sin(math.radians(fisr))**2)**(3/2)
kfi= 2* math.pi*msr/(360)
kdelta = 2* math.pi*psr/(360)


#spremembe koordinat v stopinje
fiab= math.degrees(fia-fib)
fibc = math.degrees(fic-fib)
deltaab= math.degrees(deltaa-deltab)
deltabc = math.degrees(deltac - deltab)



#spremembe koordinat v metrih
fab = fiab*kfi
fbc = fibc*kfi
deab = deltaab*kdelta
debc = deltabc *kdelta

dab = math.sqrt(fab**2+deab**2)
dbc = math.sqrt(fbc**2+debc**2)

nuab = math.degrees(math.atan(deab/fab)) + 180
nubc = math.degrees(math.atan(debc/fbc)) + 180

beta = nuab - nubc

print(fiab)
print(fibc)
print(deltaab)
print(deltabc)
print(fisr)
print(deltasr)
print(Nsr)
print(psr)
print(msr)
print(kfi)
print(kdelta)
print(fab)
print(fbc)
print(deab)
print(debc)
print(dab)
print(dbc)
print(nuab)
print(nubc)
print(beta)
