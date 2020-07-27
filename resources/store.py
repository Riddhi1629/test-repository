from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'Store not found'},404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message':'Store Already Exists'},400
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An Error Occured'},500

    def delete(self,name):
        store=StoreModel.find_by_name(name)

        if store:
            store.del_from_db()
        return {'message': 'Store Deleted'}




class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}