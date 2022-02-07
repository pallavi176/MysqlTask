import csv
import mysql.connector as connection
from custom_logger import CustomLogger

class MysqlOperation:
    log = CustomLogger.log('mysql.log')

    def __init__(self,host,user,passwd):
        """
        Intializing with Variables
        """
        try:
            self.host=host
            self.user=user
            self.passwd=passwd
            self.conn=self.establish_db_conn()
            self.cursor=self.conn.cursor()
            self.log.info(f"Initialized all the variables: {host}, {user}, {passwd}")
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def establish_db_conn(self):
        """
        Creating mysql database connection
        """
        try:
            self.log.info("Creating mysql database connection")
            mydb = connection.connect(host=self.host, user=self.user, passwd=self.passwd)
            return mydb
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def create_database(self,db):
        """
        Creating database
        """
        try:
            query = "create database {}".format(db)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            self.log.info(f"Database: {db} created")
            return f"Database: {db} created"
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def use_database(self,db):
        """
        Use database
        """
        try:
            query = "use {}".format(db)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            self.log.info(f"Database: {db} in use.")
            return f"Database: {db} in use."
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def create_table(self, tabl, tabl_struct):
        """
        Creating table
        """
        try:
            if type(tabl_struct) == dict:
                tabl_query='CREATE TABLE IF NOT EXISTS {} ('.format(tabl)
                for k in tabl_struct:
                    tabl_query += k + ' '+ tabl_struct[k]+', '
                tabl_query = tabl_query[:-2]
                tabl_query += ')'
                #print(tabl_query)
                self.cursor.execute(tabl_query)
                self.log.info(f"Executed Query: {tabl_query}")
                self.log.info(f"Table: {tabl} created successfully with format: {tabl_struct}")
                return f"Table: {tabl} created successfully"
            else:
                self.log.error(f"Table format not correct: {tabl_struct}")
                return "Table format not correct"
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def select_data_table(self, tabl):
        """
        Select Data from table
        """
        try:
            query = "select * from {}".format(tabl)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            res = self.cursor.fetchall()
            self.log.warning(f"Returning data from Table: {tabl}.")
            return res
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def bulk_insert_table(self, tabl, file_name):
        """
        Bulk insertion to table
        """
        try:
            with open(file_name, 'r') as f:
                file_data = csv.reader(f, delimiter='\n')
                for i in file_data:
                    s = '"' + i[0].replace(',', '","') + '"'
                    #print(s)
                    query = f'INSERT INTO {tabl} values ({s})'
                    self.cursor.execute(query)
                self.conn.commit()
                self.log.info(f"Executed sample Query: {query}")
            self.log.info(f"Bulk data inserted to Table: {tabl} from file: {file_name}")
            return f"Bulk data inserted to Table: {tabl} from file: {file_name}"
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def select_groupdata_table(self, tabl, col):
        """
        Group all the data with COL1 AND count occurences of each
        and every record based on col1 value
        """
        try:
            query = 'select count({0}), {0} from {1} group by {0}'.format(col,tabl)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            res = self.cursor.fetchall()
            self.log.info(f"Returning grouped data from Table: {tabl}.")
            return res
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def select_filterdata_table(self, tabl, col, val):
        """
        filter a record where col 3 value will be 4
        """
        try:
            query = "select * from {} where {} = '{}'".format(tabl, col, val)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            res = self.cursor.fetchall()
            self.log.info(f"Returning grouped data from Table: {tabl}.")
            return res
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def update_column_table(self, tabl, col, old_val, new_val):
        """
        update a col 3 value with 8 whereever you have value equal to 2
        """
        try:
            query = "update {0} set {1}='{3}' where {1}='{2}'".format(tabl, col, old_val, new_val)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            self.conn.commit()
            self.log.info(f"Updated column:{col} having old value: {old_val} with {new_val} in Table: {tabl}.")
            return f"Updated column:{col} having old value: {old_val} with {new_val} in Table: {tabl}."
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def drop_table(self, tabl):
        """
        Drop table
        """
        try:
            query = "drop table {}".format(tabl)
            self.log.info(f"Executed Query: {query}")
            self.cursor.execute(query)
            self.log.info(f"Table: {tabl} dropped")
            return f"Table: {tabl} dropped"
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def drop_database(self, db):
        """
        Drop Database
        """
        try:
            query = "drop database {}".format(db)
            self.log.info(f"Executed Query: {query}")
            self.cursor.execute(query)
            self.log.info(f"Databse: {db} dropped")
            return f"Databse: {db} dropped"
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def select_count_table(self, tabl):
        """
        Select Number of records in a table
        """
        try:
            query = "select count(*) from {}".format(tabl)
            self.cursor.execute(query)
            self.log.info(f"Executed Query: {query}")
            res = self.cursor.fetchall()
            self.log.info(f"Number of records present in table: {tabl} is: {res}")
            return res
        except Exception as e:
            self.log.exception(str(e))
            print(e)

    def __str__(self):
        return '{} - {}'.format(self.host, self.user)

    def __repr__(self):
        return "DbConnection('{}', '{}', '{}')".format(self.host, self.user, self.passwd)

