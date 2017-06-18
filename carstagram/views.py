from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserForm


class IndexView(View):
    template_name = 'carstagram/index.html'

    def get(self, request):
        return render(request, self.template_name)


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
