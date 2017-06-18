from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View, generic

from .forms import UserForm
from .models import CarPhoto


class IndexView(generic.ListView):
    template_name = 'carstagram/index.html'
    context_object_name = 'latest_carphoto_list'

    def get_queryset(self):
        return CarPhoto.objects.order_by('-pub_date')[:5]


class UserFormView(View):
    form_class = UserForm
    template_name = 'carstagram/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('carstagram:index')

        return render(request, self.template_name, {'form': form})
