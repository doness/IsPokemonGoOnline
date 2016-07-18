import os
#https://pgorelease.nianticlabs.com/plfe/


def PingaPokemonGo():
	import ping
	delay = ping.verbose_ping('pgorelease.nianticlabs.com')
	json = {}
	json["title"] = "PokemonGoPing"
	json["timeout"] = str(delay)

	f = open("available.txt", "w")
	f.write(str(json))
	f.close()

PingaPokemonGo()
