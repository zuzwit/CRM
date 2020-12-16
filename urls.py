from django.urls import path
from .views import users_list, registration, home, users_list, login, test

app_name='contacts'
urlpatterns=[
	path('users/', users_list),
	path('home/', home.as_view()),
	path('register/', registration.as_view()),
	path('login/', login.as_view()),
]
