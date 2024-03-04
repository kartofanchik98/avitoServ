from django.http import HttpResponse
  
def index(request):
    return HttpResponse("Главная")
 
def about(request):
    return HttpResponse("О сайте")
 
def contact(request):
    return HttpResponse("Контакты")
	
def user(request, name, age):
    return HttpResponse(f"<h2>Имя: {name}  Возраст:{age}</h2>")
	
