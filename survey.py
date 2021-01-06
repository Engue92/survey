# -*- coding: utf-8 -*-
"""
@author: massy

code who make all the interaction with the user
"""

import infoperso

def survey(proposition,score,nb_prop,nb_user,user_info): 
    
    y = 0
    while y < nb_user :   
        print("\nUser number ",(y+1)," answer to the survey :")
        
        i = 0
        while i < nb_prop :
            print(nb_prop)
            # we display the proposition and waiting for the answer
            print("\nThe proposition is :")
            print(proposition[i])
            print("\nWhat do you think about this ?")
            ans = int(input("Agree (1), Disagree (2), No opinion (3), End (4), Other idea (5) :\n"))
            
            # if the user is agree
            if ans == 1 :
                score[i] += 1
                i += 1
                
            # if the user is disagree
            if ans == 2 :
                score[i] -= 1
                i += 1
                
            # if the user have no opinion
            if ans == 3 :
                i += 1
            
            # if the user want to end the survey
            elif ans == 4 :
                print("End of the survey")
                break
                
            # if the user want to enter a new proposition
            elif ans == 5 :
                if nb_prop == 100 : # if the list of proposition is empty
                    print("\nMaximum of proposition reached")
                
                else :
                    new_proposition = input("Enter your proposition :\n")
                    proposition[nb_prop] = new_proposition
                    nb_prop += 1
                    # We looking if their is no other similar proposition
                    x = 0
                    while x < nb_prop-1 :
                        # If the new proposition is the same than another one
                        if new_proposition == proposition[x] : 
                            print("Your proposition is the same than another")
                            nb_prop -= 1
                            proposition[nb_prop] = ""
                        x += 1
        
        # We use the infoperso function to colect the user information
        info_perso = infoperso.infoperso()
        # we store the curent user information in the user_info liste who content the informations of all the users
        user_info += [info_perso]
        y += 1
        
    # we returne the score, the proposition et their number, and the user information liste
    return (score,proposition,nb_prop,user_info)




