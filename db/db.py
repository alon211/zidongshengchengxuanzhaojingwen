import pyodbc

class dbcls():
    def __init__(self,dbtype,dbserver,dbname,user,password,timeout):
        '''
            dbtype:mssql
            dbserver:数据库服务器名称
            dbname：数据库名称


        '''
        self._dbtype=dbtype
        self._driver=self.get_drivertype()
        if self._driver =='error':
            print('选择驱动类型不正确，支持类型为:mssql')
            return None
        self._dbserver=dbserver
        self._dbname=dbname
        self._user=user
        self._password=password
        self._timeout=timeout
        try:
            self._db=self._dbconnect()
            self._cursor=self._db.cursor()
        except Exception as identifier:
            print('dbcls初始化失败')
            print(identifier)
            self._db=None
            self._cursor=None
        
    def _dbconnect(self):
        par1=f'DRIVER={self._driver};SERVER={self._dbserver};DATABASE={self._dbname};UID={self._user};PWD={self._password}'
        print(par1)
        try:
            return pyodbc.connect(par1,timeout=self._timeout)           
        except Exception as identifier:
            print('db connect failed')
            print(identifier)
            return None
    @property
    def db(self):
        return self._db
    @property
    def dbCursor(self):
        if self._db is None:
            return None
        else:
            return self._cursor
    def get_drivertype(self):
        return{'mssql':"SQL Server\\"}.get(self._dbtype,'error')#'error'为默认返回值，可自设置
    def insertData(self,sql):
        try:
            self._cursor.execute(sql)
            self._db.commit()
        except Exception as identifier:
            print('数据插入失败')
            print(identifier)
# biblecls=dbcls('mssql','','BIBLE','sa','111',5)
# bibledb=biblecls.db
# cursor=biblecls.dbCursor
# sql="insert into BIBLE.dbo.genesis values(3,2,'werrr')"
# sql="select * from dbo.genesis"
# biblecls.insertData(sql)

# # rs= cursor.fetchall()
# # print(rs[0])
