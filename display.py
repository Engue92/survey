# -*- coding: utf-8 -*-
"""
@author: massy

This code is used to display all the results

libraries:
"""

def display_result(proposition,score,nb_prop,info_users,nb_user):
    """
    Parameters
    ----------
    proposition : Table of string
        all the proposition of the survey.
    score : Table of int
        all the score attached to a proposition.
    nb_prop : int
        total number of proposition.
    info_users : table of string
        all the information of the users.
    nb_user : int
        total number of users.

    Returns
    -------
    None.
    """
    
    # dislplay the first part
    print("\n",80*"-")
    print("{0:^80}".format("RESULTS"))
    print(80*"-")
    
    # display the score and the proposition sort from the highest score to the lowest 
    for i in range(nb_prop) :
        print("{0:^10}{1:70}".format(score[i],proposition[i]))
        i += 1
        
    # use the programe who display the resum of the survey
    survey_resum.survey_resum(info_users,nb_user)
        

def survey_resum(info_users,nb_user):
    """
    Parameters
    ----------
    info_users : table of string
        all the information of the users.
    nb_user : int
        toal number of users.

    Returns
    -------
    None.
    """
    
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
    
    
    
    
    
