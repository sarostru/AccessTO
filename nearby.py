from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import fusion
import facility

class NearbyPage(webapp.RequestHandler):
	def get(self):
		service=self.request.get("service")
		latitude=self.request.get("latitude")
		longitude=self.request.get("longitude")
		self.response.headers['Content-Type'] = 'text/plain'
		response="Service: "+service+"\nLatitude: "+\
				latitude+"\nLongitude: "+longitude
		#database = fusion.DataBase(2334172)
		database = fusion.DataBase(2337646)
		my_facilities = database.nearbyRequest(latitude,longitude,service)
		response = facility.json(my_facilities)
		self.response.out.write(response)





application = webapp.WSGIApplication(
										[('/nearby',NearbyPage)],
										debug=True)


def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()

