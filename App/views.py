import os
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile


# Create your views here.

def Home(request):
    return render(request, 'base.html')


def createProf(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        gender = request.POST.get('gender')
        if image:
            profile = Profile(
                name=name,
                image=image,
                age=age,
                address=address,
                phone_no=phone_no,
                date_of_birth=date_of_birth,
                religion=religion,
                gender=gender,
            )
            profile.save()
            return redirect('allProf')
        else:
            profile = Profile(
                name=name,
                age=age,
                address=address,
                phone_no=phone_no,
                date_of_birth=date_of_birth,
                religion=religion,
                gender=gender,
            )
            profile.save()
            return redirect('allProf')

    return render(request, 'createProf.html')


def allProf(request):
    search = request.GET.get('search')
    print(search)
    if search:
        prof = Profile.objects.filter(name__icontains=search)
    else:
        prof = Profile.objects.all()
    context = {
        'pro': prof,
    }

    print('Your Database Datas Are:', prof)
    return render(request, 'profList.html', context)


def profView(request, id):
    prof = Profile.objects.get(id=id)
    return render(request, 'profView.html', locals())


def deleteProf(request, id):
    prof = Profile.objects.get(id=id)
    prof.delete()
    return redirect('allProf')


def update(request, id):
    prof = Profile.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        date_of_birth = request.POST.get('date_of_birth')
        religion = request.POST.get('religion')
        gender = request.POST.get('gender')
        if image:
            if prof.image != 'default/default.jpg.png':
                os.remove(prof.image.path)

            prof.name = name
            prof.image = image
            prof.age = age
            prof.address = address
            prof.phone_no = phone_no
            prof.date_of_birth = date_of_birth
            prof.religion = religion
            prof.gender = gender
            prof.save()
            messages.success(request, 'Updated succesfully.')
            return redirect('allProf')

        else:
            prof.name = name
            prof.age = age
            prof.address = address
            prof.phone_no = phone_no
            prof.date_of_birth = date_of_birth
            prof.religion = religion
            prof.gender = gender
            prof.save()
            messages.success(request, 'Updated succesfully.')
            return redirect('allProf')


    return render(request, 'updateProf.html', locals())
