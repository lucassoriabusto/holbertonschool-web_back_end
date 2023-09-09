#!/usr/bin/env python3
""" Function that changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ Utiliza update_many para actualizar varios documentos """
    result = mongo_collection.update_many({"name": name},
                                          {"$set": {"topics": topics}})

    """ Returns the update_many() method and the number of documents
    that were modified during the update operation """
    return result.modified_count
