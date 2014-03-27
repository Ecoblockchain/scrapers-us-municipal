from pupa.scrape import Jurisdiction

from .people import PersonScraper
from .events import EventScraper


class Arlington(Jurisdiction):
    jurisdiction_id = 'ocd-jurisdiction/country:us/state:va/place:arlington/council'
    name = 'Arlington County Board'
    url = 'http://www.arlingtonva.us/Departments/CountyBoard/CountyBoardMain.aspx'
    provides = ['people']
    parties = [
        {'name': 'Democratic' },
        {'name': 'Green' },
        {'name': 'Republican'}
    ]
    sessions = [
        {'name': '2014', '_scraped_name': '2014'}
    ]

    def get_scraper(self, session, scraper_type):
        if scraper_type == 'people':
            return PersonScraper
        elif scraper_type == 'events':
            return EventScraper

    def scrape_session_list(self):
        return ['2014']

