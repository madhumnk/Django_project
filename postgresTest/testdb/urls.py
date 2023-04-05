from django.urls import path
from .views import get_surname
from .views import RegisterView, LoginView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('get-surname/<str:name>/', get_surname, name='get_surname')
]
