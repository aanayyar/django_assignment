from dropship import models
from dropship import serializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.settings import api_settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from dropship.roles import IsAdmin, ProjectManager




class MemberModelViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'email']
    

class CustomAuthToken(ObtainAuthToken):

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        try:
            member_obj = models.Member.objects.get(user=user.pk)
        except:
            print("User Doesn't Exist")
        return Response({
            'token': token.key,
            'user_id': member_obj.pk,
            'member_id': member_obj.id,
            'email': member_obj.email,
            'first_name': member_obj.first_name,
            'last_name': member_obj.last_name,
        })
    

class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','code','owner']
    
    

class IssueModelViewSet(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','description','type','project','sprint','reportee','assignee','watchers','status']

class LabelModelViewSet(viewsets.ModelViewSet):
    queryset = models.Label.objects.all()
    serializer_class = serializers.LabelSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class SprintModelViewSet(viewsets.ModelViewSet):
    queryset = models.Sprint.objects.all()
    serializer_class = serializers.SprintSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [ProjectManager]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','description','startdate','enddate','type','project']

class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['comment','user','issue','project']


