from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from .forms import UsersForm
from django.core.paginator import Paginator
from django.views.generic import CreateView, TemplateView, ListView

# Create your views here.

class home(TemplateView):
    template_name = 'contacts/home.html'

def users_list(request):

    u_list = Users.objects.order_by('surname')
    paginator = Paginator(u_list, 5)
    page = request.GET.get('page')
    u_list = paginator.get_page(page)

    form=UsersForm
    if request.method == 'POST':
        form = UsersForm(request.POST or None)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_surname = form.cleaned_data['user_surname']
            user_dateOfBirth = form.cleaned_data['user_dateOfBirth']
            user_login = form.cleaned_data['user_login']

            user = Users(name=user_name, surname=user_surname, dateOfBirth=user_dateOfBirth, login=user_login)
            user.save()
        else:
            form=UsersForm()

    return render(request, 'contacts/users_list.html', {'u_list': u_list, 'form': form})

class login(CreateView):
    model = Users
    template_name = 'contacts/login.html'
    success_url = 'http://localhost:8000/users/'
    fields = [
            'login',
            'password',
        ]

class registration(CreateView):
    model = Users
    template_name = 'contacts/register.html'
    success_url = 'http://localhost:8000/login/'
    fields = [
            'name',
            'surname',
            'dateOfBirth',
            'login',
            'password',
        ]


class test(ListView):
    model = Users
    
    fields = [
            'name',
            'surname',
            'dateOfBirth',
            'login',
        ]
