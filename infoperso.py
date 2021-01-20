# -*- coding: utf-8 -*-
"""
@author: massy

This code is used to colect the personal information of a user

libraries: 
"""

def infoperso() :    
    """
    Returns
    -------
    infoperso : dictionary
        all the personal information of a user.
    """
    
    # ask the age of the user
    age = int(input("Enter your age :\n"))
    
    # ask the gender of the user 
    gender = input("Enter your sex (M/W) :\n")
    gender = gender.upper()
    # ask again while we have not a corect answer
    while gender != "M" and gender != "W" :
        gender = input("Please enter M for men or W for woman :\n")
        gender = gender.upper()
    
    # ask the department of the user
    dept = input("Enter your housing department (nb) :\n" )
    
    # ask the profesion of the user
    profession = input("Enter your profession :\n")
    
    # store the user information
    infoperso = {"age":age, "gender":gender, "dept":dept, "profession":profession}
    
    # returne the user information
    return (infoperso)
