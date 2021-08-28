#===========================
#DSL PYTHON PRACTICAL 1
#===========================

#Alternate Method for Listing students(Currently Disabled)
#A = input('Cricket List')
#B = input('Badminton List')
#C = input('Football List')

global A,B,C,U

#Universal Set
U = [1,2,3,4,5,6,7,8,9,10]

#Cricket Set
A = [2,4,6,8]

#Badminton Set
B = [1,2,3,4]

#Football Set
C = [2,6,8,10]

#Lists for answer a) b) c) d)
a=[]
b=[]
c=[]
d=[]

global count

#Resetting List After Operating on them
def reset():
  global A,B,C,U
  U = [1,2,3,4,5,6,7,8,9,10]
  A = [2,4,6,8]
  B = [1,2,3,4]
  C = [2,6,8,10]
  return True

#A Function to perform intersection of lists
def intersection(list1,list2):
  union_list=[]
  for x in list1:
    count=0
    for y in list2:
      #condition to find common elements
      if x==y:
        count=count+1
    #count is added to avoid duplicates
    if count>0:
      #adding common elements in union_list
      union_list.append(x)
  reset()
  return union_list

#A Function to perform union of lists
def union(list1,list2):
  union_set=list2
  for x in list1:
    count=0
    for y in list2:
      if x!=y:
        count=count+1
    if count==len(list2):
      union_set.append(x)
  reset()
  return union_set

#A Function to perform subtraction of lists
#Note:Common of both sets will be subtracted from first set
def subtract(list1,list2):
  temp=[]
  for x in list1:
    for y in list2:
      if x==y:
        temp.append(y)
  for x in temp:
    list1.remove(x)   
  reset()
  return list1

#A Function to find difference of lists
#Note:Intersection of both sets will be subtracted from Union of both sets
def difference(list1,list2):
  #temp list to store elements to remove
  temp=[]
  l1=list1
  l2=list2
  #finding intersection
  b=intersection(l1,l2)
  #finding union
  a=union(list1,list2)
  for x in a:
    for y in b:
      #condition to find common elements
      if x==y:
        #storing common elements in temp list
        temp.append(y)
  for x in temp:
    #removing common elements from union of 2 list
    a.remove(x)
  reset()
  return a

#printing all data
print("U:"+str(U))
print("A Cricket:"+str(A))
print("B Badminton:"+str(B))
print("C Football:"+str(C))

#newline
print("\n")

#A union B
a=intersection(A,B)
#printing answer
print("Students who play both cricket and badminton: "+str(a))

#newline
print("\n")

#(A union B) - (A intersection B)
b=difference(A,B) 

print("Students who play either Badminton or Cricket: " + str(b))

#newline
print("\n")

#subtracting elements of set A(Cricket) from Universal set storing in c1
c1 = subtract(U,A)
#subtracting elements of set B(Badminton) from c1 set
c = subtract(c1,B)

print("Students who play neither Badminton nor Cricket: " + str(c))      

#newline
print("\n")

# A(Cricket) intersection C(Football) minus B(badminton)
d1=intersection(A,C)
d=subtract(d1,B)
print("Students who play Cricket and Football but not Badminton:"+ str(d))
