# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from timetable.models import Event, Slot
# Create your views here.

def current(request):
	
	all_events = Event.objects.all()
	num_range = range(8,17)
	all_slots = Slot.objects.all()
	print num_range
	context = {
		'all_events' : all_events,
		'num_range' : num_range, 
		'all_slots': all_slots,
	}	
	


	return render(request, 'timetable/current.html', context)

def addevent(request,indiv_slot_id):
	
	selected_slot = Slot.objects.get(pk=indiv_slot_id)
	

	context ={
		'selected_slot': selected_slot,
		

	}

	return render(request, 'timetable/addevent.html',context)

def thanks(request,indiv_slot_id):

	selected_event =Event()
	selected_event.ename = request.POST['ename']
	selected_event.venue = request.POST['venue']
	selected_event.code = request.POST['code']
	
	

	selected_slot = Slot.objects.get(pk=indiv_slot_id)
	selected_event.slot = selected_slot
	selected_event.save()
	selected_slot.is_free = False
	
	selected_slot.save()

	return	render(request, 'timetable/thanks.html')



