import cherrypy
import random
import string
import json
import os



class HelloWorld(object):
	@cherrypy.expose
	def index(self):
		return "Hello World!"


	def randomString(self,stringLength=8):
		letters = string.ascii_lowercase
		return ''.join(random.choice(letters) for i in range(stringLength))


	def data_file_initalizer():
		filename = "data_file.json"
		if not os.path.exists(filename):
			with open(filename,"w+") as f:
				json.dump({}, f)

	@cherrypy.expose
	@cherrypy.tools.json_out()
	@cherrypy.tools.json_in()
	def post(self,request):

		data = {}

		filename = "data_file.json"
		with open(filename) as read_file:
			data = json.load(read_file)

		request = json.loads(request)

		data[request["id"]] = request

		print (request)


		with open(filename, 'w') as json_file:
			json.dump(data, json_file)

		return (data)
HelloWorld.data_file_initalizer()
cherrypy.quickstart(HelloWorld())
