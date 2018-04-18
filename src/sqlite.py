import sqlite3
try:
    from .models import Aayulogic
except Exception:
    from models import Aayulogic

"""
first_name => First name of the employee
last_name => Last name of the employee
email => Employee's email
phone_number => Employee's phone number
text => Employee's text bio
date => Employee's date of birth
boolean => Employee's sex - M/F
address => Employee's Address
url => URL to a social account
image_url => Display Image URL

"""


# DbConnect class simply helps to create db connection

class DbConnect:

    conn = sqlite3.connect(':memory:')  # NOTE: sqlite_YOAGQHYR.db contains fake data with 200 entries

    c = conn.cursor()  # cursor object to fetch results

    # We know what we are doing here, right? :D id INTEGER PRIMARY KEY AUTOINCREMENT,

    c.execute("""CREATE TABLE employees (
                 id integer PRIMARY KEY AUTOINCREMENT,
                 first_name text(100), 
                 last_name text(100),
                 email decimal unique,
                 phone_number varchar(30),
                 text text(255),
                 date varchar(20),
                 boolean text(10),
                 address text,
                 url varchar,
                 image_url blob
                 )""")


# Some custom CRUD functions using native SQLite commands
# We bind it inside a class named CrudOperation

class CrudOperation:

    # The 'C' in CRUD
    def insert_emp(emp):
        with DbConnect.conn:
            DbConnect.c.execute(
                "INSERT INTO employees VALUES (:id, :first_name, :last_name, :email, :phone_number, :text, :date, "
                ":boolean, :address, :url,:image_url) ",
                {'id': emp.id,
                 'first_name': emp.first_name,
                 'last_name': emp.last_name,
                 'email': emp.email,
                 'phone_number': emp.phone_number,
                 'text': emp.text,
                 'date': emp.date,
                 'boolean': emp.boolean,
                 'address': emp.address,
                 'url': emp.url,
                 'image_url': emp.image_url
                 })

    # The 'R' in CRUD
    @staticmethod
    def show_all():
        DbConnect.c.execute("SELECT * FROM employees")
        return DbConnect.c.fetchall()

    # The 'U' in CRUD - Needs more modification
    def update_fields(emp, email, text):
        with DbConnect.conn:
            DbConnect.c.execute("""UPDATE employees SET email=:email, text=:text
                      WHERE first_name=:first_name AND last_name=:last_name""",
                      {'first_name': emp.first_name, 'last_name': emp.last_name, 'email': email, 'text': text})
            return c.fetchall()

    # I want the user to UPDATE only the required fields.

    # The 'D' in CRUD
    def remove_emp(emp):
        with DbConnect.conn:
            DbConnect.c.execute("DELETE from employees WHERE first_name=:first_name AND last_name=:last_name",
                      {'first_name': emp.first_name, 'last_name': emp.last_name})
            return DbConnect.c.fetchall()

    """

    Some other functions besides CRUD can be defined in such ways:

    def get_emps_by_name(last_name):
        c.execute("SELECT * FROM employees WHERE last_name=:last_name", {'last_name': last_name})
        return c.fetchall()

    print(get_emps_by_name('Doe'))
    """


class Sort:

    def insertion_sort(a_list):
        for index in range(1, len(a_list)):

            # We'll first track the current positional value
            current_value = a_list[index]

            # We just checked if the index of current position is greater than 0 AND
            # previous positional value is  greater than current
            while index > 0 and a_list[index - 1] > current_value:
                # if thats the case, sort them
                a_list[index] = a_list[index - 1]

                # We just deducted the index by 1
                index = index - 1

            # set the changed index value to current
            a_list[index] = current_value

    # What if I get a better search algorithm? I'll simply bind it over here.

    def another_better_search_algorithm(a_list):
        pass


# Testing it on arbitrary data
emp1 = Aayulogic(1,'John', 'Doe', 'test@fake.com', '984585485', 'Hello All!', '1996/2/3', 1, 'Biratnagar',
                 'www.fb.com/emp1', 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png')
CrudOperation.insert_emp(emp1)
emp2 = Aayulogic(2, 'Ram', 'Doe', 'fake@news.com', '999999999', 'I hate humans.', '1996/12/3', 0, 'Wherenot',
                 'www.fb.com/emp2', 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png')
CrudOperation.insert_emp(emp2)

"""
You can do crud operations like

update = CrudOperation.update_fields(emp2, 'akash@sky.com', 'I dont really hate humans')
remove = CrudOperation.remove_emp(emp2)
"""

print(CrudOperation.show_all())

a_list = list(CrudOperation.show_all())

Sort.insertion_sort(a_list)

print("***********After Sorting***********")

print(a_list)

DbConnect.conn.close()
