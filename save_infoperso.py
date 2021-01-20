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

"""
user_info = load_info_perso()
tot_rep = (len(user_info.keys()))
tot_rep += 1
nb_rep = str(tot_rep)
    
    # we create the id of the user
if tot_rep < 10:
    user_id = "respondant #00"+nb_rep
elif tot_rep >= 10 and tot_rep < 100:
    user_id = "respondant #0"+nb_rep
elif tot_rep >= 100:
    user_id = "respondant #"+nb_rep
"""
"""
tot = 0
for cle, valeur in user_info.items():
    #print("\n",user_info[cle]['age'])
    tot += int(user_info[cle]['age'])

moyenne = tot / 4
print(moyenne,"\n")
"""
"""
for cle, valeur in user_info.items():
    print("\n",user_info[cle]['gender'])

"""








