from django.shortcuts import render
from .models import Usuario
from django.views.decorators.csrf import csrf_exempt
from utils2.catalogs import Message, errors, success, rol, resMessage, app_info
from utils2.validations import checkEmail,checkPassword
from utils2.general import genId, checkUser, enviar_mail, checkUserById, recovery_url
from utils2.policies import login_p, check_session
from django.http.response import JsonResponse
from django.conf import settings
from django.template.loader import render_to_string
import jwt
import bcrypt


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
            'uuid': u.uuid
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


def forgot_password(request):
    if request.method == 'POST':
        respuesta = resMessage
        email = request.POST.get('email')
        if (not email):
            return JsonResponse(respuesta)

        if(checkEmail(email)):
            respuesta['message'] = errors['mail']
            return JsonResponse(respuesta)

            # crear un nuevo session temp
        user = checkUser(email)

        if(not user):
            respuesta['message'] = errors['noUser']
            return JsonResponse(respuesta)

        tmp_id = genId()
        # crear token
        token = crear_token(tmp_id, settings.SECRET_KEY, "1d")

        user.tmp_password = tmp_id
        user.save()
        # hacer un token jwt?

        url = recovery_url(token, user.uuid)

        mailObj = {
            'url': url,
            'name': user.nombre,
            'domain': app_info['domain'],
            'slogan': app_info['slogan'],
            'logo': app_info['logo']
        }

        msg_html = render_to_string('emails/forgot_pwd.html', mailObj)

        enviar_mail("Liga para resetear contraseña", msg_html, [user.email])
        # enviar correo con liga
        respuesta['success'] = True
        respuesta['message'] = success['emailSend']
        return JsonResponse(respuesta)


def change_password(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        uuid = request.POST.get('uuid')
        password = request.POST.get('password')
        respuesta = resMessage

        if (not token or not uuid or not password):
            return JsonResponse(respuesta)

        if(checkPassword(password)):
            respuesta['message'] = errors['passwordReq']
            return JsonResponse(respuesta)
        
        user = checkUserById(uuid)

        if(not user):
            respuesta['message'] = errors['noUser']
            return JsonResponse(respuesta)
        
        session = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
        
        
        if(user.tmp_password != session['user_id']):
            respuesta['message'] = errors['recovery']
            return JsonResponse(respuesta)

        passwd = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(passwd, salt)

        user.password=hashed.decode('utf8')
        user.save()
        respuesta['success'] = True
        respuesta['message'] = success['recovery']
        return JsonResponse(respuesta)


