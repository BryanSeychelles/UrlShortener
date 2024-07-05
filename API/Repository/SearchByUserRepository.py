from Service.DatabaseService import DatabaseService

class SearchByUserRepository:

    def __init__(self):
        self.db = DatabaseService()

    def create_search_by_user(self, user_id: str, url_id: str):
        query = (
            "INSERT INTO search_by_user (user_id, url_id) VALUES ('"
            + user_id
            + "', '"
            + url_id
            + "') RETURNING *;"
        )
        try:
            if self.verify_history(user_id, url_id):
                return None
            else:
                records = self.db.execute_query(query)
                return records[0] if records else None
        except Exception as e:
            print("Error while inserting record in create_search_by_user:", e)
            raise e

    def verify_history (self, user_id: str, url_id: str):
        try:
            records = self.db.execute_query(
                "SELECT * FROM search_by_user WHERE user_id = '" + user_id + "' and url_id = '" + url_id +"';"
            )
            print(user_id, 'user_id in verify_history')
            print(url_id, 'url_id in verify_history')
            print(bool(records), "bool(records) in verify_history")
            return bool(records)
        except Exception as e:
            print("Error while fetching record in verify_history:", e)
            raise e
