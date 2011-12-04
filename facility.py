
class Facility:
	def __init__(self,name,address):
		self.id=id
		self.address=address
		self.lat=lat
		self.lng=lng


#def make_facilities(data):
#	rows = data.split('\n')
#	F = []
#	for r in rows:
#		lat,lng=getGeocode(r.addr)
#		F = facility(name)


def json(facility_data):
	return "{"+facility_data+"}"
