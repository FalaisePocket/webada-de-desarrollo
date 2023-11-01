from pymongo import MongoClient
import certifi


MONGO_URI='mongodb+srv://FalaisePocket:ElefanteLoco@clusterapi.qd8usss.mongodb.net/?retryWrites=true&w=majority'

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI,tlsCAFile=ca)
        db= client["testdeltest"]
    except ConnectionError:
        print('Nah, que basura')
    return db