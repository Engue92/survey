# -*- coding: utf-8 -*-
"""
@author: massy

This code is used to :
    initialise the results of the survey  
    initialise the personal information 
    load them from the file if they exists

libraries: os, save_data, save_infoperso
"""

import os
import save_data as sd
import save_infoperso as si

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
    user_info : dictionary 
        all the personal information of the users.
    """
    
    path = os.getcwd()
    # if the file allredy existe we load the results of the survey from it
    if os.path.exists(path + "/backup_survey/data_survey.txt"):
        (nb_prop,score,proposition) = sd.load_survey()
    # if it does not existe we create it and fill it
    else:
        (nb_prop,score,proposition) = sd.init_save_data()
    
    # if the file allredy existe we load the personal information from it
    if os.path.exists(path + "/backup_info_perso/info_perso.json"):
        (user_info) = si.load_info_perso()
    # if it does not existe we create it 
    else:
        (user_info) = si.init_info_perso()    
    
    return (nb_prop,score,proposition,user_info)



