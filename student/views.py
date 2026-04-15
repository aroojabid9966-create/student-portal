from django.shortcuts import render,redirect
from .models import Student
def home(request):
    query=request.GET.get('q')
    if query:
        std=Student.objects.filter(name__icontains=query)
    else:
        std=Student.objects.all()
    return render(request,'student.html',{'std':std})
def std_detail(request,id):
    std=Student.objects.get(id=id)
    return render(request,'student_detail.html',{'std':std})
def add_std(request):
    if request.method == "POST":
        name=request.POST.get('name')
        roll_num=request.POST.get('roll_num')
        course=request.POST.get('course')
        age=request.POST.get('age')
        email=request.POST.get('email')
        address=request.POST.get('address')
        Student.objects.create(
            name=name,
            roll_num=roll_num,
            course=course,
            age=age,
            email=email,
            address=address



        )
        return redirect('home')
    return render(request,'add_student.html')
    
    


    

