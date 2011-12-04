
import ftclient as ft
import urllib2
from xml.etree.ElementTree import parse

def getGeocode(address):
	add_list=address.split()
	add_html='+'.join(add_list)
	maps_request="http://maps.googleapis.com/maps/api/geocode/xml?address="+\
	add_html+"&sensor=true"
	#maps_request="http://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=true"
	#maps_request="http://maps.googleapis.com/maps/api/geocode/json?address=205+Wilmington+Ave,+TORONTO,+ONTARIO,+CANADA&sensor=true"
	req = urllib2.Request(url=maps_request)
	etree = parse(urllib2.urlopen(req)).getroot()
	loc = etree.find('result/geometry/location')
	lat = loc.findtext('lat')
	lng = loc.findtext('lng')
	return (lat,lng)

def getIDAddresses(tableid):
	client = ft.FTClient("")
	query = "select ID,ADDRESS from "\
			+str(self.tableid)
	header_data = client.runGetQuery(query)
	data = header_data.partition('\n')[2]
	rows = data.split('\n')
	id_addr = [ (r.partition(',')[0],r.partition(',')[2]) for r in rows ] 
	return id_addr

def addlatlng():
	tableid = 2334172
	id_addresses = getIDAddresses(tableid)
	client = ft.FTClient("")
	for id,address in id_addresses:
		lat,lng = getGeocode(address)
		query = "update "+str(tableid)+" set "+\
				"LATITUDE="+str(lat)+", LONGITUDE="+\
				str(lng)+" where ID="+str(id)
	
