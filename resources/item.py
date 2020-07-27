from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from flask import request
from models.item import ItemModel

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This Field Cannot Be Empty!"
    )

    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store id!"
    )


    @jwt_required()
    def get(self,name):
        item=ItemModel.find_by_name(name)
        if ItemModel.find_by_name(name):
            return item.json()
        return {'message':"Item Does not exists"},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':'An item with this name already exists'},400

        request_data=Item.parser.parse_args()

        item=ItemModel(name, request_data['price'],request_data['store_id'])

        try:
            item.save_to_db()
        except:
            return {"message":"An Error Occured while inserting an item!"},500 #internal server error
        
        return item.json(),201

    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.del_from_db()
        
        return {'message':'Item Deleted'}

    def put(self,name):
        request_data=parser.parse_args()
        
        item=ItemModel.find_by_name(name)

        if item is None:
            item=ItemModel(name,request_data['price'],request_data['store_id'])
        else:
            item.price=request_data['price']

        item.save_to_db()
        return item.json()



class Items(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]}
