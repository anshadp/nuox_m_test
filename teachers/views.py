from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from school_admin . models import Teachers, Subject


# Create your views here.


def index(request):
    if request.session['userId']:
        teacherData = Teachers.objects.get(id=request.session['userId'])
        return render(request, 'index.html',{"permission":teacherData.permission})
    else:
        return redirect(request, 'index.html')    


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

    try:
        teacherData = Teachers.objects.get(email=email)
        if teacherData.email == email and teacherData.password == password:
            request.session['userId'] = teacherData.id
            return redirect('index')
        else:
            return render(request, 'login.html',{"msg":'Login Failed'})

    except:
        return render(request, 'login.html')


def add_teacher2(request):
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
                teacher = Teachers(firstName=fName, lastName=lName, email=email,
                phone=phone, roomNo=roomNo, password=password, image=file_url)
                teacher.save()

                teacherObj = Teachers.objects.get(id=teacher.id)
                for i in subList:
                    subject = Subject(subject=i, teacher_id=teacherObj.id)
                    subject.save()

    except  Exception as e:
        # message = traceback.format_exc()
        # print(message)
        msg = 'User not created'
        return render(request, 'add_teacher2.html',{'msg':msg})

    return render(request, 'add_teacher2.html')


def profile(request):
    try:
        teachersObj = Teachers.objects.get(id=request.session['userId'])
        subjectObj = Subject.objects.filter(teacher=teachersObj.id)
        
        return render(request, 'profile.html', {'teacherData':teachersObj, "subObj":subjectObj})
    except :
        return redirect('login')

