#!/usr/bin/env python3
""" Function that lists all documents in a collection """


def list_all(mongo_collection):
    """ Checks if the list is empty and returns an empty
    list if there is no document in the collection. """
    documents = mongo_collection.find({})
    document_list = list(documents)
    if not document_list:
        return[]
    return document_list
