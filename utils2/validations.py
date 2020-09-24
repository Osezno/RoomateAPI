
    # 'Validacion de formularios',
    # 'Revisar valores vacios.',
import re


def checkNull(string):
    if not string:
        return True
    else:
        return False


def checkLength(x, minus, max):
    if len(x) < minus or len(x) > max:
        return True
    else:
        return False


def checkPassword(password):
    regex = '[A-Za-z0-9]{8,}'
    if not re.search(regex, password) or checkLength(password, 8, 30) or checkNull(password):
          return True
    else:
          return False


def checkEmail(email):
    reg = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    if not re.search(reg , email) or checkLength(email, 8, 30) or checkNull(email):
          return True
    else:
          return False 
    
   
    
    
