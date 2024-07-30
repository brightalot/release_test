# from .models import Student
# from rest_framework.views import APIView
# from django.shortcuts import render

# from .serializers import StudentSerializer
# from rest_framework.response import Response

# # Create your views here.
# class Students(APIView):
#     def get(self, request):
#         #모든 학생들 정보 가져오기
#         all_students = Student.objects.all()
#         #json 형식으로 전달하자...
#         #시리얼라이즈
#         serializer = StudentSerializer(all_students)

#         return Response(serializer.data)

#     def post(self, request):
#         pass

from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT

# Create your views here.
class Students(APIView):

    def get(self, request):
        all_students = Student.objects.all()
        serializer = StudentSerializer(all_students, many=True)
        return Response(serializer.data)

        
    def post(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data)
        else:
            return Response(student.errors)
        

class StudentDetail(APIView):
    def get_object(self, code):
        try:
            student = Student.objects.get(code=code)
        except:
            raise NotFound
        return student
    
    def get(self, request, code):
        student = self.get_object(code)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, code):
        student = self.get_object(code)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self, request, code):
        student = self.get_object(code)
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)