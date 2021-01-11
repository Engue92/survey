# -*- coding: utf-8 -*-
"""
@author: massy

code used to save and load the data in files 
"""

import os

# this function is used to store the data
def backup_survey(nb_prop,score,proposition):
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

    
    