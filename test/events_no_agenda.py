from pupa.scrape import Scraper
from pupa.scrape import Event
import datetime as dt
import pytz

class EventNoAgendaScraper(Scraper):
    def scrape(self):
        when = dt.datetime(1776,7,4,9,15)
        tz = pytz.timezone("US/Pacific") #set the timezone for this location
        when = tz.localize(when)
        e = Event(name="Hearing",  # Event Name
                      start_time=when,  # When the event will take place
                      timezone=tz.zone, #the local timezone for the event
                      location_name='unknown')  # Where the event will be
        e.add_source("http://example.com")

        yield e
