class Ping:
	def PingPokemonGo(self):
		import requests
		import ping
		import json
		#elapsedtime = pingoldao.verbose_ping('54.241.32.9')
		with open("servers.json","r+") as jsonfile:
			r = jsonfile.read().replace('\'', '"')
			j = json.loads(r)
			#print j
			for i in ["AUTH","CON","US","UK","GER","NED"]:
				elapsedtime = ping.verbose_ping(j[i]['ip'])
				if elapsedtime is not "timeout":
					j[i]['delay'] = int(round(elapsedtime))
				else:
					j[i]['delay'] = elapsedtime

				if 170 > elapsedtime or elapsedtime == 170:
					j[i]['quality'] = "Online"
				elif 170 < elapsedtime < 500:
					j[i]['quality'] = "Unstable"
				elif elapsedtime > 500 or elapsedtime == "timeout":
					j[i]['quality'] = "Offline"
				#print j[i]['delay']
			json.dump(j,open("output.json","w"),indent=4)

Ping().PingPokemonGo()
