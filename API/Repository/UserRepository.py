from Service.DatabaseService import DatabaseService
from Models.User import User


class UserRepository:

    def __init__(self):
        self.db = DatabaseService()

    def get_user(self, user_id: str):
        try:
            records = self.db.execute_query(
                "SELECT id FROM users WHERE id = '" + user_id + "';"
            )
            return records[0][0] if records else None
        except Exception as e:
            raise e
            return None
        pass

    def create_user(self) -> str:
        query = "INSERT INTO users DEFAULT VALUES RETURNING id;"
        try:
            records = self.db.execute_query(query)
            print(records, "user created records")
            return records[0][0] if records else None
        except Exception as e:
            raise e
            return None
        pass
