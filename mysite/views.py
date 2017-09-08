from django.http import HttpResponse
from django.template.response import TemplateResponse
import datetime
from mysite.models import User
import json
import io
from PIL import Image, ImageDraw, ImageFont
from mysite.settings import BASE_DIR
import string, os, random
from mysite.controller.user import *
def hello(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = '%s' % ('show')

    users = User.objects.all().filter(user_name='admin').values()
    # 获取model执行的sql语句
    sql = users.query
    '''
    SELECT
    `mysite_user`.`id`,
    `mysite_user`.`user_id`,
    `mysite_user`.`user_name`,
    `mysite_user`.`email`,
    `mysite_user`.`cellphone`
    FROM
        `mysite_user`
    WHERE
        `mysite_user`.`user_name` = username
    '''
    user = User()
    user.user_name = 'admin'
    user.user_id = 'admin001'
    user.email = 'admin@demo.com'
    user.cellphone = '13500008888'
    user.password = md5('password')
    md5str = md5('123456')
    # user.save()
    # request =' %s', % (request)
    host = request.get_host()
    return TemplateResponse(request, 'hello.html', locals())

def md5(strs):
    strs = strs.encode('utf-8')
    import hashlib
    m = hashlib.md5()
    m.update(strs)
    return m.hexdigest()
def userReg(request):
    if request.method == 'POST':
        verify_code = request.session['verify_code']
        input_verify = request.POST['verify']
        returndata = {}
        # 检查验证码
        if verify_code.lower() != input_verify.lower():
            returndata = {'code': 100, 'msg': '验证码错误'}
        # 检查用户名是否存在
        userinfo = User.objects.filter(user_name=request.POST['username']).exists()
        if userinfo:
            returndata = {'code':101, 'msg': '用户名已存在'}
        if returndata:
            return HttpResponse(json.dumps(returndata),'application/json')
        user = User()
        user.user_name = request.POST['username']
        user.password = md5(request.POST['password'])
        user.save()
        returndata = {'code': 200, 'msg': '注册成功'}
        return HttpResponse(json.dumps(returndata),'application/json')
    else:
        return TemplateResponse(request, 'reg.html')
    # username = request.POST['username']
    # # return HttpResponse(username, content_type='application/json')
    # user = User.objects.filter(user_name=username)
    # if (user):
    #     return_data = {'code':100, 'msg': '此用户已存在'}
    #     json_data = json.dumps(return_data)
    #     return HttpResponse(json_data, content_type='application/json')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userinfo = User.objects.filter(user_name=username).filter(password=md5(password))
        if userinfo:
            returndata = {'code':200, 'msg':'登录成功', 'url': 'home'}
        else:
            returndata = {'code':100, 'msg': '用户名或者密码不正确'}
        returndata = json.dumps(returndata)
        return HttpResponse(returndata, content_type='application/json')
    else:
        return TemplateResponse(request, 'login.html', locals())
def home(request):
    return TemplateResponse(request, 'home.html')

def verify(request):
    '''Captcha'''
    image = Image.new('RGB', (147, 49), color = (255, 255, 255)) # model, size, background color
    font_file = os.path.join(BASE_DIR, 'static/fonts/ARIALN.TTF') # choose a font file
    font = ImageFont.truetype(font_file, 47) # the font object
    draw = ImageDraw.Draw(image)
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 4)) # The random string
    request.session['verify_code'] = rand_str
    draw.text((7, 0), rand_str, fill=(0, 0, 0), font=font) # position, content, color, font
    del draw
    request.session['captcha'] = rand_str.lower() # store the content in Django's session store
    buf = io.BytesIO() # a memory buffer used to store the generated image
    image.save(buf, 'jpeg')
    return HttpResponse(buf.getvalue(), 'image/jpeg') # return the image data stream as image/jpeg format, browser will treat it as an image
