# -*- coding: utf-8 -*-
"""
@author: massy

code to sort the data frome the highest score to the lowest in funtion of the proposition
"""

def sort_data(score,proposition,nb_prop,nb_user):

    # we create new table for the sort score and proposition
    score_copie = score[:]
    score_sort = [0]*100
    prop_sort = proposition
    
    j = 0
    
    # we creat a maxi variable used to looking for the highest score
    # we set it at this value because it's the lowest we can have
    maxi = -(nb_user + 1)
    
    for y in range(nb_prop) :
        for i in range(nb_prop) :
            if score_copie[i] > maxi :
                # if we find a highest value, we record its value and position 
                maxi = score_copie[i]
                sup = i
        # we record the score and the proposition in the next position of the new table
        (score_sort[j],prop_sort[j]) = (score_copie[sup],proposition[sup])
        j += 1
        # we put the score to the lowest possible so as not to meet him again 
        score_copie[sup] = -(nb_user + 1)
        # we reset the value of the maximum to find the next one
        maxi = -(nb_user + 1)
        
    # we returne the score and the proposition sort
    return(score_sort,prop_sort)