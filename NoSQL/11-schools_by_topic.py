#!/usr/bin/env python3
""" Function that returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic """
    tema = mongo_collection.find({"topics": topic})
    school_list = list(tema)
    return school_list
