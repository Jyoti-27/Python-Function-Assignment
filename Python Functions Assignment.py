#!/usr/bin/env python
# coding: utf-8

# - Q.1 Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters. 

# In[20]:


# Method 1

def count_upper_lower(string):
    count_upper = 0
    count_lower = 0
    for char in string:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper +=1
        else:    # added an extra case for the rest of the chars that aren't lower non upper
            pass
    return(count_upper, count_lower)
print(count_upper_lower("Hello I am Jyoti and I would like to become a Successful Data Scientist"))


# In[30]:


# Method 2

def upperlower(string):
    u=0
    l=0
    for i in string:
        if i.isupper():
            u=u+1
        elif i.islower():
            l=l+1
    print("Upper case letters are :",u)
    print("Lower case letters are :",l)
upperlower("Hello I am Jyoti and I would like to become a Successful Data Scientist")


# - Q.2 Write a Python function to create and print a list where the values are squares of numbers between 1 and 30 (both               included).

# In[47]:


# Method 1

def print_Square_Values():
    l = list()
    for i in range(1,31):
        l.append(i**2)
    print(l)
print_Square_Values()


# In[ ]:


# Method 2

def squarelist(): 
    l=[] 
    for i in range(1,31): 
        l.append(i*i) 
    return l 
l=[] 
l=squarelist() 
print(l) 


# In[45]:


# Method 3

sq_Values = lambda a,b: [i * i for i in range(a,b+1)]

print (sq_Values(1,30))


# In[11]:


# Method 4

def sq(n): 
    list1=[] 
    for i in range(n+1): 
        a=i*i 
        list1.append(a) 
    print(list1)
sq(30)


# - Q.3 Create a function that counts the number of elements within a list that are greater than 30. 

# In[54]:


# Method 1

# initializing list 
list = [100, 75, 21, 61, 29, 89] 
  
# initializing k 
k = 30
  
# printing list  
print ("The list : " + str(list)) 
  
# using list comprehension 
# to get numbers > k 
count = len([i for i in list if i > k]) 
  
# printing the intersection  
print ("The numbers greater than 30 are : " + str(count)) 


# In[60]:


# Method 2

from bisect import bisect 
  
# initializing list 
list1 = [15, 27, 35, 66, 3, 48] 
  
# initializing k 
k = 30
  
# printing list  
print ("The list : " + str(list1)) 
  
# using bisect() + sort() 
# to get numbers > k 
list1.sort() 
count = len(list1) - bisect(list1, k) 
# printing the intersection  
print ("The numbers greater than 30 are : " + str(count)) 


# In[61]:


# Method 3

list2 = [11, 53, 24, 95]
a = 30

Greater_elements = [element for element in list2 if element > a]
number_of_elements = len(Greater_elements)

print(number_of_elements)


# In[12]:


# Method 4

list2=[34,65,23,11,10,56,78,900,455,655,1,2]
def greater(list2):
    c=0
    for i in list2:
        if i>30:
            c=c+1
    print(list2)
    print("Numbers greater than 30 in the given list :",c)
greater(list2)


# - Q.4 Write a Python function that takes a list and returns a  new list with unique elements of the first list. 

# In[2]:


# Method 1

def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
        return x
print(unique_list([1,2,3,3,3,3,4,5])) 


# In[9]:


# Method 2

numbers = [11, 22, 22, 33, 34, 34, 55]
unique_numbers = list(set(numbers))
print(unique_numbers)


# In[13]:


# Method 3

ulist=[1,2,3,4,5,1,2,3,1,5,6,7,8,9,100,122,122,11,121,121,11]
def uniq(ulist):
    list3=[]
    for l in ulist:
        if l not in list3:
            list3.append(l)
    return(list3)
    print("New list with unique elements :",list3)
uniq(ulist)


# - Q.5 Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and       if the salary is missing in function call it should show it as 9000
# 

# In[31]:


def showEmployee(name, salary=9000):
    print("Employee", name, "salary is:", salary)
showEmployee("Jyoti", 9000)
showEmployee("Jyoti")


# - Q.6 Write a Python program to count the even, odd numbers in a given array of integers using Lambda.

# In[13]:


# Method 1

array_numbers = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_numbers)
even_numbers = len(list(filter(lambda x: (x%2 == 0) , array_numbers)))
odd_numbers = len(list(filter(lambda x: (x%2 != 0) , array_numbers)))
print("\nNumber of even numbers in the above array: ", even_numbers)
print("\nNumber of odd numbers in the above array: ", odd_numbers)


# In[23]:


# Method 2

arr=[24,25,34,65,77,88,98,100,23]
eve=len(list(filter(lambda el1: el1%2==0,arr)))
odd=len(list(filter(lambda ol1: ol1%2!=0,arr)))
print("Even numbers :", eve)
print("Odd numbers :", odd)


# - Q.7 Write a Python program to add two given lists using map and lambda

# In[15]:


# Method 1

list4 = [1, 2, 3]
list5 = [4, 5, 6]
print("Original list:")
print(list4)
print(list5)
result = map(lambda x, y: x + y, list4, list5)
print("\nResult: After adding  of two lists")
print(list(result))


# In[24]:


# Method 2

list5=[1,2,3,5]
list6=[2,3,5,6]
add_list=list(map(lambda x,y:x+y,list5,list6))
print("Lists added result :",add_list)


# - Q.8  Write a Python program to rearrange positive and negative numbers in a given array using Lambda and filter.

# In[27]:


# Method 1

array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result =[x for x in array_nums if x < 0] + [x for x in array_nums if x >= 0]
print("\nRearrange positive and negative numbers of the said array:")
print(result)


# In[28]:


# Method 2

data=[-9,-8,-7,5,6,8,7,2,5,-1,-5] 
data=list(filter(lambda x:x!=0,data)        )#no zero 
 
nPositive=sum(map(lambda x:1 if x>0 else 0,data)) 
if nPositive>len(data)-nPositive: 
    iPositve=0 
    iNegative=1 
else: 
    iPositve=1 
    iNegative=0 
while True: 
    while iPositve<len(data) and data[iPositve]>0: 
        iPositve+=2 
    while iNegative<len(data) and data[iNegative]<0: 
        iNegative+=2 
    if iPositve>=len(data) or iNegative>=len(data): 
        break 
    t=data[iPositve] 
    data[iPositve]=data[iNegative] 
    data[iNegative]=t 
print(data) 


# - Q.9  Write a Python program to filter a list of integers using Lambda. 

# In[9]:


# Method 1

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(new_list)
print("\nEven numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, new_list))
print(even_nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, new_list))
print(odd_nums)


# In[28]:


# Method 2

lst8 = [88, 28, 67, 46, 32, 12]
small = filter(lambda x: x>60, lst8)
print("Filtered using some condition :",list(sorted(small)))


# - Q.10 Write a Python program to find the intersection of two given arrays using Lambda and filter.

# In[10]:


# Method 1

array_list6 = [1, 2, 3, 5, 7, 8, 9, 10]
array_list7 = [1, 2, 4, 8, 9]
print("Original arrays:")
print(array_list6)
print(array_list7)
result = list(filter(lambda x: x in array_list6, array_list7)) 
print ("\nIntersection of the said arrays: ",result)


# In[29]:


# Method 2

listi=[9,8,7,6,10,12]
listj=[10,12,7,8,5,4]
res=list(filter(lambda x:x in listi,listj))
print("List1 :", listi)
print("List2 :", listj)
print("Intersected values of two lists :", res)


# In[ ]:


# Method 3

def interSection(arr1,arr2): # finding common elements

# using filter method oto find identical values via lambda function
     values = list(filter(lambda x: x in arr1, arr2))
     print ("Intersection of arr1 & arr2 is: ",values)

# Driver program
if __name__ == "__main__":
    arr1 = ['D','A','T','A','S','C','I','E','N','T','I','S','T']
    arr2 = ['P','Y','T','H','O','N']
    interSection(arr1,arr2)


# In[ ]:





# In[ ]:





# In[ ]:




