from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Patient
from .serializers import PatientSerializer, RegistrationSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
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
            confirm_link = f"http://127.0.0.1:8000/patient/activate/{uid}/{token}/"
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


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
    # except (User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return redirect('login')
        # return redirect('register')
    else:
        return redirect('register')


class UserLoginView(APIView):
    def post(self, request):
        print("request.data", request.data)
        print("self.request.data", self.request.data)
        # serializer = UserLoginSerializer(data=request.data)
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                print("created", created)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid credentials'})
        
        return Response(serializer.errors)

class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')