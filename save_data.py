# -*- coding: utf-8 -*-
"""
@author: massy

This code is used to :
    save (backup_survey)  
    load (load_survey) 
    init (init_save_data)
the results of the survey in a file (data_survey.txt)

libraries: os
"""

import os

# function used to initialise the data 
def init_save_data():
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
    
    return (nb_prop,score,proposition)


# this function is used to store the data
def backup_survey(nb_prop,score,proposition):
    """
    Parameters
    ----------
    nb_prop : int
        total number of proposition.
    score : table of int
        all the score attached to a proposition.
    proposition : table of string
        all the proposition of the survey.
    Returns
    -------
    None.
    """
    path = os.getcwd()
    # we opened the file
    fichier = open(path + "/backup_survey/data_survey.txt", "w", encoding="utf8")
    # we write the number of proposition in the first line of the file
    fichier.write("{0}\n".format(nb_prop))
    for i in range(nb_prop):
        # we write the score in the 4 first characters then a space and finely the proposition in 100 characters
        fichier.write("{0:4} {1:100}\n".format(score[i],proposition[i]))
    fichier.close()  # we close the file
    
    
# This function is used to load the data
def load_survey():
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
    # we opened the file
    fichier = open(path + "/backup_survey/data_survey.txt", "r", encoding="utf8")
    # we take all the lines of the file in one variable
    allcontent = fichier.readlines()
    # the first line is the number of proposition
    nb_prop = int(allcontent[0])
    score = [0]*100
    proposition = [""]*100
    
    for i in range(nb_prop):
        # we allocate the beginin of the file to the score table 
        score[i] = int(allcontent[i+1][0:4])
        # we allocate the rest of the file to the proposition table 
        proposition[i] = allcontent[i+1][5:105]
    fichier.close()  # we close the file
    # we return the empty score and proposition table and the number of proposition
    return(nb_prop,score,proposition)





    