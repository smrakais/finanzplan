from datetime import date
from datetime import datetime

class kosten:
    def __init__(self,porto,buero,stuff):
        
        #veräderbar
        self.porto = porto
        self.buero = buero 
        self.stuff = stuff
        
        #fix
        #attributes time/date
        stringZeit = datetime.now().strftime('%H:%M:%S')
        self.time = stringZeit

        datum = date.today()
        tag = datum.day
        monat = datum.month
        jahr = datum.year

        self.day = tag
        self.month = monat 
        self.year = jahr 

    
#weiß nicht was besser string oder integer mal sehen
    def get_all(self):
        alles=[self.porto,self.buero,self.stuff]
        return  alles

#TODO get date? und dann in txt soeichern

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        print(self.year)
        return year

    def get_time(self):
        return self.time

    def get_porto(self):
        #print(self.porto)
        return porto
    
    def get_buero(self):
        #print(self.buero)
        return buero

    def get_stuff(self):
        #print(self.stuff)
        return stuff

    #def get_total(self):
