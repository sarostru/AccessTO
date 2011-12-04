import ftclient as ft

class DataBase:
	def __init__(self,tableid):
		#self.token = ft.GoogleClientLogin(username,password)
		self.token=""
		self.client = ft.FTClient(self.token)
		self.tableid = tableid
	
	def idRequest(self,id):
		query = "select LOCATION_TYPE,ADDRESS,PHONE,ACCESSIBILITY_SHORT from "\
				+str(self.tableid)+" where ID="+str(id)
		header_data = self.client.runGetQuery(query)
		data = header_data.partition('\n')[2]
		return data

	def nearbyRequest(self,latitude,longitude,service):
		#query = "select LOCATION_TYPE,ADDRESS,PHONE,ACCESSIBILITY_SHORT from "\
		lat = float(latitude)/1000000.0
		lng = float(longitude)/1000000.0
		#query = "select ADDRESS from "\
		query = "select LOCATION_TYPE,ADDRESS,PHONE,ACCESSIBILITY_SHORT,LATITUDE,LONGITUDE from "\
				+str(self.tableid)+" "\
				+"order by ST_DISTANCE(ADDRESS, LATLNG("\
				+str(lat)+", "+str(lng)+"))"\
				+" limit 2"
		header_data = self.client.runGetQuery(query)
		data = header_data.partition('\n')[2]
		return data

