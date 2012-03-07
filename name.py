from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import fusion
import facility

class NamePage(webapp.RequestHandler):
	def get(self):
		name=self.request.get("name")
		self.response.headers['Content-Type'] = 'text/plain'
		#database = fusion.DataBase(2334172)
		#database = fusion.DataBase(2337646)
		database = fusion.DataBase(2921075)
		my_facility = database.idRequest(name)
		response = facility.json(my_facility)
		self.response.out.write(response)


application = webapp.WSGIApplication(
										[('/name',NamePage)],
										debug=True)



def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()

