#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
    
def am_gm_hm(x,y):
    if (x==0 or y==0):
        print("Enter valid number greater than zero")
        exit()
    else:
        am=(x+y)/2
        gm=math.sqrt(x*y)
        hm=2/((1/x)+(1/y))
        print("Arithemetic Mean of two number is :",am)
        print("Geometric Mean of two number is :",gm)
        print("Harmonic Mean of two number is :",hm)       
am_gm_hm(x,y) 


# In[2]:


a=int(input("Enter value for first side of the triangle,a:"))
b=int(input("Enter value for second side of the triangle,b:"))
c=int(input("Enter value for third side of the triangle,c:"))


def check_triangle_inequality(a,b,c):
    if (a+b>c and b+c>a and c+a>b):
        print("Hence the sum of any two sides of a triangle is greater than the third side")
    elif(a+b==c or b+c==a or c+a==b):
        print("False")
    else:
        print("True,sum of any two sides of triangle is greather than the third side")
check_triangle_inequality(a,b,c)   


# In[3]:


import math

x=float(input("Enter the value of x in degrees:"))
k=int(input("Enter the number of terms k:"))

def calculate_sin(x,k):
    y=0
    for i in range(k):
        y=y+x**i/math.factorial(i)
        print(y)
calculate_sin(x,k)
        


# In[16]:


string1=str(input("Enter string1:"))
string2=str(input("Enter string2:"))

def check_substring(string1,string2):
    if string2 in string1:
        print("True")
    else:
        print("False")
check_substring(string1,string2)        
        


# In[26]:


string=input("Enter the string to generate substring:")

def generate_substring(string,n):
    for Len in range(1,n+1):
        for i in range(n-Len+1):
            j=i+Len-1
            
            for k in range(i,j+1):
                print(string[k],end="")
            print()
generate_substring(string,len(string))                


# In[39]:


x=input("Enter your name:")

def greet_me():
    print("Hello,",x,",how are you today?")
greet_me()    


# In[41]:


import math

x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
    
def mean_calculator(x,y):
    if (x==0 or y==0):
        print("Enter valid number greater than zero")
        exit()
    else:
        am=(x+y)/2
        gm=math.sqrt(x*y)
        hm=2/((1/x)+(1/y))
        print("Arithemetic Mean of two number(AM) is :",am)
        print("Geometric Mean of two number is(GM) :",gm)
        print("Harmonic Mean of two number is(HM) :",hm)       
mean_calculator(x,y) 


# In[54]:


a=int(input("Enter number to start with:"))
b=int(input("Enter number to end with:"))

def print_odd_for(a,b):
    for i in range(a,b+1):
        if i % 2 != 0:
            print(i)
print_odd_for(a,b)            


# In[ ]:


a=int(input("Enter number to start with:"))
b=int(input("Enter number to end with:"))
i=a

def print_odd_while(a,b,i):
    while i <= b:
        if(i%2 != 0):
            print(i)
            i=i+1
print_odd_while(a,b,i)
    


# In[13]:


def fibonacci(n):
    if n<= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
nterms=int(input("Enter number to find fibonacci terms:"))
if nterms<=0:
    print("Please enter number greater than zero")
else:
    print("Fibonacci sequence:")
    for i in range (nterms):
        print(fibonacci(i))                    


# In[14]:


def fibonacci_loop(n):
    if n<= 1:
        return n
    else:
        return(fibonacci_loop(n-1)+fibonacci_loop(n-2))
nterms=int(input("Enter number to find fibonacci terms:"))
if nterms<=0:
    print("Please enter number greater than zero")
else:
    print("Fibonacci sequence:")
    for i in range (nterms):
        print(fibonacci_loop(i)) 


# In[ ]:


value=1
sum=int(input("Enter number:"))

def sum_game(value):
    value=value+1
    while sum>value:
        print("Game Over!!")
        
        if sum==value:
            exit()
        else:
            sum=int(input("Enter number:"))
sum_game(value)        


# In[48]:


lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69] 
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
def list_overlap(list1,list2):
    list3=[value for value in list1 if value in list2]
    return list3
print(list3)
list_overlap(list1,list2)


# In[ ]:





# In[ ]:




