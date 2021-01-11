# -*- coding: utf-8 -*-
"""
@author: massy

code display a resum of the survey 
"""

def survey_resum(info_users,nb_user):
    
    
    # we display all the department of the users without redundancies
    print("\n\nThe users come from this department :")
    # We make a copie of the data to avoid displaying duplicates data
    double_info = [""]*nb_user
    for i in range(nb_user) :
        if info_users[i]["dept"] not in double_info :
            print(info_users[i]["dept"],  end=' ')
            double_info[i] += info_users[i]["dept"]


    # we display all the profesion of the users without redundancies
    print("\n\nThe profesion of the users is :")
    double_info = [""]*nb_user
    for i in range(nb_user) :
        if info_users[i]["profession"] not in double_info :
            print(info_users[i]["profession"],  end=' ')
            double_info[i] = info_users[i]["profession"]
    
    
    # we calculate and display the average age of the users
    sum_age = 0
    for i in range(nb_user) :
        sum_age += info_users[i]["age"]
    avg_age = round(sum_age / nb_user,2)
    print("\n\nThe average age of the users is : ", avg_age, "years")


    # we calculate the number of men who have answer the survey
    sum_men = 0
    for i in range(nb_user) :
        if info_users[i]["gender"] == "M" :
            sum_men += 1
    # we calculate the % of men and woman and display the result
    percentage_men = round(((sum_men/nb_user)*100),2)
    percentage_woman = round((100 - percentage_men),2)
    print("\nTheir is ", percentage_men, "% of men and ",  percentage_woman, "% of woman who have answer to the survey")    
    