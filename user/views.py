import random
import string
import secrets

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from django.conf import settings
from user.forms import CreateUserForm, ResetUserPasswordForm
from user.models import User


class UserRegisterView(CreateView):
    template_name = 'user/user_form.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        verification_link = f'http://{host}/user/email_confirm/{token}/'
        subject = 'Подтверждение почты'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, verification_link, from_email, recipient_list)
        return super().form_valid(form)


def email_confirm(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse_lazy("user:login"))


class PasswordResetView(FormView):
    template_name = 'password_reset.html'
    form_class = ResetUserPasswordForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            user.is_active = True
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            user.password = make_password(new_password)
            user.save()

            subject = 'Сброс пароля.'
            message = f'Ваш новый пароль был сгенерирован автоматически:\n {new_password}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
        except User.DoesNotExist:
            form.add_error('email', 'Пользователь с таким адресом электронной почты не найден.')

        return super().form_valid(form)
