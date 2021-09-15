def avg(list1):
  avg=0
  sum=0
  
  n=0
  for x in list1:
    if x<0:
      continue
    sum=x+sum
    n=n+1
  avg=sum/n
  return avg

def min_max(list1):
  min=list[0]
  max=list[0]
  for x in list1:
    if x<0:
      continue
    if x<min:
      min=x
    if x>max:
      max=x
  return min,max

def absent_students(list1):
  count=0
  for x in list1:
    if x==-1:
      count=count+1
  return count

def max_freq(list1):
  max=0
  max_no=0
  for x in list1:
    count=0
    if x==-1:
      continue
  
    for y in list1:
      if y==-1:
        continue
      if x==y:
        count=count+1
    if count>max:
       max_no=x
       max=count
  return max_no

list=[]
print('Welcome -1 = Absent')
x=int(input('Enter No. of student:'))
for i in range(0,x):
  student=int(input('Enter marks of student ' + str(i+1)+"\n"))
  list.append(student)


print('Average of Present Students: '+ str(avg(list)))
print('Min & Max of all students(Min,Max): '+ str(min_max(list)))
print('No of absent students: ' + str(absent_students(list)))
print('Marks with Max Frequency: '+str(max_freq(list)))
