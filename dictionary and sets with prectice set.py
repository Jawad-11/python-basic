mydict = {"name": "jawad", 
          "reg_no": 19-88-45  ,
          "another dictionary" : {'jaawad': 'player'},
          "friend no ": [1,4,5,3]   ,
           1:2  }
#print(mydict['name'])           
#print(mydict['reg_no'])           
#print(mydict['balance'])    
 #dictionary in mutable(we can change)
# mydict['name'] = "saad"
# print(mydict['name'])
# print(mydict['another dictionary']['jaawad'])      
   #dic method
print(mydict.keys()) #>for printing only keys in dectionary 
#we can also comvert this into list(keys) by
print(list(mydict.keys()))
print(mydict.values())
print(mydict.items())  #otput in form of taple  -->print keys and values of all content of mydic
updatedict = {"new update": "add new in doct"}
mydict.update(updatedict) #add new or update any value of existing
print(mydict)
#.get method
print(mydict.get('jawad2')) # it will not throw error and give none tha why we use .get for this
#[] you are reposnisble for out in these brackets because this throw error and stop program in case of erroe but
# in () we get none and programs will be in running form in this case
                              #sets 
#there is no repetative elements in sets
# a = {1,4,2,5,1}
# print(type(a))
# print(a)
# a ={}if we want a empty set than it will not show empty set but it show a empty dictionary 
# b=set()
# b.add(5)
# print(b()
#we cannot add lists in sets list and ALSO WE CANNOT ADD list in set 
#sets are unordered or unindexed
     #methods
#sets are unrepeitative
# b.add((2,6,7))
# print(b)
# b.remove(2)

# # print(b.pop())
# b.remove(5) #remove 5 from set
# print(b)
# b.clear()
# print(b)
# b.intersection({8,12})
# print(b)
                        #practice Set
                  #1>>>
# diction =  {"okay": "hala" , "sir": "jnab"} 
# print(" options are as ::>" , diction)
# l = input("Enter the input word:")
# print("result will be" , diction.get(l))  #>get will give us none value 

                 #2>>
fevlang = {}
a = input("enter the value of jawad")
b = input("enter value of atta")
fevlang['jawad'] =a
fevlang['atta']=b 
print(fevlang)