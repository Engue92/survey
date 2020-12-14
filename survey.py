# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:12:23 2020

@author: massy
"""

import infoperso
import display

# initial proposition
proposition = [""]*100
proposition[0] = "Boycott products that are too bad for the climate"
proposition[1] = "Stop using coal"
proposition[2] = "Use green energy"
proposition[3] = "Eat less meat to reduce pollution from animal husbandry"
proposition[4] = "Avoid products that come from the other side of the world"

score = [0]*100

i = 0
n = 4

while i < n+1 :
    
    # we display the proposition and waiting for the answer
    print("\nThe proposition is :")
    print(proposition[i])
    print("\nWhat do you think about this ?")
    ans = int(input("Agree (1), Disagree (2), No opinion (3), End (4), Other idea (5) :\n"))
    
    # if the user is agree
    if ans == 1 :
        score[i] = 1
        i += 1
        
    # if the user is disagree
    if ans == 2 :
        score[i] = -1
        i += 1
        
    # if the user have no opinion
    if ans == 3 :
        score[i] = 0
        i += 1
    
    # if the user want to end the survey
    elif ans == 4 :
        print("End of the survey")
        break
        
    # if the user want to enter a new proposition
    elif ans == 5 :
        if n == 99 : # if the list of proposition is empty
            print("\nMaximum of proposition reached")
        
        else :
            new_proposition = input("Enter your proposition :\n")
            n += 1
            proposition[n] = new_proposition
            # 4. We looking if their is no other similar proposition
            y = 0
            while y < n :
                if new_proposition == proposition[y] : # If the new proposition is the same than another one
                    print("Your proposition is the same than another")
                    proposition[n] = ""
                    n -= 1
                y += 1

infoperso.infoperso()
display.display_result(proposition,n,score)





