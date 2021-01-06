# -*- coding: utf-8 -*-
"""
@author: massy

code to sort the data frome the highest score to the lowest in funtion of the proposition
"""

def sort_data(score,proposition,nb_prop,nb_user):

    # we create new table for the sort score and proposition
    score_sort = [0]*100
    prop_sort = proposition
    
    x = 0
    i = 0
    y = 0
    
    # we creat a maxi variable used to looking for the highest score
    # we set it at this value because it's the lowest we can have
    maxi = -(nb_user + 1)
    
    while y < nb_prop :
        while i < nb_prop :
            if score[i] > maxi :
                # if we find a highest value, we record its value and position 
                maxi = score[i]
                sup = i
            i += 1
        # we record the score and the proposition in the next position of the new table
        (score_sort[x],prop_sort[x]) = (score[sup],proposition[sup])
        x += 1
        # we put the score to the lowest possible so as not to meet him again 
        score[sup] = -(nb_user + 1)
        i = 0
        # we reset the value of the maximum to find the next one
        maxi = -(nb_user + 1)
        y += 1
        
    # we returne the score and the proposition sort
    return(score_sort,prop_sort)