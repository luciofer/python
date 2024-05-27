import csv
from collections import deque
import elasticsearch
from elasticsearch import helpers


def get_movie_title():
    csvfile = open('ml-latest-small/movies.csv', 'r', encoding="utf8")
    reader = csv.DictReader(csvfile)

    title_lookup = {}
    for movie in reader:
        title_lookup[movie['movieId']] =  movie['title']

    return title_lookup

def create_tags():
    csvfile = open('ml-latest-small/tags.csv', 'r', encoding="utf8")
    reader = csv.DictReader(csvfile )
    tags = {}
    title_lookup = get_movie_title()

    for line in reader:
        tags['userId'] = int(line['userId'])
        tags['movieId'] = int(line['movieId'])
        tags['title']  = title_lookup[line['movieId']]
        tags['tag'] = line['tag']
        tags['timestamp'] = int(line['timestamp'])
        yield tags

es = elasticsearch.Elasticsearch(["http://127.0.0.1:9200"])
es.indices.delete(index="tags",ignore=404)
deque(helpers.parallel_bulk(es,create_tags(),index="tags"), maxlen=0)
es.indices.refresh()






