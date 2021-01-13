# -*- coding: utf-8 -*-
"""
@author: massy

This code is used to initialise the data or load them from the file

libraries: os, save_data
"""

import os
import save_data as sd

def init_survey():
    """
    Returns
    -------
    nb_prop : int
        total number of proposition.
    score : table of int
        all the score attached to a proposition.
    proposition : table of string
        all the proposition of the survey.
    """
    
    path = os.getcwd()
    # if the file alredy existe we load the data from it
    if os.path.exists(path + "/backup_survey/data_survey.txt"):
        (nb_prop,score,proposition) = sd.load_survey()
        
    # if it does not existe we create it and fill it
    else:
        os.makedirs(path + "/backup_survey")
        fichier = open(path + "/backup_survey/data_survey.txt", "w", encoding="utf8")
        
        # insert and create the number of proposition
        nb_prop = 5
        fichier.write("5\n")
        
        # insert the 5 first proposition to the file 
        fichier.write("{0:4} {1:100}\n".format("0","Boycott products that are too bad for the climate"))
        fichier.write("{0:4} {1:100}\n".format("0","Stop using coal"))
        fichier.write("{0:4} {1:100}\n".format("0","Use green energy"))
        fichier.write("{0:4} {1:100}\n".format("0","Eat less meat to reduce pollution from animal husbandry"))
        fichier.write("{0:4} {1:100}\n".format("0","Avoid products that come from the other side of the world"))
        fichier.close()
        
        # Create proposition table and insert the 5 first
        proposition = [""]*100
        proposition[0] = "Boycott products that are too bad for the climate"
        proposition[1] = "Stop using coal"
        proposition[2] = "Use green energy"
        proposition[3] = "Eat less meat to reduce pollution from animal husbandry"
        proposition[4] = "Avoid products that come from the other side of the world"
        
        # initialise the score table
        score = [0]*100
    
    # return the number of proposition the score and the proposition tables
    return (nb_prop,score,proposition)



