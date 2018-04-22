"""
The following code is for testing the fake data which is stored on custom database 'postgresql_kzemssmd'
Here, we have generated a database with relevant fields with up to 100000 entries.
Below, we have defined a custom function to show all the data stored in the table.

Method for generating fake data using fake2db:

fake2db --rows 100000 --db postgresql --custom first_name last_name email phone_number text date boolean address url image_url

"""

import unittest

import psycopg2


conn = psycopg2.connect("dbname=postgresql_kzemssmd user=postgres password=postgres host=localhost")
c = conn.cursor()


def show_all():
    c.execute("SELECT * FROM custom")
    return c.fetchall()


"""
Testing the number of entries on the database.
"""


class TestNumber(unittest.TestCase):

    def test_number_of_entries(self):
        self.assertGreaterEqual(len(show_all()), 100000)


if __name__ == '__main__':
    unittest.main()

conn.close()