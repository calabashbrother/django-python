from django.http import HttpResponse
from django.template.response import TemplateResponse
import datetime
def hello(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")
    name = {'name': 'zhang'}
    return TemplateResponse(request, 'hello.html', locals())