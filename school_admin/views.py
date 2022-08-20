from django.shortcuts import render, redirect
from . models import Teachers, Subject
from django.core.files.storage import FileSystemStorage


# Create your views here.


def home(request):
    return render(request, 'home.html')


def add_teacher(request):
    try:
        if request.method == "POST":
            fName = request.POST['firstName']
            lName = request.POST['lastName']
            email = request.POST['email']
            phone = request.POST['phone']
            roomNo = request.POST['roomNo']
            subjects = request.POST['subject']
            password = request.POST['password']
            subList = subjects.split(',')

            upload = request.FILES['image']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)

            
            if len(subList) < 5:
                teacher = Teachers(firstName=fName, lastName=lName, email=email, phone=phone, roomNo=roomNo, password=password, image=file_url)
                teacher.save()

                teacherObj = Teachers.objects.get(id=teacher.id)
                for i in subList:
                    subject = Subject(subject=i, teacher_id=teacherObj.id)
                    subject.save()

    except:
        msg = 'User not created'
        return render(request, 'add_teacher.html',{'msg':msg})

    return render(request, 'add_teacher.html')

    
def view_teachers(request):
    teachersObj = Teachers.objects.all()
    subjectObj = Subject.objects.all()
    return render(request, 'view_teachers.html', {'teacherData':teachersObj, 'subObj':subjectObj})


def permission(request, id):
    teachersObj = Teachers.objects.get(id=id)
    if teachersObj.permission:
        Teachers.objects.filter(id=id).update(permission=False)
    else:
        Teachers.objects.filter(id=id).update(permission=True)
    return redirect('view_teachers')
