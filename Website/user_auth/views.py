from django.shortcuts import render, redirect

import requests


def log_in(request):
    name = request.POST['user_name']
    password = request.POST['password']
    info = {"username": name,
            "password": password
            }

    url = 'http://127.0.0.1:8000/user_auth/rest-auth/login/'

    response = requests.post(url, info)

    data = response.json()

    if 'key' in data.keys():
        token = data["key"]
        print(token)
        request.session['token'] = token

        drug_list = []
        request.session["selected_drugs"] = drug_list

        return redirect('search_drug')
    else:
        return redirect('home')


def sign_up(request):
    if request.method == "POST":
        name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = password1

        info = {

            "username": name,
            "email": email,
            "password1": password1,
            "password2": password2,

        }

        url = 'http://127.0.0.1:8000/user_auth/rest-auth/registration/'
        response = requests.post(url, info)

        data = response.json()

        if 'key' in data.keys():
            token = data["key"]

            request.session['token'] = token

            drug_list = []
            request.session["selected_drugs"] = drug_list

            return render(request, 'user_auth/log_in.html', {"data": data})
        else:
            return render(request, 'user_auth/registration.html', {"data": data})

    return render(request, 'user_auth/registration.html', )


def home(request):
    return render(request, 'user_auth/home.html')


def log_out(request):
    url = 'http://127.0.0.1:8000/user_auth/rest-auth/logout/'
    header = {

        'Authorization': "Token {}".format(request.session['token'])
    }

    response = requests.post(url, headers=header)
    data = response.json()

    return redirect("home")
