
#  description: 'Objetos Arrays y variables'

class Message:
    def __init__(self, success="False", message="Faltan datos", data=None):
        self.success = success
        self.message = message
        self.data = data

    def show(self):
        return dict(vars(self), success=self.success, message=self.message, data=self.data)


resMessage = {
    'success': False,
    'message': "Faltan datos"
}

errors = {'mail': 'El email es incorrecto',
          'mailUnavalible': 'El email ya existe en nuestra base de datos',
          'password': 'El Password es incorrecto',
          'name': 'Nombre incorrecto',
          'noUser': 'El Usuario no existe en el sistema',
          'session': 'Sesión invalida',
          'denied': 'Permisos insuficientes',
          'estatus': 'tu cuenta esta desabilitada'}

success = {
    'login': "sesión exitosa",
    'verified': "sesión verificada",
    'logout': "sesión cerrada"
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
