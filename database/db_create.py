import sqlite3


def create_database(database_name: str):
    try:
        conn = sqlite3.connect(database_name)
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS DPG_API(
            Command         TEXT,
            Message         TEXT
            )
        """)
        conn.commit()
        conn.close()
    except sqlite3.Error:
        print("{}".format(sqlite3.Error))
