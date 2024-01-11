from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer, RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User

# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class UserRegistrationView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print("token", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print('uid', uid)
            # print("url", f"http://127.0.0.1:8000/activate/{uid}/{token}/")
            # confirm_link = f"http://127.0.0.1:8000/activate/{uid}/{token}/"
            # confirm_link = f"http://127.0.0.1:8000/patient/activate/{uid}/{token}/"
            # print("url", f"http://127.0.0.1:8000/patient/active/{uid}/{token}/")
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}/"
            email_subject = "Activate your account"
            email_body = render_to_string(
                'patient/email_templates/confirm_link.html', {'confirm_link': confirm_link}
            )
            email = EmailMultiAlternatives(subject=email_subject, body=email_body, to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            # serializer.save()
            # return Response("Form done")
            return Response("Check your email and activate your account.")
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)


# def activate(request, uidb64, token):
def activate(request, uid64, token):
    print("uid", uid64, 'token', token)
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        # user = User.objects.get(pk=uid)
        user = User._default_manager.get(pk=uid)
        
    # except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    except(User.DoesNotExist):
        user = None
    print('uid', uid, 'user', user)

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return redirect("register")
    else:
        # return HttpResponse('Activation link is invalid!')
        return redirect("register")
