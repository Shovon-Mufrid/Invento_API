import django_filters
from django.contrib.auth.models import Group
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser, AllowAny
from Software_Settings import serializers, permissions, models
from django.contrib.admin.models import LogEntry
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission
import django_filters
from django.db.models import Q
from django.forms.models import model_to_dict

# Create your views here.
# from Software_Settings.models import UserProfile
from HRM import serializers as hrm_Serializer
from HRM.models import Employee, Designation

# sessionout
from django.http import JsonResponse
from django.utils import timezone
# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handel creating and updating users"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        Employee_res = Employee.objects.get(employee=user)
        employee_serializer = hrm_Serializer.EmployeeSerializer(Employee_res)
        permissions_data = ""
        if Employee_res.Designation:
            permissions = Designation.objects.get(
                id=Employee_res.Designation.id)
            permissions_data = hrm_Serializer.DesignationSerializer(
                permissions).data
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            "phone": Employee_res.phone,
            "superuser": user.is_superuser,
            "staff": user.is_staff,
            "profile": employee_serializer.data,
            "permissions": permissions_data['approved_permissions_list'],
        })

class moduleViewSet(viewsets.ModelViewSet):
    """Handel creating and updating users"""
    serializer_class = serializers.moduleSerializer
    queryset = models.module.objects.all()
    authentication_classes = (TokenAuthentication,)


class sub_moduleViewSet(viewsets.ModelViewSet):
    """Handel creating and updating users"""
    serializer_class = serializers.sub_moduleSerializer
    queryset = models.sub_module.objects.all()
    authentication_classes = (TokenAuthentication,)
