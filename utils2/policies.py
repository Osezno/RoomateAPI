from .validations import checkNull, checkLength, checkPassword, checkEmail
from .catalogs import errors, resMessage, Message,estatus
from .general import checkUser, checkUserById
from django.conf import settings
import bcrypt
import jwt


def login_p(data):
    f = {'email', 'password'}

    full_request = data.keys() >= f

    if (full_request != True):
        m = Message()
        return m
    elif (checkEmail(data['email'])):
        m = Message(message=errors['mail'])
        return m
    elif (checkPassword(data['password'])):
        m = Message(message=errors['password'])
        return m

    userExists = checkUser(data['email'])
    
    if (not userExists):
        
        m = Message(message= errors['noUser'])
        return m
    
    # if(data['email'] == "test@test.com"):
    #       print('entro')
    #       m = Message(success=True)
    #       return m
      
      
    match = bcrypt.checkpw(data['password'].encode(), userExists.password.encode())
    print("match",match)

    if (match):
        m = Message(success=True)
        return m
    else:
        m = Message(message=errors['password'])
        return m


def check_session(data, rol):
    f = {'token', 'uuid'}
   
    full_request = data.keys() >= f
    
    if (full_request != True):
        m = Message()
        return m
    #verify token
    session = jwt.decode(data['token'], settings.SECRET_KEY, algorithm='HS256')
    #verify user
    user = checkUserById(data['uuid'])
   
    #validate
    if(user and user.id_estatus == estatus['activo'] and user.ses_id == session['user_id'] and user.id_rol in rol): 
        m = Message(success= True)
    # find error
    elif (not user):  
        m = Message(message= errors['noUser'])
    elif (user.ses_id != session['user_id']):
        m = Message(message= errors['session'])
    elif(user.id_estatus != estatus['activo']):
        m = Message(message= errors['estatus'])       
    elif(user.id_rol not in rol):
        m = Message(message= errors['denied'])
    
    return m
