
from reactapiapp.serializers import loginserializer
from reactapiapp.models import Loginmodel
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class loginviewsets(viewsets.ModelViewSet):
    queryset=Loginmodel.objects.all()
    serializer_class=loginserializer

@csrf_exempt
def signinview(request,id=0):
    
    authdata=Loginmodel.objects.all()
    authserializer=loginserializer(authdata,many=True)

    if request.method=='GET':
        return JsonResponse(authserializer.data,safe=False)
    
    if request.method=='POST':
        authparseddata=JSONParser().parse(request)
        
        userreq=authparseddata['username']
        pswdreq=authparseddata['password']
        print(type(userreq))
        objdb=list(Loginmodel.objects.filter(username=userreq).values())
        print(objdb)
        if(len(objdb)!=0):
            pswddb=objdb[0]['password']
            print(pswddb)
            print(userreq)
            print(pswdreq)
            if pswddb==pswdreq:
                return JsonResponse("Authentication Successful",safe=False)
            else:
                return JsonResponse("Username or Password is Incorrect",safe=False)
        else:
            return JsonResponse("Username or Password is Incorrect",safe=False)
        
