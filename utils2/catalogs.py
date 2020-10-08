
#  description: 'Objetos Arrays y variables'

class Message:
    def __init__(self, success="False", message="Faltan datos", data=None):
        self.success = success
        self.message = message
        self.data = data

    def show(self):
        return dict(vars(self), success=self.success, message=self.message, data=self.data)


app_info = {
    'logo': "goodCode.png",
    'slogan': "Lorem ipsum Dolor Amet",
    'domain': "https://localhost:3000/",
    'mainColor': "#3498db",
    'mail': "postmaster@sandboxb7c0a2ee1196468993ae2c09b63eccd5.mailgun.org"
}

resMessage = {
    'success': False,
    'message': "Faltan datos"
}

errors = {'mail': 'El email es incorrecto',
          'mailUnavalible': 'El email ya existe en nuestra base de datos',
          'password': 'El Password es incorrecto',
          'passwordReq': 'El Password no es seguro',
          'name': 'Nombre incorrecto',
          'noUser': 'El Usuario no existe en el sistema',
          'session': 'Sesión invalida',
          'denied': 'Permisos insuficientes',
          'estatus': 'tu cuenta esta desabilitada',
          'recovery': 'Tu token expiro o es incorrecto',
          'serverError': 'Estamos experimentando problemas, nuestros tecnicos estan trabajando para resolverlos.'
          }

success = {
    'login': "Sesión exitosa",
    'verified': "Sesión verificada",
    'logout': "Sesión cerrada",
    'userCreated': "Usuario creado exitosamente",
    'userDeleted':"Usuario borrado exitosamente!",
    'userUpdated': "¡Usuario actualizado exitosamente!",
    'recovery': "Contraseña actualizada.",
    'getUser':"Usuario obtenido exitosamente",
    'emailSend': "¡Correo enviado! revisa tu bandeja "
}

rol = {
    'admin': [1],
    'manager': [1, 2],
    'associate': [1, 2, 3],
}

estatus = {
    'activo': 1,
    'pendiente': 2,
    'suspendido': 3,
    'elminiado': 4,
}
