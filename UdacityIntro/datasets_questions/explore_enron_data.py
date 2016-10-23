#!/usr/bin/python
# coding=utf-8

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

# Q1:
#   For each person, how many features are available?
print enron_data
# A1: check out enron_data.txt, 21 features.

# Q2:
#   The "poi" feature records whether the person is a person of interest, according to our definition.
#   How many POIs are there in the E+F dataset?

#print enron_data["METTS MARK"]["poi"]

count = 0
for person_name in enron_data:
    #print person_name
    if enron_data[person_name]["poi"] == 1:
        print person_name
        count += 1
print count
# A2: count = 18

# Q3:
#   We compiled a list of all POI names (in ../final_project/poi_names.txt) and associated email addresses
#   (in ../final_project/poi_email_addresses.py).
#   How many POI’s were there total?
#   (Use the names file, not the email addresses, since many folks have more than one address and
#   a few didn’t work for Enron, so we don’t have their emails.)
#
# A3: counted 35 names in poi_names.txt

# Q4:
#   What might be a problem with having some POIs missing from our dataset?
#
# A4:
#   There are a few things you could say here, but our main thought is about having enough data to really learn the
#   patterns. In general, more data is always better--
#   only having 18 data points doesn't give you that many examples to learn from.

# Q5:
# Like any dict of dicts, individual people/features can be accessed like so:
#
# enron_data["LASTNAME FIRSTNAME"]["feature_name"]
# or, sometimes
# enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]
#
# What is the total value of the stock belonging to James Prentice?
print enron_data["PRENTICE JAMES"]
exercised_stock_options = enron_data["PRENTICE JAMES"]["exercised_stock_options"]
restricted_stock = enron_data["PRENTICE JAMES"]["restricted_stock"]
restricted_stock_deferred = enron_data["PRENTICE JAMES"]["restricted_stock_deferred"]
total_stock_value = enron_data["PRENTICE JAMES"]["total_stock_value"]
print total_stock_value
# A5:
#   total_stock_value = 1095040

# Q6:
# Like any dict of dicts, individual people/features can be accessed like so:
# enron_data["LASTNAME FIRSTNAME"]["feature_name"]
# How many email messages do we have from Wesley Colwell to persons of interest?
print enron_data["COLWELL WESLEY"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
# A6:
#   from_this_person_to_poi = 11

# Q7:
# Like any dict of dicts, individual people/features can be accessed like so:
# enron_data["LASTNAME FIRSTNAME"]["feature_name"]
# or
# enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]
# What’s the value of stock options exercised by Jeffrey K Skilling?
print enron_data["SKILLING JEFFREY K"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
# A7:
#   exercised_stock_options = 19250000

