from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from .models import User


# Create your views here.

class UserView(APIView):
    def get(self, request):
        token = request.META.get('AUTHORIZATION')
        if token is None or token == '':
            return JsonResponse({
                'code': '0002',
                'msg':'未认证的请求'
            })
        users = User.objects.all().values()
        return JsonResponse({
            "code":"0000",
            "msg":"操作成功",
            "data": list(users)
        })

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        name = request.POST.get('name')
        if not username or not password or not name or not name or not password2:
            return JsonResponse({
                "code":"0001",
                "msg":"缺少必要参数",
                "data":[]
            })
        if password != password2:
            return JsonResponse({
                "code":"U001",
                "msg":"两次密码不一致"
            })

        try:
            user = User(username=username, password=password, name=name).save()
        except Exception as e:
            return JsonResponse({
                "code":"U002",
                "msg":"添加用户失败"
            })
        return JsonResponse({
            "code":"0000",
            "msg":"操作成功"
        })

    def put(self, request):
        pass

    def delete(self, request):
        pass

class LoginView(APIView):
    def get(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        if not username or not password:
            return JsonResponse({
                "code":"0001",
                "msg":"缺少必要参数",
                "data": []
            })
        user = User.objects.filter(username=username, password=password).first()
        if not user:
            return JsonResponse({
                "code":"L001",
                "msg":"用户名或密码不匹配"
            })
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        pay_load = jwt_payload_handler(user)
        token = jwt_encode_handler(pay_load)
        return JsonResponse({
            "code":"0000",
            "msg":"操作成功",
            "data": token
        })



