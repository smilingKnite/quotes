from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import *
import sys, re
import bcrypt
from django.contrib import messages

#################################################################################################


def index(request):
    users = Users.objects.all()

    return render(request, 'quotes/index.html')


#################################################################################################


def signIn(request):
    errors = Users.objects.verify(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        # request.session['name'] = request.POST['name']
        # request.session['email'] = request.POST['email']
        # context = {
        #     # 'name': request.session['name'],
        #     'email': request.session['email'],
        #     'user': Users.objects.all(),
        #     'quote': Quotes.objects.all()
        # }
        return redirect('/dash')


##################################################################################################
#CREATING USER THEN MAKE FORIEGN KEY RELS AND MAKE TABLES AND THEN THE ADD PAGE TO ADD ITEMS
def createUser(request):
    errors = Users.objects.creater(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hPassword = bcrypt.hashpw((request.POST['cPassword']).encode(),
                                  bcrypt.gensalt())

        Users.objects.create(
            name=request.POST['nName'],
            email=request.POST['eEmail'],
            password=hPassword)


        return redirect('/dash')


#################################################################################################


def addQuote(request):
    errors = Quotes.objects.addQuote(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/dash')
    else:
        Quotes.objects.create(
            quotedBy=request.POST['quotedBy'],
            quote=request.POST['quote'],
            addBy=request.POST['addBy'])
        context = {
            'errorz': errors
        }
        return redirect('/dash')
    # return render(request, "quotes/dashboard.html")



#################################################################################################


def addFav(request):
    user = Users.objects.all()
    quotE = Quotes.objects.all()
    context = {'Users': user, 'Quotes': quotE}
    # boole = True
    return render(request, "quotes/dashboard.html", context)


#################################################################################################


def look(request):

    # print request.session['name']
    # print "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    # name = request.session['name']
    user = Users.objects.all()
    quotE = Quotes.objects.all()

    context = {'Users': user, 'Quotes': quotE}
    return render(request, 'quotes/look.html', context)


#################################################################################################


def edit(request):
    # sys.stdout.flush()
    return render(request, 'quotes/edit.html')


#################################################################################################


def deleter(request):
    print "AND IT'S OUTTA HEEERRREEE"
    return render(request, 'quotes/delete.html')


#################################################################################################


def add(request):
    print "Time to add something.. loser"
    return render(request, 'quotes/add.html')


#################################################################################################


def renderDash(request):

    user = Users.objects.all()
    quotE = Quotes.objects.all()
    context = {'Users': user, 'Quotes': quotE}

    return render(request, "quotes/dashboard.html", context)


#################################################################################################
def goingaway(request):
    request.session.clear()
    return redirect('/')


#################################################################################################

sys.stdout.flush()  # to flush output
# app.run(debug=True)
