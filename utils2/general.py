import random
import string
from usr.models import Usuario
from django.core.mail import send_mail
from .catalogs import app_info
from .firebase import db, storage
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import storage

# cred = credentials.Certificate('path/to/serviceAccountKey.json')
# firebase_admin.initialize_app(cred, {
#     'storageBucket': '<BUCKET_NAME>.appspot.com'
# })


def genId(chars=string.ascii_uppercase + string.digits, N=12):
    return ''.join(random.choice(chars) for _ in range(N))


def checkUser(email):
    user = Usuario.objects.filter(email=email).first()
    return user


def checkUserById(id):
    user = Usuario.objects.filter(uuid=id).first()
    return user


def recovery_url(pwd, uuid):
    string = '{url}recovery?tmp={pwd}&id={uuid}'.format(
        url=app_info['domain'], pwd=pwd, uuid=uuid)
    return string


def enviar_mail(subject, body, mails):
    send_mail(subject=subject, message='hola como estas', from_email=app_info['mail'],
               recipient_list=mails,  html_message=body)
   
    
    return False


def file_upload(blob, imageId, user_id):
    if (not imageId):
        imageId = genId()

    # upload = storage.ref('assets/img/${imageId}').put(blob)
    # upload.on('state_changed', snapshot => {
    #     console.log("entra")
    # }, error => {
    #         console.log('error', error);
    # }, () => {
    #     upload.snapshot.ref.getDownloadURL().then(url => {
    #         res(url);
    #         });
    #     });
    # }


def add_notification(user_id):

    liga = '/{user_id}/'.format(user_id=user_id)

    data = db.child(liga).shallow().get().val()
    
    if (data):
        #remove first seen notifications 
        data = db.child(liga).child("notificaciones").get().val()
        data.append({"mensaje": "test", "url": '', "creado": "jueves", "visto": False})
        result = db.child(liga).update({"notificaciones":data})
        return result
    else:
        # add the actual notification
        result = db.child(liga).update({"notificaciones": [
            {"mensaje": "test", "url": '', "creado": "jueves", "visto": False}]}
        )

        return result

  