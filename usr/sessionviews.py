from django.shortcuts import render
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
from utils2.catalogs import Message, success, rol, resMessage
from utils2.general import genId
from utils2.policies import login_p, check_session
from django.http.response import JsonResponse
from django.conf import settings
import jwt




# ver implementacion de policies con roles




def crear_token(ses_id, secret, expiracion):
    payload = {
        'user_id': ses_id,
    }
    jwt_token = jwt.encode(payload, secret, algorithm='HS256').decode('utf-8')
    return jwt_token


def login(request):
    if request.method == 'POST':
        d = request.POST
        auth = login_p(d)
        if(auth.success != True):
            return JsonResponse(auth.show())
        # crear un nuevo session id para el usuario y actualizarlo
        ses_id = genId()
        # crear token
        token = crear_token(ses_id, settings.SECRET_KEY, "365d")
        print("token",token)
        # actualizar el id de sesion en el usuario
        u = Usuario.objects.filter(email=d['email']).first()
        u.ses_id = ses_id
        u.save()
        # send sesion to the front
        data = {
            'token': token,
            'onboard': u.onboard,
            'id_rol': u.id_rol,
            'id_estatus': u.id_estatus,
            'uuid': u.id
        }

        respuesta = Message(success=True, message=success['login'], data=data)
        return JsonResponse(respuesta.show())

def logout(request):
    if request.method == 'POST':
        auth = check_session(request.headers, rol['associate'])
        
        if(auth.success != True):
            return JsonResponse(auth.show())
        
        d = request.POST
        respuesta = resMessage
        
        f = {'uuid'}
        full_request = d.keys() >= f
        
        if (full_request != True):
            return JsonResponse(respuesta)

        u = Usuario.objects.filter(id=d['uuid']).first()
        u.ses_id = ''
        u.save()
        respuesta['success'] = True
        respuesta['message'] = success['logout']

        return JsonResponse(respuesta)
