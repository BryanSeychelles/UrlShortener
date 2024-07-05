from Service.DatabaseService import DatabaseService
import psycopg2
import logging

class UrlShortenerRepository:
    def __init__(self):
        self.map = {}
        self.db = DatabaseService()

    def is_url_exists(self, url):
        try:
            records = self.db.execute_query(
                "SELECT current FROM urls WHERE current = '" + url + "';"
            )
            return bool(records)
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching record:", error)
            raise error
            return None

    def get_short_url(self, url):
        try:
            records = self.db.execute_query(
                "SELECT shorten FROM urls WHERE current = '" + url + "';"
            )
            return records[0][0] if records else None
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching record:", error)
            return None

    def get_id(self, url):
        try:
            records = self.db.execute_query(
                "SELECT id FROM urls WHERE current = '" + url + "';"
            )
            return records[0][0] if records else None
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching record:", error)
            return None

    def create_short_url(self, url, short_url, user_id):
        query = (
            "INSERT INTO urls (current, shorten) VALUES ('"
            + url
            + "', '"
            + short_url + "') RETURNING id, shorten;"
        )
        try:
            records = self.db.execute_query(query)
            return {"id": records[0][0], "url": records[0][1]} if records else None
        except (Exception, psycopg2.Error) as error:
            logging("Error while inserting record:", error)
            return None

    def get_my_searches(self, user_id):
        query = "SELECT u.current, u.shorten FROM search_by_user sbu inner join urls u on sbu.url_id = u.id  WHERE sbu.user_id = '" + user_id + "';"
        try:
            records = self.db.execute_query(query)
            print(records, 'records in get_my_searches')
            return records
        except (Exception, psycopg2.Error) as error:
            logging("Error while fetching record:", error)
            raise error
            return None
