#! usr/bin/env python3
from mysite.models import User
from django.template.response import TemplateResponse
def userlist(request):
    userlist = User.objects.values()
    return TemplateResponse(request, 'userlist.html', locals())
