from django.http import HttpResponse
from django.template.response import TemplateResponse
import datetime
from mysite.models import User

def hello(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = {'name': 'zhang'}
    user = User()
    user.user_name = 'username'
    user.user_id = 'user_id'
    user.email = 'email@email.com'
    user.cellphone = '123456789098'
    user.save()
    # request =' %s', % (request)
    host = request.get_host()
    return TemplateResponse(request, 'hello.html', locals())