# -*- coding: utf-8 -*-
"""
@author: massy

This code is used to execute the survey for users

libraries: infoperso
"""

import infoperso

def unit_survey(proposition,score,nb_prop,user_info): 
    """
    Parameters
    ----------
    proposition : Table of string
        all the proposition of the survey.
    score : Table of int
        all the score attached to a proposition.
    nb_prop : int
        total number of proposition.
    user_info : dictionary
        all the personal information of the users.

    Returns
    -------
    score : table of int
        all the score attached to a proposition.
    proposition : table of string
        all the proposition of the survey.
    nb_prop : int
        total number of proposition.
    user_info : dictionary
        all the personal information of the users.
    """
    
    print("You will answer the participatory survey on global warming")
    input("Press enter to start the survey")
        
    i = 0
    while i < nb_prop :
        # we display the proposition and waiting for the answer
        print("\nThe proposition is :")
        print(proposition[i])
        print("\nWhat do you think about this ?")
        ans = int(input("Agree (1), Disagree (2), No opinion (3), End (4), Other idea (5) :\n"))
        
        # if the user is agree
        if ans == 1 :
            score[i] += 1
            
        # if the user is disagree
        elif ans == 2 :
            score[i] -= 1
        
        # if the user want to end the survey
        elif ans == 4 :
            print("End of the survey")
            break
        
        # if the user want to enter a new proposition
        elif ans == 5 :
            i -= 1
            if nb_prop == 100 : # if the list of proposition is empty
                print("\nMaximum of proposition reached")
            
            else :
                new_proposition = input("Enter your proposition :\n")
                # we add space after the proposition because we save proposition in 100 characters in the file
                new_proposition = new_proposition + (" "*(100-(len(new_proposition))))
                proposition[nb_prop] = new_proposition
                nb_prop += 1
                test = True # variable to know if the proposition is ok or not 
                # We looking if their is no other similar proposition
                for j in range(nb_prop-1) :
                    # If the new proposition is the same than another one we remove it
                    if new_proposition.upper() == proposition[j].upper() : 
                        print("Your proposition is the same than another")
                        nb_prop -= 1
                        proposition[nb_prop] = ""
                        test = False
                if test == True :
                    print("Your proposition is registered")
            input("Press enter to continue")
        i += 1 
        
        
    # We use the infoperso function to colect the user information
    info_perso = infoperso.infoperso()
    
    # tot_rep is the number of users who have already answered
    tot_rep = (len(user_info.keys()))
    tot_rep += 1
    nb_rep = str(tot_rep)
    
    # we create the id of the user
    if tot_rep < 10:
        user_id = "respondant #00"+nb_rep
    elif tot_rep >= 10 and tot_rep < 100:
        user_id = "respondant #0"+nb_rep
    elif tot_rep >= 100:
        user_id = "respondant #"+nb_rep
    
    # we store the information of the user in the user_info dictionary 
    user_info[user_id] = info_perso
    
    # end of the survey for a user
    input("Press enter to end the survey")
    
    # end of the survey for all users
    input("Press enter to have the results of the survey")

    # we returne the score, the proposition et their number, and the user information liste
    return (score,proposition,nb_prop,user_info)




