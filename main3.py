#导入mx模块
import wx
import wx.grid
from db import Sql_operation



class UserOperation(wx.Frame):
    '''
    操作界面
    '''
    def __init__(self,*args,**kw):
        # ensure the parent's __init__ is called
        super(UserOperation,self).__init__(*args, **kw)
        #设置窗口屏幕居中
        self.Center()
        #创建窗口
        self.pnl = wx.Panel(self)
        #调用操作界面函数
        self.OperationInterface()

    def OperationInterface(self):
        #创建垂直方向box布局管理器
        self.vbox = wx.BoxSizer(wx.VERTICAL) 
        #################################################################################
        #创建logo静态文本，设置字体属性
        logo = wx.StaticText(self.pnl,label="论文管理系统(普通用户)")
        font = logo.GetFont()
        font.PointSize += 30
        font = font.Bold()
        logo.SetFont(font)
        #添加logo静态文本到vbox布局管理器
        self.vbox.Add(logo,proportion=0,flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border=5)
        #################################################################################
        #创建静态框
        sb_button = wx.StaticBox(self.pnl,label="选择操作")
        #创建垂直方向box布局管理器
        vsbox_button = wx.StaticBoxSizer(sb_button,wx.VERTICAL)
        #创建操作按钮、绑定事件处理
        check_button = wx.Button(self.pnl,id=10,label="查看论文信息",size=(150,50))
        add_button = wx.Button(self.pnl,id=11,label="添加论文信息",size=(150,50))
        #delete_button = wx.Button(self.pnl,id=12,label="删除论文信息",size=(150,50))
        quit_button = wx.Button(self.pnl,id=13,label="退出系统",size=(150,50))
        self.Bind(wx.EVT_BUTTON,self.ClickButton,id=10,id2=13)
        #添加操作按钮到vsbox布局管理器
        vsbox_button.Add(check_button,0,wx.EXPAND | wx.BOTTOM,40)
        vsbox_button.Add(add_button,0,wx.EXPAND | wx.BOTTOM,40)
        #vsbox_button.Add(delete_button,0,wx.EXPAND | wx.BOTTOM,40)
        vsbox_button.Add(quit_button,0,wx.EXPAND | wx.BOTTOM,200) 
        #创建静态框
        sb_show_operation = wx.StaticBox(self.pnl,label="显示/操作窗口",size=(800,800))
        #创建垂直方向box布局管理器
        self.vsbox_show_operation = wx.StaticBoxSizer(sb_show_operation,wx.VERTICAL)
        #创建水平方向box布局管理器
        hbox = wx.BoxSizer()
        hbox.Add(vsbox_button,0,wx.EXPAND | wx.BOTTOM,5)
        hbox.Add(self.vsbox_show_operation,0,wx.EXPAND | wx.BOTTOM,5)
        #将hbox添加到垂直box 
        self.vbox.Add(hbox,proportion=0,flag=wx.CENTER) 
        #################################################################################
        self.pnl.SetSizer(self.vbox)
    
    def ClickButton(self,event):
        source_id = event.GetId()
        if source_id == 10:
            print("查询操作！")
            inquire_button = InquireOp(None,title="论文管理系统(普通用户)",size=(1024,668))
            inquire_button.Show()
            self.Close(True) 
        elif source_id == 11:
            print("添加操作！")
            add_button = AddOp(None,title="论文管理系统(普通用户)",size=(1024,668))
            add_button.Show()
            self.Close(True) 
        elif source_id == 12:
            print("删除操作！")
            del_button = DelOp(None,title="论文管理系统(普通用户)",size=(1024,668))
            del_button.Show()
            self.Close(True) 
        elif source_id == 13:
            self.Close(True)

#继承UserOperation类，实现初始化操作界面
class InquireOp(UserOperation):
    def __init__(self,*args,**kw):
        # ensure the parent's __init__ is called
        super(InquireOp,self).__init__(*args, **kw)
        #创建论文列表信息网格
        self.stu_grid = self.CreateGrid()
        self.stu_grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.OnLabelleftClick)
        #添加到vsbox_show_operation布局管理器
        self.vsbox_show_operation.Add(self.stu_grid,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,30) 
        
    def ClickButton(self,event):
        source_id = event.GetId()
        if source_id == 10:
            pass 
        elif source_id == 11:
            print("添加操作！")
            add_button = AddOp(None,title="论文管理系统(普通用户)",size=(1024,668))
            add_button.Show()
            self.Close(True) 
        elif source_id == 12:
            print("删除操作！")
            del_button = DelOp(None,title="论文管理系统(普通用户)",size=(1024,668))
            del_button.Show()
            self.Close(True) 
        elif source_id == 13:
            self.Close(True)
        
    def CreateGrid(self):
        #连接student_db数据库
        op = Sql_operation("student_db")
        #获取Paper表中的论文信息，返回为二维元组
        np = op.FindAll("Paper")
        column_names = ("Papername","author","date","keyword","abstract","journal")
        stu_grid = wx.grid.Grid(self.pnl)
        stu_grid.CreateGrid(len(np),len(np[0])-1)
        for row in range(len(np)):
            stu_grid.SetRowLabelValue(row,str(np[row][0]))#确保网格序列号与数据库id保持一致
        for col in range(1,len(np[row])):
            stu_grid.SetColLabelValue(col-1,column_names[col-1]) #设置col名称
            stu_grid.SetCellValue(row,col-1,str(np[row][col])) #设置单元格
            stu_grid.AutoSize()
        return stu_grid
    
    def OnLabelleftClick(self,event):
        #连接student_db数据库
        op = Sql_operation("student_db")
        #获取users表中的用户名和密码信息，返回为二维元组
        np = op.FindAll("users")
        print("RowIdx: {0}".format(event.GetRow()))
        print("ColIdx: {0}".format(event.GetRow()))
        print(np[event.GetRow()])
        event.Skip()

#继承UserOperation类，实现初始化操作界面
class AddOp(UserOperation):
    def __init__(self,*args,**kw):
        # ensure the parent's __init__ is called
        super(AddOp,self).__init__(*args, **kw)
        #创建添加论文息输入框、添加按钮
        self.id = wx.TextCtrl(self.pnl,size = (210,25))
        self.Papername = wx.TextCtrl(self.pnl,size = (210,25))
        self.author = wx.TextCtrl(self.pnl,size = (210,25))
        self.date = wx.TextCtrl(self.pnl,size = (210,25))
        self.keyword = wx.TextCtrl(self.pnl,size = (210,25))
        self.abstract = wx.TextCtrl(self.pnl,size = (210,25))
        self.journal = wx.TextCtrl(self.pnl,size = (210,25))
        self.add_affirm = wx.Button(self.pnl,label="添加",size=(80,25))
        #为添加按钮组件绑定事件处理
        self.add_affirm.Bind(wx.EVT_BUTTON,self.AddAffirm)
        #################################################################################
        #创建静态框
        sb_id = wx.StaticBox(self.pnl,label="id")
        sb_name = wx.StaticBox(self.pnl,label="Papername")
        sb_gender = wx.StaticBox(self.pnl,label="author")
        sb_age = wx.StaticBox(self.pnl,label="date")
        sb_cid = wx.StaticBox(self.pnl,label="keyword")
        sb_classid = wx.StaticBox(self.pnl,label="abstract")
        sb_phone = wx.StaticBox(self.pnl,label="journal") 
        #创建水平方向box布局管理器
        hsbox_id = wx.StaticBoxSizer(sb_id,wx.HORIZONTAL)
        hsbox_name = wx.StaticBoxSizer(sb_name,wx.HORIZONTAL)
        hsbox_gender = wx.StaticBoxSizer(sb_gender,wx.HORIZONTAL)
        hsbox_age = wx.StaticBoxSizer(sb_age,wx.HORIZONTAL)
        hsbox_cid = wx.StaticBoxSizer(sb_cid,wx.HORIZONTAL)
        hsbox_classid = wx.StaticBoxSizer(sb_classid,wx.HORIZONTAL)
        hsbox_phone = wx.StaticBoxSizer(sb_phone,wx.HORIZONTAL)
        #添加到hsbox布局管理器
        hsbox_id.Add(self.id,0,wx.EXPAND | wx.BOTTOM,5)
        hsbox_name.Add(self.Papername,0,wx.EXPAND | wx.BOTTOM,5)
        hsbox_gender.Add(self.author,0,wx.EXPAND | wx.BOTTOM,5)
        hsbox_age.Add(self.date,0,wx.EXPAND | wx.BOTTOM,5)
        hsbox_cid.Add(self.keyword,0,wx.EXPAND | wx.BOTTOM,5)
        hsbox_classid.Add(self.abstract,0,wx.EXPAND | wx.BOTTOM,5)
        hsbox_phone.Add(self.journal,0,wx.EXPAND | wx.BOTTOM,5)
        #################################################################################
        #添加到vsbox_show_operation布局管理器
        self.vsbox_show_operation.Add(hsbox_id,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
        self.vsbox_show_operation.Add(hsbox_name,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
        self.vsbox_show_operation.Add(hsbox_gender,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
        self.vsbox_show_operation.Add(hsbox_age,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
        self.vsbox_show_operation.Add(hsbox_cid,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
        self.vsbox_show_operation.Add(hsbox_classid,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
        self.vsbox_show_operation.Add(hsbox_phone,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
        self.vsbox_show_operation.Add(self.add_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

    def ClickButton(self,event):
        source_id = event.GetId()
        if source_id == 10:
            print("查询操作！")
            inquire_button = InquireOp(None,title="论文管理系统(普通用户)",size=(1024,668))
            inquire_button.Show()
            self.Close(True) 
        elif source_id == 11:
            pass 
        elif source_id == 12:
            print("删除操作！")
            del_button = DelOp(None,title="论文管理系统(普通用户)",size=(1024,668))
            del_button.Show()
            self.Close(True) 
        elif source_id == 13:
            elf.Close(True)
    
    def AddAffirm(self,event):
        #连接student_db数据库
        op = Sql_operation("student_db")
        #向Paper表添加论文信息
        Papername = self.Papername.GetValue()
        print(Papername)
        author = self.author.GetValue()
        print(author)
        date = self.date.GetValue()
        print(date)
        keyword = self.keyword.GetValue()
        print(keyword)
        abstract = self.abstract.GetValue()
        print(abstract)
        journal = self.journal.GetValue()
        print(journal)
        #np = op.Insert(Papername,author,date,keyword,abstract,journal)
        id = self.id.GetValue()
        print(id)
        np = op.Insert(Papername,author,date,keyword,abstract,journal,id)

#继承InquireOp类，实现初始化操作界面
# class DelOp(InquireOp):
 # def __init__(self,*args,**kw):
 # # ensure the parent's __init__ is called
 # super(DelOp,self).__init__(*args, **kw)
 # #创建删除学员信息输入框、删除按钮
 # self.del_id = wx.TextCtrl(self.pnl,pos = (407,78),size = (210,25))
 # self.del_affirm = wx.Button(self.pnl,label="删除",pos=(625,78),size=(80,25))
 # #为删除按钮组件绑定事件处理
 # self.del_affirm.Bind(wx.EVT_BUTTON,self.DelAffirm)
 # #################################################################################
 # #创建静态框
 # sb_del = wx.StaticBox(self.pnl,label="请输入需要删除的论文的ID")
 # #创建水平方向box布局管理器
 # hsbox_del = wx.StaticBoxSizer(sb_del,wx.HORIZONTAL)
 # #添加到hsbox_name布局管理器
 # hsbox_del.Add(self.del_id,0,wx.EXPAND | wx.BOTTOM,5)
 # #添加到vsbox_show_operation布局管理器
 # self.vsbox_show_operation.Add(hsbox_del,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
 # self.vsbox_show_operation.Add(self.del_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

 # def ClickButton(self,event):
 # source_id = event.GetId()
 # if source_id == 10:
 # print("查询操作！")
 # inquire_button = InquireOp(None,title="论文管理系统",size=(1024,668))
 # inquire_button.Show()
 # self.Close(True) 
 # elif source_id == 11:
 # print("添加操作！")
 # add_button = AddOp(None,title="论文管理系统",size=(1024,668))
 # add_button.Show()
 # self.Close(True) 
 # elif source_id == 12:
 # pass 
 # elif source_id == 13:
 # self.Close(True)

 # def DelAffirm(self,event):
 # #连接student_db数据库
 # op = Sql_operation("student_db")

 # del_id = self.del_id.GetValue()
 # print(del_id)
 # np = op.Del(int(del_id))
 
 # del_button = DelOp(None,title="论文管理系统",size=(1024,668))
 # del_button.Show()
 # self.Close(True)

if __name__ == '__main__':
     app = wx.App()
     operation = UserOperation(None,title="论文管理系统(普通用户)",size=(1024,668))
     #login = UserLogin(None,title="论文管理系统",size=(1024,668))
     operation.Show()
     app.MainLoop()