from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import MongoClient
import database as dbase
from list import Carrito

app=Flask(__name__)
'''app.config['MONGO_URI']='mongodb+srv://FalaisePocket:ElefanteLoco@clusterapi.qd8usss.mongodb.net/'
mongo = MongoClient(app.config['MONGO_URI'])'''

#rutas
    #registra 
#@app.route('/userRegist')

if __name__== "__main__":
    app.run(debug=True)


