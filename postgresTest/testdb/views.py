from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from rest_framework.views import APIView

# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
       
        if user:
            
            serializer = UserSerializer(user)
            print(serializer.data)
            data = {'user': serializer.data["last_name"] }

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



    



def get_surname(request, name):
    # Define a dictionary of names and surnames
    name_surname_dict = {'Madhu': 'Kumawat', 'Mayank': 'Sherwani', 'Govindh': 'Arunachalam', 'Meherzad': 'Chinoy', 'Jeya': 'Suriya'}
    
    # Check if the name is in the dictionary
    if name in name_surname_dict:
        # Return the surname as a JSON response
        return JsonResponse({'surname': name_surname_dict[name]})
    else:
        # Return an error message as a JSON response
        return JsonResponse({'error': f"No surname found for name '{name}'"})



