# -*- coding: utf-8 -*-
"""
@author: massy

This code is the main code of the project

libraries: init_survey, unit_survey, sort_data, display, save_data
"""

import init_survey as init
import unit_survey
import sort_data as sort
import display
import save_data as sd

nb_user = int(input("How many users answer the survey ?\n"))

users_info = []*nb_user

# call the function to initialise or load the data
(nb_prop,score,proposition) = init.init_survey()

# call the function to execute the survey for users
(score, proposition, nb_prop, users_info) = unit_survey.unit_survey(proposition, score, nb_prop, nb_user, users_info)

# call the function to save the results in a file
sd.backup_survey(nb_prop,score,proposition)

# call the function to sort the results
(score_sort, prop_sort) = sort.sort_data(score, proposition, nb_prop, nb_user)

# call the data to display the results
display.display_result(prop_sort, score_sort, nb_prop, users_info, nb_user)


