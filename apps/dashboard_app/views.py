from django.shortcuts import render, redirect, HttpResponse

def panel(request):
    return HttpResponse('Panel de usuario')


