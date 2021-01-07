# -*- coding: utf-8 -*-
"""
@author: massy

code to display the results
"""

import survey_resum 

def display_result(proposition,score,nb_prop,info_users,nb_user):
    
    # dislplay the first part
    print("\n",80*"-")
    print("{0:^80}".format("RESULTS"))
    print(80*"-")
    
    # display the score and the proposition sort from the highest score to the lowest 
    for i in range(nb_prop) :
        print("{0:^10}{1:70}".format(score[i],proposition[i]))
        i += 1
        
    # use the programe who display the resum of the survey
    survey_resum.survey_resum(info_users,nb_user)
        
        
    
    
    
    
