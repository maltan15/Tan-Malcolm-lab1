#!/usr/bin/env python
# coding: utf-8

# # Assignment: Lab 1
# 
# ## Instructions
# 
# This is the template file for the assignment of Module 4 called "Lab 1." Please carefully follow the instructions below.
# 
# 1. Rename this file by filling out your surname and first name in the file name. For example, if your surname is Ilagan and if your first name is Joben, then rename the file to ILAGAN-JOBEN-lab1.ipynb.
# 2. Fill out the markdown cell just above `Problem 1` with your student details as indicated.  
# 3. To submit this file, first, upload your file to your GitHub repository and, second, submit your repository link to the assignment on Canvas.

# ## Student Details
# 
# ID Number:  204957
# Surname: Tan, Malcolm
# Year and Course:  2 BS ITE

# ## Problem 1 (3 points)
# 
# ### Currency Converter  
# 
# Overall prompt: **Write a function called `dollars_to_pesos` that accepts an amount in US dollars and that RETURNS a string that indicates the equivalent amount in Philippine pesos.**  
# 
# The program must follow these specifications: 
# 1. It is very important that your entire program is contained within a function. It is also very important that your output value is **returned** and not merely printed. This is to make sure that the function, when called, actually evaluates to a value instead of merely printing the calculated value out to the terminal. This is because the function, conceptually, is intended to be a utility function for further conversions, so it needs to evaluate to a value on its own.
# 2. The function must accept the input through one parameter called `dollars`.
# 3. The function must return a string that is formatted as follows: `{dollars} US dollar(s) = {pesos} Philippine pesos.`, where `dollars` is the amount of dollars given as input and where `pesos` is the equivalent amount of pesos for the given dollars. 
# 4. For simplicity, use the conversion rate \$1 = PHP 50.  
# 
# #### Sample Input and Output  
# 
# Sample Input:  
# `Enter the amount in US Dollars: 1`  
# Sample Output:  
# `1 US dollar(s) = 50 Philippine Pesos.`  

# In[17]:


def dollars_to_pesos():
    dollars_to_pesos = int(input('Enter the amount in US Dollars: '))
    amount = dollars_to_pesos * 50
    return amount, 'Philippine Pesos'  


# In[18]:


dollars_to_pesos()


# ## Problem 2 (3) 
# ### Numerical Operations  
# 
# Overall prompt: **Write a function called `perform_operations` that accepts two parameters, `x` and `y`, which are integers. The function should PRINT the results of performing operations on those two numbers.**  
# 
# The program must follow these specifications:
# 1. It is very important that the function **prints** the output this time.  
# 2. The function must accept two parameters, `x` and `y`, which are both integers.
# 3. The function should print the results of *addition*, *subtraction*, *multiplication*, *division without the remainder*, and finally the *remainder upon division* of `x` and `y` on separate lines.
# 
# #### Sample Input and Output 
# 
# Sample Input:  
# `55`  
# `3`  
# Sample Output:  
# `58`  
# `52`  
# `165`  
# `18`  
# `1`  

# In[ ]:


def perform_operations():
    first_input = int(input('X: '))
    second_input = int(input('Y: '))
    print (first_input + second_input)
    print (first_input - second_input)
    print (first_input * second_input)
    print (first_input // second_input)
    print (first_input % second_input)


# In[ ]:


perform_operations ()


# ## Problem 3 (4) 
# ### BMI Calculator  
# 
# Overall prompt: **Write a function called `bmi` that computes for and _returns_ your Body Mass Index (BMI). The formula for BMI is as follows:**  
# 
# `BMI = (kg) / (m^2)`  
# 
# In the formula, `kg` is a person's weight in kilograms, and `m` is the person's height in meters.  
# 
# The program must follow these specifications:  
# 1. The function `bmi` must accept two parameters `kg` and `cm`, where `kg` is a person's weight in kilograms and `cm` is the person's height in _centimeters_.  
# 2. The function must return a _float_. This float will be checked for computational accuracy within 4 decimal places.  
# 
# #### Sample Input and Output
# 
# Sample Input:  
# `kg = 65, cm = 180`  
# Sample Output:  
# `20.061728395061728`  

# In[1]:


def bmi():
    first_input = int(input('kg: '))
    second_input = int(input('cm: '))
    meters = second_input / 100
    convertion = (first_input / meters**(2))
    return convertion


# In[2]:


bmi()


# In[ ]:




