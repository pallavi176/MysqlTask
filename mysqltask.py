from mysqloperation import MysqlOperation

DB = 'cardataset'
TABLE = 'car'

conn_1 = MysqlOperation('localhost','root','root')

print(conn_1)
print(repr(conn_1))
print(str(conn_1))

#1 . take a data set from attached URL https://archive.ics.uci.edu/ml/datasets/Car+Evaluation
#2 . create a database called as cardataset

print(conn_1.create_database(DB))

#3 . create a table called as car with a column name given in dataset description
print(conn_1.use_database(DB))

table_structure = {"buying": "VARCHAR(20)", "maint": "VARCHAR(20)", "doors": "VARCHAR(20)", "persons": "VARCHAR(20)",
                   "lug_boot": "VARCHAR(20)", "safety": "VARCHAR(20)", "Class": "VARCHAR(20)"}
print(conn_1.create_table(TABLE, table_structure))

#4. Dump all the data into car table
print(conn_1.bulk_insert_table(TABLE,'car.data'))

#5. try to check weather all the data is aviable inside your table or not
print(conn_1.select_count_table(TABLE))

#6. try to group all the data with COL1 AND count occurences of each and every record based on col1 value
print(conn_1.select_groupdata_table(TABLE,'buying'))

#7. Try to filter a record where col 3 value will be 4 .
data=conn_1.select_filterdata_table(TABLE,'doors','4')
for d in data:
    print(d)

#8. Try to update a col 3 value with 8 whereever you have value equal to 2
print(conn_1.update_column_table(TABLE,'doors','2','8'))

#9. try to delete table
print(conn_1.drop_table(TABLE))

#10.Try to delete database
print(conn_1.drop_database(DB))