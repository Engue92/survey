# -*- coding: utf-8 -*-
"""
@author: massy

This code is used to :
    save (backup_info_perso)  
    load (load_info_perso) 
    init (init_info_perso)
the personal information of the users in a file (info_perso.json)

libraries: os, json
"""

import os
import json

# function to initialise the users informations dictionary 
def init_info_perso():
    """
    Returns
    -------
    user_info : dictionary
        all the personal information of the users.
    """
    path = os.getcwd()
    #
    os.makedirs(path + "/backup_info_perso")
    f = open(path + "/backup_info_perso/info_perso.json", "w")
    f.close()
    user_info = []
    return(user_info)

# function to save the users informations dictionary 
def backup_info_perso(user_info):
    """
    Parameters
    ----------
    user_info : dictionary
        all the personal information of the users.
    Returns
    -------
    None.
    """
    path = os.getcwd()
    f = open(path + "/backup_info_perso/info_perso.json", "w")
    json.dump (user_info, f, sort_keys = True, indent = 4)
    f.close()
    
# function to load the users informations dictionary 
def load_info_perso():
    """
    Returns
    -------
    user_info : dictionary
        all the personal information of the users.
    """
    path = os.getcwd()
    f = open(path + "/backup_info_perso/info_perso.json", "r")
    user_info = json.load(f)
    f.close()
    
    return(user_info)




