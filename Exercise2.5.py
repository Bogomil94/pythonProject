p= float(input("Principal = "))
r= float(input( "interest rate = "))
n= float(input( "annual compounding periods = " ))
t= float(input( "number of years = "))
a= p*((1+r/n)**(n*t))
a2= round(a,2)
print( "final amount = ", a2)
percent= ((a-p)/p)*100
percent2= round(percent,2)
print( "percent increase = ", percent2, "%")


