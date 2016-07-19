
class Availability:
    def IPGOOAvailable(self):
        import json
        a = json.loads(open("available.json", "r").read().replace('\'', '"'))
        #print(a["timeout"])
        return a["timeout"]

class messages:
    def PingMessage(self):
        b = Availability().IPGOOAvailable()
        print(b)
        if int(float(b)) < 170:
            return 0

        if float(170) < int(float(b)) < float(500):
            return 1

        if float(500) < int(float(b)):
            return 2

        if float(170) == int(float(b)):
            return 3
