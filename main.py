# -*- coding: utf-8 -*-
"""
@author: massy

main code of the project to 
"""

import init
import survey
import sort_data as sort
import display
import save_data as sd

nb_user = int(input("How many users answer the survey ?\n"))

users_info = []*nb_user

(nb_prop,score,proposition) = init.init()

(score, proposition, nb_prop, users_info) = survey.survey(proposition, score, nb_prop, nb_user, users_info)

sd.backup_survey(nb_prop,score,proposition)

(score_sort, prop_sort) = sort.sort_data(score, proposition, nb_prop, nb_user)

input("Press enter to have the results of the survey")
display.display_result(prop_sort, score_sort, nb_prop, users_info, nb_user)


