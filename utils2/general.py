import random
import string
from usr.models import Usuario



def genId(chars = string.ascii_uppercase + string.digits, N=12):
    return ''.join(random.choice(chars) for _ in range(N))
    
def checkUser(email):
    user = Usuario.objects.filter(email=email).first()
    print(user)
    return user

def checkUserById(id):
    user = Usuario.objects.filter(id=id).first()
    print(user)
    return user
