from rest_framework import serializers
from django.utils import timezone
from todolist.models import Todo


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title',]


class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'is_complete',]

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     instance.title = validated_data.get('title', instance.title)
    #     if validated_data.get('is_complete') == True:
    #         instance.is_complete = True
    #         instance.completion_at = timezone.now()
    #     else:
    #         instance.is_complete = False
    #         instance.completion_at = None
    #     instance.save()
    #     return instance
