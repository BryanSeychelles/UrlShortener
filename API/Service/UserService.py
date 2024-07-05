from Repository.UserRepository import UserRepository
from Repository.UrlShortenerRepository import UrlShortenerRepository
from Models.User import User


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.url_shortener_repository = UrlShortenerRepository()

    def get_user_and_urls(self, user_id: str):
        try:
            id = self.user_repository.get_user(user_id)
            urls = self.url_shortener_repository.get_my_searches(id)
            listUrls = []
            for url in urls:
                listUrls.append({"original": url[0], "shortened": url[1]})
            return {
                "id": id,
                "urls": listUrls,
            }
        except Exception as e:
            raise e
            return None
        pass

    def create_user(self):
        try:
            return self.user_repository.create_user()
        except Exception as e:
            raise e
            return None
        pass

    def verify_user(self, user_id: str):
        try:
            return bool(self.user_repository.get_user(user_id))
        except Exception as e:
            raise e
            return None
        pass
        