from django.http import HttpResponse
from django.template.response import TemplateResponse
import datetime
def hello(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = {'name': 'zhang'}
    # request =' %s', % (request)
    host = request.get_host()
    return TemplateResponse(request, 'hello.html', locals())