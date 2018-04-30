import sqlite3

import os

DEFAULT_DB_FILENAME = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                   'wordcount_users.db'))


class LoginAuthentication(object):
    def __init__(self, db_filename=DEFAULT_DB_FILENAME):
        self.connection = sqlite3.connect(db_filename)
        self.cursor = self.connection.cursor()

    def authenticate(self, username, password):
        sql_query = "SELECT * FROM wordcount_users WHERE username='{}'" \
                    " and password='{}';".format(username, password)
        rows = self.cursor.execute(sql_query)
        rows = [1 for row in rows]
        return len(rows) == 1
