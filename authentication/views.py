from authentication.models import User
from authentication.serializers import SignUpSerializers
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from authentication.hashers import MyBcrypt, ParameterCheckers
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken 




# Create your views here.

        
class SignUp(APIView):

    def post(self,request):
        user = SignUpSerializers(data=request.data)

        if user.is_valid() and user.validated_data['password'] == user.validated_data['password2']:
            user.save(user=request.data)
            return Response({"success":"success","data":user.data})
            # ,"refresh":str(RefreshToken),"access":str(RefreshToken.access_token)})
        else:
            return Response({"error":"error","data":user.data})


class LogIn(APIView):

    def post(self,request,*args, **kwargs):
        # user = SignUpSerializers.objects.filter()
        pass

        

class test(APIView):
    # refresh = RefreshToken.for_user(SignUp)

    # return {
    #     'refresh': str(refresh),
    #     'access': str(refresh.access_token),
    # }

    # serializer_class  = LogInSerializers

    # def post(self,request):

    #     # email = self.kwargs['email']
    #     # password = self.kwargs['password']

    #     # print(email)
    #     # print(password)
    #     # print(request.data)
    #     details = request.data
    #     # return Response(details)

    #     # value = User.objects.filter(email=details['email']).values()
    #     # print(value)
    #     # return JsonResponse(value)

    #     queryset = User.objects.filter(email=details['email']).values()
    #     # queryset = User.objects.filter(password=details['password'])
    #     print(queryset)
    #     return HttpResponse(queryset)
            # return HttpResponse({"data":details.data})


    pass

    # print(User.objects.filter(email='frfdfa@gmail.com'))
    # print(User.objects.name)
    
        
        



