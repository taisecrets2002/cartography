import math
import csv

filename = 'C:/Users/krist/OneDrive/Desktop/faks/kart_v5.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) # 2. create a csvwriter object
    

mylist = ["ime", "vrednost"]

#dane kolicine
a=6377397.15500 #m
b=6356078.96325 #m

fi1 = math.radians(46.125)
delta1 = math.radians(14.5)

fi2 = math.radians(46.25)
delta2= math.radians(14.625)

#dolzine meridianskega loka
e2= (a**2-b**2)/a**2
e_2= (a**2-b**2)/b**2

A= 1+((3/4)*e2)+((45/64)*e2**2)+ ((175/256)*e2**3)+ ((11025/16384)*e2**4)
B= ((3/4)*e2)+((15/16)*e2**2)+((525/512)*e2**3)+((2205/2048)*e2**4)
C= ((15/64)*e2**2)+((105/265)*e2**3)+((2205/4096)*e2**4)
D= ((35/512)*e2**3)+((315/2048)*e2**4)

L1= a*(1-e2)*(A*fi1 - (B/2)*math.sin(fi1*2) + (C/4)*math.sin(4*fi1) - (D/6)*math.sin(6*fi1))
L2= a*(1-e2)*(A*fi2 - (B/2)*math.sin(fi2*2) + (C/4)*math.sin(4*fi2) - (D/6)*math.sin(6*fi2))

mylist= mylist + ["e^2", e2]+ ["e'^2", e_2]+ ['A', A]+ ['b', B]+ ['C', C]+ ['D', D]+ ['L1', L1]+ ['L2', L2]

#oddaljenost od srednjega meridiana

l1 = delta1 - math.radians(15)
l2 = delta2 - math.radians(15)

mylist = mylist + ['l1', l1] +['l2', l2]

#pomozne kolicine
N1 = a/math.sqrt(1-e2*math.sin(fi1)**2)
N2 = a/math.sqrt(1-e2*math.sin(fi2)**2)

t1 = math.tan(fi1)
t2 = math.tan(fi2)

ni1 = math.sqrt(e_2)*math.cos(fi1)
ni2 = math.sqrt(e_2)*math.cos(fi2)

mylist= mylist + ['N1', N1]+ ['N2', N2]+ ['t1', t1]+ ['t2', t2]+ ['ni1', ni1]+ ['ni2', ni2]

#nemodelirane koordinate

x_1= L1 + (1/2)*l1**2*N1*math.sin(fi1)*math.cos(fi1) + (1/24)*l1**4*N1*math.sin(fi1)*math.cos(fi1)**3*(5-t1**2-9*ni1**2+4*ni1**4) + (1/720)*l1**6*N1*math.cos(fi1)**5*(61-58*t1**2+t1**4)
x_2= L1 + (1/2)*l2**2*N1*math.sin(fi1)*math.cos(fi1) + (1/24)*l2**4*N1*math.sin(fi1)*math.cos(fi1)**3*(5-t1**2-9*ni1**2+4*ni1**4) + (1/720)*l2**6*N1*math.cos(fi1)**5*(61-58*t1**2+t1**4)
x_3= L2 + (1/2)*l1**2*N2*math.sin(fi2)*math.cos(fi2) + (1/24)*l1**4*N2*math.sin(fi2)*math.cos(fi2)**3*(5-t2**2-9*ni2**2+4*ni2**4) + (1/720)*l1**6*N2*math.cos(fi2)**5*(61-58*t2**2+t2**4)
x_4= L2 + (1/2)*l2**2*N2*math.sin(fi2)*math.cos(fi2) + (1/24)*l2**4*N2*math.sin(fi2)*math.cos(fi2)**3*(5-t2**2-9*ni2**2+4*ni2**4) + (1/720)*l2**6*N2*math.cos(fi2)**5*(61-58*t2**2+t2**4)

y_1 = l1*N1*math.cos(fi1) + (1/6)*l1**3*N1*math.cos(fi1)**3*(1+ni1**2-t1**2) + (1/120)*l1**5*N1*math.cos(fi1)**5*(5-18*t1**2+t1*4+14*ni1**2-58*ni1**2*t1**2)
y_2 = l2*N1*math.cos(fi1) + (1/6)*l2**3*N1*math.cos(fi1)**3*(1+ni1**2-t1**2) + (1/120)*l2**5*N1*math.cos(fi1)**5*(5-18*t1**2+t1**4+14*ni1**2-58*ni1**2*t1**2)
y_3 = l1*N2*math.cos(fi2) + (1/6)*l1**3*N2*math.cos(fi2)**3*(1+ni2**2-t2**2) + (1/120)*l1**5*N2*math.cos(fi2)**5*(5-18*t2**2+t2**4+14*ni2**2-58*ni2**2*t2**2)
y_4 = l2*N2*math.cos(fi2) + (1/6)*l2**3*N2*math.cos(fi2)**3*(1+ni2**2-t2**2) + (1/120)*l2**5*N2*math.cos(fi2)**5*(5-18*t2**2+t2**4+14*ni2**2-58*ni2**2*t2**2)

mylist = mylist + ['x_1', x_1]+ ['x_2', x_2]+ ['x_3', x_3]+ ['x_4', x_4]+ ['y_1', y_1]+ ['y_2', y_2]+ ['y_3', y_3]+ ['y_4', y_4]

#modulacija

x1 = x_1*0.9999 -5000000
x2 = x_2*0.9999 -5000000
x3 = x_3*0.9999 -5000000
x4 = x_4*0.9999 -5000000

y1 = y_1*0.9999 + 500000
y2 = y_2*0.9999 + 500000
y3 = y_3*0.9999 + 500000
y4 = y_4*0.9999 + 500000

mylist.extend(['x1', x1]+ ['x2', x2]+ ['x3', x3]+ ['x4', x4]+ ['y1', y1]+ ['y2', y2]+ ['y3', y3]+ ['y4', y4])

#meridianska konvergenca

fisr = (fi1+fi2)/2
deltasr = (fi1+fi2)/2

l=deltasr - math.radians(15)
ni = e_2*math.cos(fisr)
t=math.tan(fisr)

gamma= l*math.sin(fisr)+ (1/3)*l**3*math.sin(fisr)*math.cos(fisr)**2*(1+3*ni**2)+(1/15)*l**5*math.sin(fisr)*math.cos(fisr)**4*(2-t**2)

mylist.extend(['sredinski fi', fisr] + ['srednji delta', deltasr] + ['l srednji', l] + ['ni sredinski', ni] + ['t srednji', t] + ['konvergenca', gamma])


#dolzine stranic v naravi

d1 = math.sqrt((x2-x1)**2+(y2-y1)**2)
d2 = math.sqrt((x3-x2)**2+(y3-y2)**2)
d3 = math.sqrt((x4-x3)**2+(y4-y3)**2)
d4 = math.sqrt((x1-x4)**2+(y1-y4)**2)

mylist.extend(['d1 v naravi', d1]+ ['d2 v naravi', d2]+ ['d3 v naravi', d3]+ ['d4 v naravi', d4])

#dolzine stranic v merilu

d_1 = d1/250 
d_2 = d2/250 
d_3 = d3/250 
d_4 = d4/250 

mylist.extend (['d1 v merilu', d_1] + ['d2 v merilu', d_2] + ['d3 v merilu', d_3] + ['d4 v merilu', d_4])

print('im before the iteration')

#iteration

fi_1 = 2*x_1/(a+b)
L_1 = a*(1-e2)*(A*fi_1 - B/2*math.sin(2*fi_1)) + C/4*math.sin(4*fi_1) - D/6*math.sin(6*fi_1)
d_1 = x_1-L_1

while (abs(d_1)< 0.001):
    fi_1 += 2*d_1/(a+b)
    L_1 = a*(1-e2)*(A*fi_1 - B/2*math.sin(2*fi_1)) + C/4*math.sin(4*fi_1) - D/6*math.sin(6*fi_1)
    d_1 = x_1 - L_1

#pomozne kolicine

n_1 = a/math.sqrt(1-e2*math.sin(fi_1)**2)
t_1 = math.tan(fi_1)
ni_1 = math.sqrt(e_2)* math.cos(fi_1)


fi_z = fi_1 - t_1*(1+ni_1**2)*y_1**2/(2*n_1**2) + t_1*(5 + 3*t_1**2 + 6*ni_1**2 -6*ni_1**2*t_1**2)*y_1**4/(24*n_1**4) - t_1*(61 + 90*t_1**2 + 45* t_1**4)*y_1**6/(720*n_1**6)
l_1 = y_1/(n_1*math.cos(fi_1)) - (1+2*t_1**2 + ni_1**2)*y_1**3/(6*n_1**3*math.cos(fi_1)) + (5 + 28*t_1**2 + 24*t_1**4)* y_1**5/(120*n_1**5*math.cos(fi_1))
del_1 = 15 + math.degrees(l_1)
phi_1 = math.degrees(fi_z)

mylist.extend(['fi reiteriran', phi_1] + ['delta reiterirana', del_1])


#write to csv

with open(filename, 'w') as f:
    write = csv.writer(f)
    write.writerow(mylist)
    
