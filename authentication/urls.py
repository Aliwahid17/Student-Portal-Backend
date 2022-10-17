from django.urls import path
from authentication.views import SignUp,test


app_name = 'Authentication'


urlpatterns = [
    path('signup/', SignUp.as_view(), name='Signup'),
    # path('login/', Login.as_view(), name='Login'),
    path('test/', test.as_view(), name='test'),
]

