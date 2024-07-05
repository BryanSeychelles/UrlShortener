import pyshorteners
from Repository.UrlShortenerRepository import UrlShortenerRepository
from Repository.SearchByUserRepository import SearchByUserRepository
import logging

class UrlShortenerService:
    def __init__(self):
        self.url_shortener_repository = UrlShortenerRepository()
        self.sbur = SearchByUserRepository()
        self.s = pyshorteners.Shortener()

    def shorten(self, url: str, user_id: str) -> str:        
        if self.url_shortener_repository.is_url_exists(url):
            print("URL already exists")
            try:
                short_url = self.url_shortener_repository.get_short_url(url)
                url_id = self.url_shortener_repository.get_id(url)
                if not self.sbur.verify_history(user_id, url_id):
                    print("Creating search by user")
                    self.sbur.create_search_by_user(user_id, url_id)
                return short_url
            except Exception as e:
                logging.error("Error while getting short URL, error: %s", e)
                raise e
                return None
        else:
            try:
                short_url = self.s.tinyurl.short(url)
                records =  self.url_shortener_repository.create_short_url(url, short_url, user_id)
                self.sbur.create_search_by_user(user_id, records["id"])
                return records["url"]
            except Exception as e:
                logging.error("Error while shortening URL, error: %s", e)
                raise e
                return None

    def get_original_url(self, short_url) -> str:
        return self.s.tinyurl.expand(short_url)
