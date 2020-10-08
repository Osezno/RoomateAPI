
from .models import Usuario
from django.utils import timezone
from django.http.response import JsonResponse
from utils2.general import add_notification, file_upload
from utils2.validations import checkNull, checkLength, checkPassword, checkEmail
from utils2.policies import check_session
from utils2.catalogs import Message, errors, success, rol, resMessage
import bcrypt


def update_profile_pic(request):
    if request.method == 'POST':
        auth = check_session(request.headers, rol['associate'])
        if(auth.success != True):
            return JsonResponse(auth.show())

        respuesta = resMessage
        uuid = request.POST.get('uuid')
        image = request.POST.get('image')
        # if (not uuid or not image):
        #  return JsonResponse(respuesta)

    if (uuid is not req.headers.uuid):
        respuesta['message'] = errors['denied']
        return JsonResponse(respuesta)

    url = file_upload(image)

    if (url):
        u = Usuario.objects.filter(id=uuid).first()
        u.fotografia = url
        u.save
        respuesta['success'] = True
        respuesta['message'] = success['userUpdated']
        return JsonResponse(respuesta)
    else:
        respuesta['message'] = errors['serverError']
        return JsonResponse(respuesta)


def notification_test(request):
    if request.method == 'POST':
        auth = check_session(request.headers, rol['associate'])
        if(auth.success != True):
            return JsonResponse(auth.show())
        
        uuid = request.POST.get('uuid')
        notification = add_notification(uuid)
        
        print(notification)
        return JsonResponse({'test': "test"})
