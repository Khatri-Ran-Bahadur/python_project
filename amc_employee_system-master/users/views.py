from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from users.models import User

def Login(request):
    data = {
        "message":""
    }
    if request.method == "POST":
        input_data = request.POST
        username = input_data["username"]
        password = input_data["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            data["message"] = "Invalid username/password"

    return render(request, "login.html", data)


def Register(request):
    data = {
        "message":""
    }
    if request.method == "POST":
        input_data = request.POST

        user = User.objects.filter(
                username=input_data["username"]
                )
        if user:
            data["message"] = "username already exists"

        else:
            user = User.objects.create(
                    username=input_data["username"],
                    email=input_data["email"],
                    phone=input_data["phone"]
                )
            user.set_password(input_data["password"])
            user.save()
            data["message"] = "User created successfully"

    return render(request, "register.html", data)