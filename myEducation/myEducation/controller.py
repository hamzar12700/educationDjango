# from django.contrib import messages  # Correct import for Django's message framework
# from email import message
# from django.shortcuts import redirect, render
# from educationModel.models import Auth


# def formView(request) : 
#     return render (request , 'index.html')

# # def loginPage(request) : 
# #     return render (request , 'login.html')

# def insertFun (request) :
#     if request.method == 'POST' :
#         name = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         checkname = Auth.objects.filter(name=name).exists()
#         checkemail = Auth.objects.filter(email = email).exists()
#         if checkname : 
#             message.error(request, "name already exist!!!")
#             return render(request , "index.html")
#         elif checkemail :
#             message.error(request, "email already exist!!!")
#             return render(request , "index.html")
#         elif 8 < len(password) < 15:
#             userdata = Auth.objects.create(name = name , email = email , password = password)
#             userdata.save()
#             message.success(request, "account create successfully!!")
#             return render (request , 'index.html')
#         else :
#             message.error(request, "password should be greater than 8 and less than 15")
#             return render (request , 'index.html')



from django.shortcuts import redirect, render
from django.contrib import messages  # Correct import for messages framework
from educationModel.models import Auth

def formView(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def insertFun(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        # if not name or not email or not password:  # Basic form validation
        #     messages.error(request, "All fields are required!")
        #     return render(request, 'index.html')

        checkname = Auth.objects.filter(name=name).exists()
        checkemail = Auth.objects.filter(email=email).exists()

        if checkname:
            messages.error(request, "Name already exists!")
            return render(request, 'index.html')
        elif checkemail:
            messages.error(request, "Email already exists!")
            return render(request, 'index.html')
        elif 8 < len(password) < 15:
            userdata = Auth.objects.create(name=name, email=email, password=password)
            userdata.save()
            return render(request, 'login.html')
        else:
            messages.error(request, "Password should be between 8 and 15 characters.")
            return render(request, 'index.html')


# def logincheck(request) :
#     if request.method == "POST" :
#         loginemail = request.POST['email']
#         loginpassword = request.POST['password']
#         checkuseremail = Auth.objects.filter(email = loginemail).first()
#         checkuserpassword = Auth.objects.filter(password = loginpassword).first()
#         checkuserdata = Auth.objects.filter(email=loginemail , password = loginpassword)
#         if checkuseremail == '' :
#             messages.success(request , "Invalid email")
#             return render (request, 'login.html')
#         elif checkuserpassword == '' :
#             messages.success(request , 'Invalid Passowrd')
#             return render (request, 'login.html')
#         elif checkuserdata :
#             #   request.session['getid'] = checkuserdata.id
#             #   request.session['getname'] = checkuserdata.name
#                request.session['getid'] = checkuserdata.id
#                request.session['getname'] = checkuserdata.name
#                return render(request, 'home.html')
#         else :
#              messages.success(request , 'User Not Found')
#              return render (request, 'login.html')
        
def logincheck(request):
    if request.method == "POST":
        loginemail = request.POST['email']
        loginpassword = request.POST['password']
        
        # Single user retrieve karna
        checkuser = Auth.objects.filter(email=loginemail, password=loginpassword).first()

        if checkuser is None:  # Agar user nahi mila
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html')
        else:
            # Session set karna correct object se
            request.session['getid'] = checkuser.id
            request.session['getname'] = checkuser.name
            return render(request, 'home.html')  # Successful login
    else:
        return render(request, 'login.html')  # Agar GET request ho toh login form dikhaye


def homePage(request) :
    return render(request , "home.html")