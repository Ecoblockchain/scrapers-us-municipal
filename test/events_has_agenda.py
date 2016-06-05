from .events_no_agenda import EventNoAgendaScraper
from pupa.scrape import Event
import datetime as dt
import pytz

class EventHasAgendaScraper(EventNoAgendaScraper):
    def scrape(self):
        for obj in super(EventHasAgendaScraper, self).scrape():
            e = obj

            #add an agenda item to this event
            a = e.add_agenda_item(description="Testimony from concerned citizens")

            yield e
