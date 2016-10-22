#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# Q1: For each person, how many features are available?
print enron_data
# A1: check out enron_data.txt, 21 features.

# Q2: The "poi" feature records whether the person is a person of interest, according to our definition.
#       How many POIs are there in the E+F dataset?
print enron_data["METTS MARK"]["poi"]

count = 0
for person_name in enron_data:
    #print person
    if enron_data[person_name]["poi"] == 1:
        count += 1
print count
# A2: count = 18
