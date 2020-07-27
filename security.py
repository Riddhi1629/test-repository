from models.user import UserModel
# users=[
#     User(1,'Riddhi','1234')
# ]

# user_mapping={u.username : u for u in users}

# user_id_mapping={u.id : u for u in users}
   
def authenticate(username,password):
    user=UserModel.find_by_name(username)
    # user=user_mapping.get(username,None)
    if user and user.password==password:
        return user

def identity(payload):
    id=UserModel.find_by_id(payload['identity'])
    # user_id=payload['identity']
    return id