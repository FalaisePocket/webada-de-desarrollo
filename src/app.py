from flask import Flask, render_template, request,Response, jsonify,redirect,url_for
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import MongoClient
import database as dbase
from list import Carrito
from bson import json_util

db=dbase.dbConnection()

app=Flask(__name__)
CORS(app)

#rutas
@app.route('/')
def home():
    carritodb=db['usertest']
    carritoslist=carritodb.find()
    return render_template('index.html',carritos=carritoslist)

@app.route('/fetch/<string:id>',methods=['GET'])
def fetch(id):
    carritodb=db['usertest']
    carritouserlist=carritodb.find_one({'userid':id})
    
    if carritouserlist:
        response=json_util.dumps(carritouserlist)
        
        return Response(response, mimetype='application/json')
    else:
        return "No se encontró",404


#registra POST METHOD
@app.route('/userRegist', methods=['POST'])
def regist():
    
    carritodb = db['usertest']
    userid=request.form['userid']
    list=request.form['list']
    newlist=[]
    if userid and list:
        carritonew = Carrito(userid,list)
        carritodb.insert_one(carritonew.toDBCollection())
        response = jsonify({
            'userid': userid,
            'list':list
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#DELETE METHOD 
@app.route('/delete/<string:user_id>')
def delete(user_id):
    carritodb=db['usertest']
    carritodb.delete_one({'userid':user_id})
    return redirect(url_for('home'))




#edit PUT METHOD
@app.route('/edit/<string:user_id>',methods=['POST'])
def editcarrito(user_id):
    carritodb = db['usertest']
    userid=request.form['userid']
    lista=request.form['list']


    if userid and lista:
        carritodb.update_one({'userid':user_id},{'$set':  {'userid':userid,'list':lista}   }   )
        response = jsonify({'message':'Carrito editado'})
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message':'No fue posible',
        'status':'404 Not Found'
    }    
    response = jsonify(message)
    response.status_code=404
    return response


if __name__== "__main__":
    app.run(debug=True)


