# -*- coding: utf-8 -*-
"""
@author: massy

This code is used to sort the data frome the highest score to the lowest in funtion of the proposition

libraries:
"""

def sort_data(score,proposition,nb_prop,user_info):
    """
    Parameters
    ----------
    score : table of int
        all the score attached to a proposition.
    proposition : table of string
        all the proposition of the survey.
    nb_prop : int
        total number of proposition.
    user_info : dictionary
        all the personal information of the users.

    Returns
    -------
    score_sort : table of int
        all the score sort from the biggest to the smallest attached to a proposition.
    prop_sort : table of string
        all the proposition of the survey sort from the biggest to the smallest
    """
    
    # we create a copie of the score in order to save our data
    score_copie = score[:]
    # we create new table for the sort score and proposition
    score_sort = [0]*nb_prop
    prop_sort = [""]*nb_prop
    
    # j is a cunter to empty the prop_sort and score_sort table
    j = 0
    
    # we creat a maxi variable used to looking for the highest score
    # we set it at this value because it's the lowest we can have
    tot_user = (len(user_info.keys()))
    maxi = -(tot_user + 1)
    
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
        score_copie[sup] = -(tot_user + 1)
        # we reset the value of the maximum to find the next one
        maxi = -(tot_user + 1)
        
    # we returne the score and the proposition sort
    return(score_sort,prop_sort)