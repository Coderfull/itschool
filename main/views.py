from django.shortcuts import render
from .models import MyUser,Student,Yunalishlar
# Create your views here.
def MainView(request):
    assistantlar = MyUser.objects.filter(role__exact ="assistant")

    return render(request, "index.html",{"assistantlar":assistantlar})

def CreateStudentView(request):
    if request.method == 'POST':
        new_student = Student(
            ismi = request.POST['inputName'],
            familya = request.POST['familya'],
            yunalish = request.POST['yunalish'],
            vaqt = request.POST['vaqt'],
            kun=request.POST['kun'],
            telefon=request.POST['phone']
        )
        new_student.save()

    yunalishlar = Yunalishlar.objects.all()
    return render(request, "create_student.html", {"yunalishlar": yunalishlar})
