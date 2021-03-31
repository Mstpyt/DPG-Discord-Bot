import sqlite3
import logging


def TExecSql(database_name: str, statement: str, bind: list = None):
    try:
        conn = sqlite3.connect(database_name)
        c = conn.cursor()
        if bind:
            if bind.__class__.__name__ in ('list', 'tuple'):
                c.execute(statement, bind)
            else:
                c.execute(statement, [bind])
        else:
            c.execute(statement)
        conn.commit()
        conn.close()
    except sqlite3.Error as err:
        print(err)

        logging.error("{}".format(sqlite3.Error))


def TExecSqlReadCount(database_name: str, statement: str, bind: list = None):
    try:
        conn = sqlite3.connect(database_name)
        c = conn.cursor()
        if bind:
            c.execute(statement, bind)
        else:
            c.execute(statement)
        result = c.fetchone()
        conn.close()
        return result
    except sqlite3.Error:
        logging.error("{}".format(sqlite3.Error))


def TExecSqlReadMany(database_name: str, statement: str, bind: list = None):
    try:
        nI = 0
        conn = sqlite3.connect(database_name)
        c = conn.cursor()
        if bind:
            if bind.__class__.__name__ in ('list', 'tuple'):
                c.execute(statement, bind)
            else:
                c.execute(statement, [bind])
        result = c.fetchall()
        print(result)
        conn.close()
        return result
    except sqlite3.Error as err:
        print(err)

