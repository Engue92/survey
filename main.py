# -*- coding: utf-8 -*-
"""
@author: massy

main code of the project to 
"""

import init
import survey
import sort_data as sort
import display

nb_user = int(input("How many users answer the survey ?\n"))

proposition = [""]*100
score = [0]*100
users_info = []*nb_user

(proposition) = init.init(proposition)

(score, proposition, nb_prop, users_info) = survey.survey(proposition, score, 5, nb_user, users_info)

(score_sort, prop_sort) = sort.sort_data(score, proposition, nb_prop, nb_user)

input("Press enter to have the results of the survey")
display.display_result(prop_sort, score_sort, nb_prop, users_info, nb_user)


