from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from deepak_app.models import RegisterModel,book_details

def registration_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        contact_number = request.POST.get('phnum')
        password = request.POST.get('password')
        register_model = RegisterModel.objects.create(
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            email=email,
            contact_number=contact_number,
            password=password,
        )
        return redirect('login')
    return render(request, 'register.html')

def book_details_view(request):
    if request.method == 'POST':
        Book_Name=request.POST.get('bookname')
        Author_Name=request.POST.get('authorname')
        File_Data=request.FILES['filedata']
        Status=request.POST.get('status')
        Create_Date=request.POST.get('createdate')
        Update_Date=request.POST.get('updatedate')

        book_model= book_details.objects.create(
            Book_Name=Book_Name,
            Author_Name=Author_Name,
            File_Data=File_Data,
            Status=Status,
            Create_Date=Create_Date,
            Update_Date=Update_Date,
        )
        return redirect('book_submit_admin')
    return render(request,'book_details.html')

def login(request):
    if request.method == 'POST':
        mailidlogin=request.POST.get('mailid')
        pswrdlogin = request.POST.get('pswrd')
        try:
            obj=RegisterModel.objects.get(email=mailidlogin,password=pswrdlogin)
            request.session['uid'] = obj.id
            if obj.email == 'admin@gmail.com':
                return redirect('home')
            else:
                request.session['firstname']=obj.first_name
                request.session['lastname']=obj.last_name
                return redirect('book_submit')
        except:
            pass
    return render(request , 'login.html')

def home(request):
    obj=RegisterModel.objects.all()
    return render(request,'home.html',{'object':obj})

def book_submit(request):
    firstname=request.session['firstname']
    lastname=request.session['lastname']
    # id=request.session['id']
    obj=book_details.objects.all()
    return render(request,'book_submit.html',{'object':obj,'firstname':firstname,'lastname':lastname})


def book_submit_admin(request):
    obj=book_details.objects.all()
    return render(request,'book_submit_admin.html',{'object':obj})

def delete_book(request,id):
    obj = book_details.objects.filter(id=id).delete()
    return redirect('book_submit_admin')

def my_details(request):
    uid=request.session['uid']
    obj_details=RegisterModel.objects.filter(id=uid)
    return render(request,'my_details.html',{'object':obj_details})

def edit_details(request):
    uid = request.session['uid']
    obj_details = RegisterModel.objects.filter(id=uid)
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        contact_number = request.POST.get('phnum')
        register_model = RegisterModel.objects.filter(id=uid).update(
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            gender=gender,
            email=email,
            contact_number=contact_number,
        )
        return redirect('my_details')
    return render(request,'edit_details.html',{'object':obj_details})

def change_password(request):
    uid = request.session.get('uid')

    if request.method == 'POST':
        newPassword = request.POST.get('newPassword')
        confirmPassword = request.POST.get('confirmPassword')
        oldpassword = request.POST.get('oldPassword')

        try:
            user = RegisterModel.objects.get(id=uid)
            if user.password == oldpassword:
                if newPassword == confirmPassword:
                    user.password = newPassword
                    user.save()
                    return redirect('my_details')
        except:
            pass

    return render(request, 'change_password.html')

