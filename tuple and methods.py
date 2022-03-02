# create tuple ()
#we can not change (immutable)
taple = (2 ,8 ,9,5, 3,2)
print(taple)
#For taple we have to put , if you have  only one element
#           ..Taple mehod
taple.count(2)
print(taple.count(2))  #> for counting the no of 2
print(taple.index(2))  # > for finding index of 2
     #practice list and taple
     #1>>
a = input(" enter the first fruit ::")
b = input(" enter the first fruit2::")
c = input(" enter the first fruit2::")
d = input(" enter the first fruit3::")
e = input(" enter the first fruit4::")
f = input(" enter the first fruit5::")
g = input(" enter the first fruit6::")
lista = [a , b ,c ,d ,e,f,g ]  
print(lista)
in list there is no issue that values are repeating
    #>>2wrie a program to list 6 students marks in ascending order from input
a = input(" enter the first fruit ::")
b = input(" enter the first fruit2::")
c = input(" enter the first fruit2::")
d = input(" enter the first fruit3::")
e = input(" enter the first fruit4::")
f = input(" enter the first fruit5::")
g = input(" enter the first fruit6::")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)

lista = [a , b ,c ,d ,e,f,g ]
lista.sort()
print(lista)
 #>>3 # write program to add 4 integers in a list
a = [1 ,12,3,4]
print(a[0]+a[1]+a[2]+a[3])
  #>>4 write program to count no of zeroes
zeroes = [2,4,53,0 , 0 ,0]
print(zeroes.count(0))

      


