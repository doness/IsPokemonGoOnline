
# https://pgorelease.nianticlabs.com/plfe/

class Ping:
	def PingPokemonGo(self):
		import ping
		delay = ping.verbose_ping('pgorelease.nianticlabs.com')
		json = {}
		json["title"] = "PokemonGoPing"
		json["timeout"] = str(delay)
		#print(str(json)) # FOR VERBOSE PURPOSES ONLY
		f = open("available.json", "r+")
		f.write(str(json))
		f.close()

Ping().PingPokemonGo()