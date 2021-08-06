from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import Bmi, User


def index(request):
    global state
    context = {}
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))

        bmi = round((weight / ((height / 100) ** 2)), 2)
        save = request.POST.get("save")
        if save == "on":
            Bmi.objects.create(user=request.user, weight=weight, height=height, bmi=bmi)
        if bmi < 18.5:
            state = "Underweight"
        elif 18.5 < bmi < 24.9:
            state = "Healthy Weight"
        elif 24.9 < bmi < 29.9:
            state = "Overweight"
        elif bmi > 29.9:
            state = "Obese"

        context["bmi"] = bmi
        context["state"] = state

    return render(request, 'index.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Login Details')
            return redirect('login')
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken, please try another')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password does not match")
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def history(request):
    histories = Bmi.objects.all()
    return render(request, 'history.html', {'histories': histories})


def delete(request, id):
    context = {}
    remove = Bmi.objects.get(id=id)
    if request.method == 'POST':
        remove.delete()
        return redirect('/history')
    return render(request, "delete.html", context)
