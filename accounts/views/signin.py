from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from accounts.forms import SignInForm

class SignInView(View):
    template_name = 'accounts/signin.html'
    form_class = SignInForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        contex = {'form': forms}
        return render(request, self.template_name, contex)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            email = forms.cleaned_data['email']
            password = forms.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('kalevent:calendar')
        context = {'form': forms}
        return render(request, self.template_name, context)