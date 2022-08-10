
from turtle import title
from dropship import models
from rest_framework import serializers
from django.shortcuts import render, redirect  


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = "__all__"

    
class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Member
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):

        user = models.User.objects.create_user(
            validated_data['email'], validated_data['email'], validated_data['password'])

        member = models.Member.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            user=user
        )
        return member



class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Label
        fields = "__all__"

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue         
        fields = "__all__"

class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Sprint
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = "__all__"