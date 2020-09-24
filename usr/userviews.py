from django.shortcuts import render
from .models import Usuario
from django.utils import timezone
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils2.validations import checkNull, checkLength, checkPassword, checkEmail
import bcrypt


class Message:
    def __init__(self, success="False", message="Faltan datos", data=None):
        self.success = success
        self.message = message
        self.data = data

    def show(self):
        return dict(vars(self), success=self.success, message=self.message, data=self.data)


def validate(d, edit):
    f = {'id_rol', 'id_estatus', 'nombre', 'email', 'password', 'telefono', 'uuid'} if edit else {
        'id_rol', 'id_estatus', 'nombre', 'email', 'password', 'telefono'}
    full_request = d.keys() >= f

    if (full_request != True):
        m = Message()
        return m

    if (checkNull(d['nombre']) or checkLength(d['nombre'], 2, 50)):
        m = Message(message="El usuario es incorrecto")
        return m

    if (checkPassword(d['password'])):
        m = Message(message="La contraseña es incorrecta")
        return m

    if (checkEmail(d['email'])):
        m = Message(message="El email es incorrecto")
        return m

    m = Message(success=True)
    return m


@csrf_exempt
def nuevo_usuario(request):
    if request.method == 'POST':
        d = request.POST

        valid = validate(d, False)
        if(valid.success != True):
            return JsonResponse(valid.show())

        # espacio de validaciones
        userExists = Usuario.objects.filter(email=d['email']).first()
        # check if user exists
        if(userExists):
            print("El correo ya se encuentra")
            m = Message(
                message="El correo ya se encuentra en nuestra base de datos")

            return JsonResponse(m.show())
        else:
            dummy = 'https://www.worldfuturecouncil.org/wp-content/uploads/2020/02/dummy-profile-pic-300x300-1.png'
            passwd = d['password'].encode()
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(passwd, salt)
            foto = d['fotografia'] if hasattr(d, 'fotografia') else dummy
            # let hash = bcrypt.password passw something with bcrypt for password
            u = Usuario(nombre=d['nombre'],
                        password=hashed,
                        email=d['email'],
                        telefono=d['telefono'],
                        fotografia=foto,
                        id_rol=d['id_rol'],
                        id_estatus=d['id_estatus'],
                        onboard=False,
                        createdAt=timezone.now(),
                        updatedAt=timezone.now())
            u.save()
            # salt = bcrypt.gensalt()
            # hashed = bcrypt.hashpw(passwd, salt)
            # if bcrypt.checkpw(passwd, hashed):
            # print("match")
            # else:
            # print("does not match")
            m = Message(
                success=True,
                data=u.id,
                message="Usuario creado exitosamente")

            return JsonResponse(m.show())


@csrf_exempt
def eliminar_usuario(request):
    if request.method == 'POST':
       id =  request.POST.get('uuid')
       print(id)
       if(id):
           userExists = Usuario.objects.filter(id = id).first()
           if(userExists):
               userExists.delete()
               m = Message(
                success=True,
                data= {"nombre":userExists.nombre,'id':userExists.id, 'email':userExists.email},
                message="Usuario eliminado exitosamente")
               return JsonResponse(m.show())
           else:
               m = Message(message="Usuario no existe en la base de datos")
               return JsonResponse(m.show())
       else:
            m = Message()
            return JsonResponse(m.show())
               


@csrf_exempt
def editar_usuario(request):
    if request.method == 'POST':
        d = request.POST
        valid = validate(d, True)

        if(valid.success != True):
            return JsonResponse(valid.show())

        userExists = Usuario.objects.filter(id=d['uuid']).first()
        print(userExists)
        # check if user exists
        if(not userExists):
            print("El Usuario no existe")
            m = Message(
                message="El Usuario no existe")

            return JsonResponse(m.show())
        else:
            dummy = 'https://www.worldfuturecouncil.org/wp-content/uploads/2020/02/dummy-profile-pic-300x300-1.png'
            passwd = d['password'].encode()
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(passwd, salt)
            foto = d['fotografia'] if hasattr(d, 'fotografia') else dummy
            # revisar bien  lo del rehash de la contraseña creo que es necesario un nuevo controller
            userExists.nombre = d['nombre']
            userExists.password = hashed
            userExists.email = d['email']
            userExists.telefono = d['telefono']
            userExists.fotografia = foto
            userExists.id_rol = d['id_rol']
            userExists.id_estatus = d['id_estatus']
            userExists.updatedAt = timezone.now()
            # timezone.now() no cuenta los segundos
            userExists.save()

            m = Message(
                success=True,
                data=userExists.id,
                message="Usuario actualizado  exitosamente")

            return JsonResponse(m.show())


@csrf_exempt
def ver_usuario(request):
    if request.method == 'GET':
        id = request.GET.get('uuid')
        print( id)
        if(id == False): 
            m = Message()
            return JsonResponse(m.show())
            
        userExists = Usuario.objects.filter(id = id).values()
        print(userExists)
        if(userExists):
            m = Message(
                success=True,
                data=list(userExists),
                message="Usuario obtenido exitosamente")
            return JsonResponse(m.show())
        else:
            m = Message(message="Usuario no encontrado")
            return JsonResponse(m.show())


@csrf_exempt
def ver_usuarios(request):
    if request.method == 'GET':
        usersExists = Usuario.objects.values().order_by('id')
        if usersExists:
            m = Message(
                success=True,
                data=list(usersExists),
                message="Usuarios obtenidos exitosamente")
            return JsonResponse(m.show())
        else:
            m = Message(
                message="No encontramos usuarios en la base de datos")
            return JsonResponse(m.show())
            
