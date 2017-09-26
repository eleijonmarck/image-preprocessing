import flask
from flask_restful import request
import flask_restful

from cat_dog.extensions import auth

# import scipy.misc.imresize
import scipy.misc

from keras.models import model_from_json


import json
class LoggedInResource(flask_restful.Resource):
    method_decorators = []

class CatDog(LoggedInResource):
    def post(self):
        json_file = open('first_try.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("first_try.h5")
        print('loaded the model')
        # file = request.files['image']
        file = request.files.get('photo')
        print(file.filename)
        file.filename="our.jpg"
        print(file.filename)
        print(file.filename)
        file.save(file.filename)
        testimage = scipy.misc.imresize(scipy.misc.imread(file),(150,150))
        testimage = testimage.reshape((1,) + testimage.shape)
        prediction = loaded_model.predict(testimage).astype(float)
        print(prediction)
        return { 'classification': { 'cat': prediction[0][0], 'dog' : 1-prediction[0][0]} }

def register_api(app):
    api = flask_restful.Api()

    @api.representation('application/json')
    def output_json(data, code, headers=None):
        response = flask.make_response(flask.json.dumps(data), code)
        response.headers.extend(headers or {})
        return response

    api.add_resource(CatDog, '/predict')
    api.init_app(app)
