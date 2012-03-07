#!usr/bin/env python

import urllib2
import csv
from xml.etree.ElementTree import parse

def load_funguide(filename):
	f = open(filename,'rb')
	#First line is the keys
	fg_reader = csv.reader(f,delimiter=',',quotechar='"')
	#keys = [  k.replace('"','') for k in f.readline().strip().split(',') ]
	keys = [  k.replace('"','') for k in fg_reader.next() ]
	data = dict( zip(keys,[ [] for _ in keys ]))
	#print(keys)
	#print(len(keys))
	#The rest is data
	for r in fg_reader:
		#r = [ k.replace('"','') for k in line.strip().split(',') ]
		#print(len(r))
		for k,v in zip(keys,r):
			data[k].append(v)
	#print(data)
	f.close()
	return data

def save_funguide(data,filename):
	f = open(filename,'wb')
	keys = list(data.keys())
	fg_writer = csv.writer(f,delimiter=',',quotechar='"')
	fg_writer.writerow(keys)
	n = len(data[keys[0]])
	for i in range(0,n):
		r = [ data[k][i] for k in keys ]
		fg_writer.writerow(r)
	f.close()
	
def format_address(data,city,state,country):
	Addresses = [ a + "," + ",".join([city,state,country]) for a in data['Address'] ]
	data['Address'] = Addresses
	
	
def getGeocode(address):
	add_html=address.upper().replace(',',',+').replace(' ','+')
	#add_html='+'.join(add_list)
	maps_request="http://maps.googleapis.com/maps/api/geocode/xml?address="+\
	add_html+"&sensor=true"
	#maps_request="http://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=true"
	#maps_request="http://maps.googleapis.com/maps/api/geocode/json?address=205+Wilmington+Ave,+TORONTO,+ONTARIO,+CANADA&sensor=true"
	req = urllib2.Request(url=maps_request)
	#print(maps_request)
	etree = parse(urllib2.urlopen(req)).getroot()
	loc = etree.find('result/geometry/location')
	print(address+str(loc))
	if loc:
		lat = loc.findtext('lat')
		lng = loc.findtext('lng')
		return (lat,lng)
	else:
		return (0.0,0.0)
	
def add_lat_longs(data):
	format_address(data,'Toronto','Ontario','Canada')
	Addresses = data['Address']
	data['Latitude']=[]
	data['Longitude']=[]
	for a in Addresses:
		coord = getGeocode(a)
		data['Latitude'].append(str(coord[0]))
		data['Longitude'].append(str(coord[1]))
#load_funguide('chart_page_7.csv')