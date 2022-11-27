# Adaptador de banco de dados PostgreSQL
import psycopg2
# Load data from metadata
import UploadMetadados
# Archives Constants
from Constants import Constants

# Connect to the Bank and run the script
def connectionDatabase(sql):
    connection = psycopg2.connect(host='localhost', database='logredo', user='root', password='root')
    cursor = connection.cursor()
    # print('Database connection opened!')

    try:
        cursor.execute(sql)
        
        if cursor.pgresult_ptr is not None:
            return  cursor.fetchall()

        connection.commit()
    except(Exception, psycopg2.DatabaseError) as Error:
        print("Database Error: %s" % Error)
        connection.rollback()
        cursor.close()
    finally:
        if connection is not None:
            connection.close()
            # print('Database connection closed!')
        
    cursor.close()

# Commands DML Database
def commandSelectAll():
    return connectionDatabase(Constants.SELECT_REGISTERS)

def commandInsert(ID, A, B):
    sql = f'INSERT INTO t_logredo VALUES ({ID}, {A}, {B})'
    return connectionDatabase(sql)

def commandUpdate(ID, FIELD, VALUE):
    sql = f'UPDATE t_logredo SET {FIELD}={VALUE} WHERE ID = {ID}'
    return connectionDatabase(sql)

def commandCreateTable():
    return connectionDatabase(Constants.CREATE_TABLE)

def commandDropTable():
    return connectionDatabase(Constants.DROP_TABLE)

# Load metadata files for table
def archiveToTable():
    try:
        output = UploadMetadados.uploadMetadados()

        for line in output:
            commandInsert(line[0], line[1], line[2])
    except:
        print('Error loading data for insert command!')

# Commands executed in table
def load():
    try:
        commandDropTable()   # If exists table drop
        commandCreateTable() # Create table
        archiveToTable()     # Load metadata files for table
    except:
        print('Error when executing DML commands!');
