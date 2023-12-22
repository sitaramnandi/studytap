from django.shortcuts import render,redirect
from api.serializers import studentSerializer
from rest_framework.generics import ListAPIView
from api.models import student
from api.form import StudentForm
# from api.form import 
# Create your views here.
class StudentList(ListAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

def insert_data(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/display")
            
    return render(request,"api/insert.html",{"form":form})

def display(request):
    student_lst=student.objects.all()
    return render(request,"api/display.html",{"student_lst":student_lst})


def delete_view(request,id):
    st=student.objects.get(id=id)
    st.delete()
    return redirect("/display")

def upadte_view(request,id):
    Student=student.objects.get(id=id)
    form=StudentForm(instance=Student)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=Student)
        if form.is_valid():
            
            form.save()
            return redirect("/display")

    return render(request,"api/update.html",{"form":form})



