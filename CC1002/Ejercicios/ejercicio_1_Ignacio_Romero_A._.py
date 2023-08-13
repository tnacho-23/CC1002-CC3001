#se tiene un triángulo de lados a, b y c
a=5
b=12
c=13
#resolución de la ecuación ax^2+bx+c=0 de raices r1 y r2
r1=(1/2*a)*(-b+(b**2-4*a*c))
r2=(1/2*a)*(-b-(b**2-4*a*c))
#s=semiperímetro del triángulo abc
s=(1/2)*(a+b+c)
#at=cálculo del área del triángulo usando el semiperímetro
at=(s*(s-a)*(s-b)*(s-c))**(1/2)

