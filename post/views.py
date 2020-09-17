from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
 

# Create your views here.
@csrf_exempt
def create_post(request):    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        print(title,content)
        if (title != None and content != None):
            print("Entro")
            p = Post(title= title, content=content, created=timezone.now(), modified=timezone.now())
            p.save()
            return JsonResponse({"success": True,
                     "data": { "id": p.id, "title":title , "content":content},
                     "mensaje": "Post creado exitosamente",
               })
        else:
            return JsonResponse({"success": False,
                     "data": None,
                     "mensaje":"Error"
               })
    