import pymysql


# 创建数据库操作类
class Sql_operation(object):
    '''
    数据库操作
    '''

    # 用构造函数实现数据库连接，并引入mydb参数，实现调用不同的数据库
    def __init__(self, mydb):

        # 实例变量
        self.mydb = mydb
        # 打开数据库连接
        self.db = pymysql.connect(host="localhost", user="root", password="1234", db=self.mydb, charset="utf8")
        # 创建游标对象
        self.cursor = self.db.cursor()

    # 定义查看数据表信息函数，并引入table_field、table_name参数，实现查看不同数据表的建表语句
    def FindAll(self, table_name):

    # 实例变量
        self.table_name = table_name
        # 定义SQL语句
        sql = "select * from %s" % (self.table_name)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 处理结果
            data = self.cursor.fetchall()
            return data
        except Exception as err:
            print("SQL执行错误，原因：", err)
            
    def FindNewest(self, table_name = 'machines'):

    # 实例变量
        self.table_name = table_name
        # 定义SQL语句
        sql = "select * from (select *,rank() over(partition by machine_id order by upload_date desc) `ranked` from %s) `s1` where s1.ranked = 1" % (self.table_name)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 处理结果
            data = self.cursor.fetchall()
            return data
        except Exception as err:
            print("SQL执行错误，原因：", err)

    # 定义添加表数据函数
    def InsertUser(self, user_name, user_password):
        id = 1

        self.user_name = user_name
        self.user_password = user_password

        sql = "insert into users(id,user_name,user_password)values('%s','%s','%s')" % (
        int(id), self.user_name, self.user_password)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
        # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)
#变量名称问题调整
    def Insert(self, papername, author, date,keyword,abstract,journal,paperid):

        # 实例变量
        self.papername = papername
        self.author= author
        self.date = date
        self.keyword = keyword
        self.abstract = abstract
        self.journal = journal
        self.paperid = paperid
        # 定义SQL语句
        sql = "insert into Paper(Papername,author,date,keyword,abstract,journal,id) values('%s','%s','%s','%s','%s','%s','%d')" % (
        self.papername, self.author, self.date, self.keyword, self.abstract, self.journal, int(self.paperid))
        try:
        # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
        # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)

    # 定义删除表数据函数
    def Del(self, paperid):

        # 实例变量
        self.paperid = paperid
        # 定义SQL语句
        sql = "delete from Paper where id=%d" % (self.paperid)
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
        # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)

    # 定义修改表数据函数
    def Update(self, id, amend_name, amend_value):
        self.id = id

        self.amend_name = amend_name
        self.amend_value = amend_value

        sql = "update Paper set %s=%s where id=%d" % (self.amend_name, self.amend_value, int(self.id))

        try:
        # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
        # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)

    # 用析构函数实现数据库关闭
    def __del__(self):

    # 关闭数据库连接
        self.db.close()

a = Sql_operation('ima')
res = a.FindNewest('machines')
print(res)







