import psycopg2
from Utils.GetEnv import GetEnv

class DatabaseService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connect()
        return cls._instance

    def connect(self):
        env = GetEnv("database")
        config = f"dbname={env['database']} user={env['user']} port={env['port']} host={env['host']} password={env['password']}"
        conn = psycopg2.connect(config)
        conn.set_session(autocommit=True)
        print("Database connected successfully")
        self.conn = conn
        self.cur = conn.cursor()

    def execute_query(self, query):
        self.cur.execute(query)
        records = self.cur.fetchall()
        print("Records fetched successfully")
        return records

    def close(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
        print("Database connection closed")
        DatabaseService._instance = None
