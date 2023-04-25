from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from todolist.serializers import TodoListSerializer, TodoCreateSerializer, TodoUpdateSerializer
from todolist.models import Todo


# Create your views here.
class TodoListView(APIView):
    def get(self, request):
        todo_list = Todo.objects.all()
        serializer = TodoListSerializer(todo_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"message": "로그인 해주세요"}, 401)
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailView(APIView):
    def get(self, request, todolist_id):
        todo = get_object_or_404(Todo, id=todolist_id)
        serializer = TodoListSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, todolist_id):
        todo = get_object_or_404(Todo, id=todolist_id)
        if not request.user == todo.user:
            return Response({"message": "권한이 없습니다."}, 403)
        serializer = TodoUpdateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, todolist_id):
        todo = get_object_or_404(Todo, id=todolist_id)
        if not request.user == todo.user:
            return Response({"message": "권한이 없습니다."}, 403)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
