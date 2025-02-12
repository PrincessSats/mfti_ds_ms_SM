from sympy import *
a,b,w=symbols(' a b w' )
g = 3*a**2 + a + 4*b + 5*b**2
print('Целевая функция для аргументов a и b :\n f = ', g)
q = a + b - 200
print('Функция ограничений: ', q,'= 0')
f = 3*a**2 + a + 4*b + 5*b**2 + w*(a + b - 200)
print('Функция Лагранжа :\n ',f)
fa = f.diff(a)
print('df/da =',fa,'= 0')
fb = f.diff(b)
print('df/db =',fb,'= 0')
fw = f.diff(w)
print('df/dw =',fw,'= 0')
sols = solve([fa,fb,fw],a,b,w)
print('Стационарная точка M(x,y):\n',float(sols[a]),',',float(sols[b]))

#Целевая функция для аргументов a и b :
#f =  3*a**2 + a + 5*b**2 + 4*b
#Функция ограничений:  a + b - 200 = 0
#Функция Лагранжа :
#3*a**2 + a + 5*b**2 + 4*b + w*(a + b - 200)
#df/da = 6*a + w + 1 = 0
#df/db = 10*b + w + 4 = 0
#df/dw = a + b - 200 = 0
#Стационарная точка M(x,y):
#125.1875 , 74.8125