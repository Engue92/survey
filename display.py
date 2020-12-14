# -*- coding: utf-8 -*-
"""
@author: massy

code to display the results
"""

def display_result(proposition,n,score):
    
    print(80*"-")
    print("{0:^80}".format("RESULTS"))
    print(80*"-")
    
    score_bis = score
    
    i = 0
    y = 0
    maxi = -1000
    
    while y < n+1 :
        while i < n+1 :
            if score_bis[i] > maxi :
                maxi = score_bis[i]
                sup = i
            i += 1
        print("{0:^10}{1:70}".format(score_bis[sup],proposition[sup]))
        score_bis[sup] = -1000
        (i,maxi) = (0,-1000)
        y += 1
    
        
        
    
    
    
    
