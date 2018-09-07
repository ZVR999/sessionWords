# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'session_words/index.html')

def process(request):
    now = datetime.now()
    word = request.POST['new_word']
    color = ''
    added_on = '<span> - added on '+str(now)+' </span>'
    end = '</div>'
    # Create a log to hold all entries
    if not 'log' in request.session:
        request.session['log'] = []
    # Create an entry to be placed in the log
    if not 'entry' in request.session:
        request.session['entry']= ''

    if request.POST['color'] == 'red':
        if 'big_font' in request.POST:
            color = '<div class="red big">'
            added_on = '<span class="reg"> - added on '+str(now)+' </span>'
        else:
            color = '<div class="red">'
    elif request.POST['color'] == 'green':
        if 'big_font' in request.POST:
            color = '<div class="green big">'
            added_on = '<span class="reg"> - added on '+str(now)+' </span>'
        else:
            color = '<div class="green">'
        
    elif request.POST['color'] == 'blue':
        if 'big_font' in request.POST:
            color = '<div class="blue big">'
            added_on = '<span class="reg"> - added on '+str(now)+' </span>'
        else:
            color = '<div class="blue">'
    
    request.session['entry'] = "{}{}{}{}".format(color,word,added_on,end)
    entry = request.session['entry']
    log = request.session['log'] 
    log.append(entry)
    
    # print request.POST['big_font']
    return redirect('/')

def clear(request):
    request.session['log'] = []
    return redirect('/')