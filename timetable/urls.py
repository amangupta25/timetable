from django.conf.urls import url
from . import views


urlpatterns = [
	# /timetable/
	url(r'^$', views.current, name='current'),

	# /timetable/addevent

	url(r'^addevent/(?P<indiv_slot_id>[0-9]+)$', views.addevent, name='addevent'),

	#/timetable/addevent/1212/thanks

	url(r'^addevent/(?P<indiv_slot_id>[0-9]+)/thanks$', views.thanks, name='thanks'),


]