# -*- coding: utf-8 -*-
"""
@author: massy

code to manage personal information
"""

def infoperso() :    
    print(1)
    age = int(input("Enter your age :\n"))
    gender = input("Enter your sex :\n")
    dept = input("Enter your housing department :\n" )
    profession = input("Enter your profession :\n")
    
    infoperso = {"age":age, "gender":gender, "dept":dept, "profession":profession}
    
    print("age : ",age)
    print("gender : ",gender)
    print("deot : ",dept)
    print("profession : ",profession)
    
    return (infoperso)
