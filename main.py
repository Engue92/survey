# -*- coding: utf-8 -*-
"""
@author: massy

This code is the main code of the project
It used to run the entire programme

libraries: init_survey, unit_survey, sort_data, display, save_data, save_infoperso
"""

import init_survey as init
import unit_survey
import sort_data as sort
import display
import save_data as sd
import save_infoperso as si

# call the function to initialise or load the data
(nb_prop,score,proposition,user_info) = init.init_survey()

# call the function to execute the survey for users
(score, proposition, nb_prop, user_info) = unit_survey.unit_survey(proposition, score, nb_prop, user_info)

# call the function to save the results in a file
sd.backup_survey(nb_prop,score,proposition)

# call the function to save the users informations in a file
si.backup_info_perso(user_info)

# call the function to sort the results
(score_sort, prop_sort) = sort.sort_data(score, proposition, nb_prop, user_info)

# call the data to display the results
display.display_result(prop_sort, score_sort, nb_prop, user_info)


