#!/usr/bin/env python3
""" Inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Insert document in the collection and
    returns the _id of the new inserted document. """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
