import tkinter
from tkinter import *
from tkinter import messagebox
import os
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def center_window(root, w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.minsize(w, h)
    root.maxsize(w, h)


def checkusername(username, login):
    if not username:
        return False
    if '\n' in username:
        return False
    userfile = open("user/username.txt", mode='r')
    for i in userfile:
        if i[0: len(i) - 1] == username:
            return login
    return not login


def checkpassword(username, password):
    if not password:
        return False
    uapfile = open('user/uernameandpassword.txt', 'r')
    i = '1'
    while (i):
        i = uapfile.readline()
        k = uapfile.readline()
        if i[0: len(i) - 1] == username:
            if k[0: len(k) - 1] == password:
                return True
            else:
                return False


class index:
    def __init__(self, master):
        self.index = tkinter.Frame()
        self.index.pack()
        global img
        img = PhotoImage(file='img/logo1.gif')
        imglabel = Label(self.index, image=img, compound='center')
        imglabel.grid()
        usernamelabel = Label(self.index, text="用户名", font=("sold", 25))
        usernamelabel.grid(column=0, row=1)
        usernametext = Entry(self.index, font=("sold", 25), width=30)
        usernametext.grid(column=0, row=2)
        passwordlabel = Label(self.index, text="密码", font=("sold", 25))
        passwordlabel.grid(column=0, row=3)
        passwordtext = Entry(self.index, font=("sold", 25), width=30, show="*")
        passwordtext.grid(column=0, row=4)
        blank = Label(self.index, text="", font=("sold", 10))
        blank.grid(column=0, row=5)
        blank = Label(self.index, text="", font=("sold", 10))
        blank.grid(column=0, row=7)
        submit = Button(self.index, font=('sold', 20), width=20, text="登录",
                        command=lambda: self.login(self, usernametext.get(), passwordtext.get()), relief=RIDGE)
        regist = Button(self.index, font=('sold', 20), width=20, text="注册", command=lambda: self.regist(self),
                        relief=RIDGE)
        submit.grid(column=0, row=6)
        regist.grid(column=0, row=8)

    def login(self, master, username, password):
        if checkusername(username, True):
            if checkpassword(username, password):
                self.index.destroy()
                myindex(self, username)
            else:
                messagebox.showinfo("登录失败", "密码错误\n")
        else:
            messagebox.showinfo("登录失败", "用户名不合法或不存在\n")

    def regist(self, master):
        self.index.destroy()
        register(self)


class register:
    def __init__(self, master):
        self.register = tkinter.Frame()
        self.register.pack()
        imglabel = Label(self.register, image=img, compound='center')
        imglabel.grid()
        usernamelabel = Label(self.register, text="用户名", font=("sold", 25))
        usernamelabel.grid(column=0, row=1)
        usernametext = Entry(self.register, font=("sold", 25), width=30)
        usernametext.grid(column=0, row=2)
        passwordlabel = Label(self.register, text="密码", font=("sold", 25))
        passwordlabel.grid(column=0, row=3)
        passwordtext = Entry(self.register, font=("sold", 25), width=30, show="*")
        passwordtext.grid(column=0, row=4)
        blank = Label(self.register, text="", font=("sold", 10))
        blank.grid(column=0, row=5)
        blank = Label(self.register, text="", font=("sold", 10))
        blank.grid(column=0, row=7)
        tryregist = Button(self.register, font=('sold', 20), width=20, text="注册",
                           command=lambda: self.toregist(self, usernametext.get(), passwordtext.get()), relief=RIDGE)

        backindex = Button(self.register, font=('sold', 20), width=20, text="返回主页",
                           command=lambda: self.indexback(self), relief=RIDGE)
        tryregist.grid(column=0, row=6)
        backindex.grid(column=0, row=8)

    def toregist(self, master, username, password):
        if not password:
            messagebox.showinfo("注册失败", "请输入密码\n")
            return
        if checkusername(username, False):
            messagebox.showinfo("注册成功", "你的用户名是%s" % username + ",密码是%s" % password)
            userfile = open("user/username.txt", 'a')
            userfile.write(username + '\n')
            userfile.close()
            uapfile = open('user/uernameandpassword.txt', 'a')
            uapfile.write(username + '\n')
            uapfile.write(password + '\n')
            uapfile.close()
            path = 'user/' + username
            os.mkdir(path)
            file = open('%s/record.txt' % path, 'a')
            file.write('1 1 1')
            file.close()
            file = open('%s/wrongs.txt' % path, 'w')
            file.close()
            file = open('%s/wrongj.txt' % path, 'w')
            file.close()
            file = open('%s/self.txt' % path, 'a')
            file.write('0 0 0 0')
            file.close()
            file = open('%s/statisticss.txt' % path, 'a')
            for i in range(50):
                file.write('0 ')
            file.write('\n')
            file.write('0')
            for i in range(49):
                file.write(' 0')
            file.close()
            file = open('%s/statisticsj.txt' % path, 'a')
            for i in range(50):
                file.write('0 ')
            file.write('\n')
            file.write('0')
            for i in range(49):
                file.write(' 0')
            file.close()
            self.indexback(self)
        else:
            messagebox.showinfo("注册失败", "用户名不合法或已存在\n")

    def indexback(self, master):
        self.register.destroy()
        index(self)


class myindex:
    def __init__(self, master, text):
        self.myindex = tkinter.Frame()
        self.myindex.pack()
        welcome = Label(self.myindex, text="欢迎您", font=("sold", 20), fg='purple')
        welcome.grid(column=0, row=0)
        user = Label(self.myindex, text=text, font=("sold", 20), fg='purple')
        user.grid(column=1, row=0)
        back = Button(self.myindex, text='退出登录', font=('sold', 15), command=lambda: self.indexback(self), relief=RIDGE)
        back.grid(column=2, row=0)
        single = Button(self.myindex, text='单选题', height=8, width=15, font=('sold', 12), bg='skyblue',
                        command=lambda: self.tosingle(self, text, False), relief=RIDGE)
        single.grid(column=0, row=1)
        judge = Button(self.myindex, text='判断题', height=8, width=15, font=('sold', 12), bg='orange',
                       command=lambda: self.tojudgement(self, text, False), relief=RIDGE)
        judge.grid(column=1, row=1)
        qblank = Button(self.myindex, text='简答题', height=8, width=15, font=('sold', 12), bg='pink',
                        command=lambda: self.tobrief(self, text), relief=RIDGE)
        qblank.grid(column=2, row=1)
        wrongs = Button(self.myindex, text='单选错题', height=8, width=15, font=('sold', 12), bg='red', relief=RIDGE,
                        command=lambda: self.tosingle(self, text, True))
        wrongs.grid(column=0, row=2)
        wrongj = Button(self.myindex, text='判断错题', height=8, width=15, font=('sold', 12), bg='red', relief=RIDGE,
                        command=lambda: self.tojudgement(self, text, True))
        wrongj.grid(column=1, row=2)
        store = Button(self.myindex, text='我', height=8, width=15, font=('sold', 12), bg='green', relief=RIDGE,
                       command=lambda: self.toself(self, text))
        store.grid(column=2, row=2)
        statisticss = Button(self.myindex, text='单选正确率', height=8, width=15, font=('sold', 12), bg='grey', relief=RIDGE,
                             command=lambda: self.tostatisticss(self, text))
        statisticss.grid(column=0, row=3)
        statisticsj = Button(self.myindex, text='判断正确率', height=8, width=15, font=('sold', 12), bg='grey', relief=RIDGE,
                             command=lambda: self.tostatisticsj(self, text))
        statisticsj.grid(column=1, row=3)
        store = Button(self.myindex, text='题库', height=8, width=15, font=('sold', 12), bg='brown', relief=RIDGE,
                       command=lambda: self.tostore(self, text))
        store.grid(column=2, row=3)

    def indexback(self, master):
        self.myindex.destroy()
        index(self)

    def tosingle(self, master, username, wrongset):
        self.myindex.destroy()
        mysingle(self, username, wrongset, 0)

    def tojudgement(self, master, username, wrongset):
        self.myindex.destroy()
        myjudgement(self, username, wrongset, 0)

    def tobrief(self, master, username):
        self.myindex.destroy()
        mybrief(self, username, 0)

    def toself(self, master, username):
        self.myindex.destroy()
        myself(self, username)

    def tostatisticss(self, master, username):
        self.myindex.destroy()
        mystatisticss(self, username)

    def tostatisticsj(self, master, username):
        self.myindex.destroy()
        mystatisticsj(self, username)

    def tostore(self, master, username):
        self.myindex.destroy()
        allstore(self, username)


class allstore:
    def __init__(self, master, username):
        self.allstore = tkinter.Frame()
        self.allstore.pack()
        selected = IntVar()
        pa = Radiobutton(self.allstore, text='单选题(共50题)', value=1, variable=selected, font=("sold", 12), wraplength=400)
        pb = Radiobutton(self.allstore, text='判断题(共50题)', value=2, variable=selected, font=("sold", 12), wraplength=400)
        pc = Radiobutton(self.allstore, text='简答题(共20题)', value=3, variable=selected, font=("sold", 12), wraplength=400)
        sign = Label(self.allstore, font=("sold", 25), width=30, text='请输入题号')
        no = Entry(self.allstore, font=("sold", 25), width=30)
        check = Button(self.allstore, text='提交',
                       command=lambda: self.change(self, selected, username, no.get()),
                       relief=RIDGE, font=('sold', 15), width=20)
        pa.grid()
        pb.grid()
        pc.grid()
        sign.grid()
        no.grid()
        check.grid()

    def change(self, master, selected, username, no):
        v = selected.get()
        if v == 0:
            messagebox.showinfo("啊哦", "请选择题目类型\n")
        else:
            try:
                if v == 1:
                    if 0 < int(no) < 50:
                            self.allstore.destroy()
                            mysingle(self, username, False, no)
                elif v == 2:
                    if 0 < int(no) < 50:
                        self.allstore.destroy()
                        myjudgement(self, username, False, no)
                elif v == 3:
                    if 0 < int(no) < 20:
                        self.allstore.destroy()
                        mybrief(self, username, no)
            except BaseException:
                messagebox.showinfo("啊哦", "非法操作\n")


def readrecord(sign, username, wrongset):
    if wrongset:
        if sign == 0:
            record = open('user/%s/wrongs.txt' % username, 'r')
            all = record.readlines()
            record.close()
            if len(all) != 0:
                k = all[0]
                file = open('user/%s/wrongs.txt' % username, 'w')
                for i in all:
                    if i != k:
                        file.write(i)
                file.close()
                return k[0:len(k) - 1]
            return False
        if sign == 1:
            record = open('user/%s/wrongj.txt' % username, 'r')
            all = record.readlines()
            record.close()
            if len(all) != 0:
                k = all[0]
                file = open('user/%s/wrongj.txt' % username, 'w')
                for i in all:
                    if i != k:
                        file.write(i)
                file.close()
                return k[0:len(k) - 1]
            return False
    record = open('user/%s/record.txt' % username, 'r')
    k = record.readline().split(' ')
    return k[sign]


def selfdata(username, ty, right):
    file = open('user/%s/self.txt' % username, 'r')
    k = file.readline().split(' ')
    file.close()
    k[ty * 2] = str(int(k[ty * 2]) + 1)
    k[ty * 2 + 1] = str(int(k[ty * 2 + 1]) + right)
    file = open('user/%s/self.txt' % username, 'w')
    file.write('%s %s %s %s' % (k[0], k[1], k[2], k[3]))
    file.close()


def statistics(username, no, right, ty):
    file = open('user/%s/%s.txt' % (username, ty), 'r')
    k1 = file.readline().split(' ')
    k2 = file.readline().split(' ')
    file.close()
    no = int(no)
    if no == 50:
        k1[no - 1] = str(int(k1[no - 1][0:len(k1[no - 1]) - 1]) + right)
        k1[no - 1] = '%s\n' % k1[no - 1]
    else:
        k1[no - 1] = str(int(k1[no - 1]) + right)
    k2[no - 1] = str(int(k2[no - 1]) + 1)
    file = open('user/%s/%s.txt' % (username, ty), 'w')
    file.write(k1[0])
    for i in range(1, 50):
        file.write(' %s' % k1[i])
    file.write('%s' % k2[0])
    for i in range(1, 50):
        file.write(' %s' % k2[i])
    file.close()


class mysingle:
    def __init__(self, master, username, wrongset, num):
        self.mysingle = tkinter.Frame()
        self.mysingle.pack()
        if num == 0:
            no = readrecord(0, username, wrongset)
        else:
            no = num
        if not no:
            messagebox.showinfo("啊哦", "目前还没有错题\n")
            self.back(self, username)
            return
        problem = open('single/s%s.txt' % no, 'r', encoding='UTF-8')
        p = list()
        for i in problem:
            p.append(i)
        pp = Label(self.mysingle, text=p[0], font=("sold", 12), wraplength=400)
        pp.grid(column=0, row=0)
        selected = IntVar()
        pa = Radiobutton(self.mysingle, text=p[1], value=1, variable=selected, font=("sold", 12), wraplength=400)
        pb = Radiobutton(self.mysingle, text=p[2], value=2, variable=selected, font=("sold", 12), wraplength=400)
        pc = Radiobutton(self.mysingle, text=p[3], value=3, variable=selected, font=("sold", 12), wraplength=400)
        pd = Radiobutton(self.mysingle, text=p[4], value=4, variable=selected, font=("sold", 12), wraplength=400)
        ans = p[5]
        pa.grid(column=0, row=1)
        pb.grid(column=0, row=2)
        pc.grid(column=0, row=3)
        pd.grid(column=0, row=4)
        s = ''
        if int(no) == 50:
            s = '这是最后一题'
        feedback = Label(self.mysingle, text=s, wraplength=400, font=("sold", 12))
        feedback.grid(column=0, row=7)
        check = Button(self.mysingle, text='提交',
                       command=lambda: self.judge(self, selected, pa, pb, pc, pd, ans, feedback, check, username, no,
                                                  wrongset),
                       relief=RIDGE, font=('sold', 15), width=20)
        check.grid(column=0, row=5)
        back = Button(self.mysingle, text='返回', command=lambda: self.back(self, username), relief=RIDGE,
                      font=('sold', 15), width=20)
        back.grid(column=0, row=6)

    def judge(self, master, selected, pa, pb, pc, pd, ans, feedback, check, username, no, wrongset):
        v = selected.get()
        if not v:
            messagebox.showinfo("提交失败", "请选择答案\n")
            return
        if int(ans) == 1:
            pa.configure(bg='green')
        elif int(ans) == 2:
            pb.configure(bg='green')
        elif int(ans) == 3:
            pc.configure(bg='green')
        elif int(ans) == 4:
            pd.configure(bg='green')
        if int(v) == int(ans):
            feedback.configure(text='回答正确', fg='green')
            selfdata(username, 0, 1)
            statistics(username, no, 1, 'statisticss')
            file = open('user/%s/wrongs.txt' % username, 'r')
            k = file.readlines()
            file.close()
            s = no + '\n'
            file = open('user/%s/wrongs.txt' % username, 'w')
            for i in k:
                if i != s:
                    file.write(i)
            file.close()
        else:
            feedback.configure(text='回答错误', fg='red')
            selfdata(username, 0, 0)
            statistics(username, no, 0, 'statisticss')
            file = open('user/%s/wrongs.txt' % username, 'r')
            k = file.readlines()
            file.close()
            s = no + '\n'
            exist = False
            for i in k:
                if i == s:
                    exist = True
            if not exist:
                file = open('user/%s/wrongs.txt' % username, 'a')
                file.write('%s\n' % no)
                file.close()
            if v == 1:
                pa.configure(bg='red')
            elif v == 2:
                pb.configure(bg='red')
            elif v == 3:
                pc.configure(bg='red')
            elif v == 4:
                pd.configure(bg='red')
        check.configure(text='下一题', command=lambda: self.nextq(self, username, no, wrongset), relief=RIDGE)

    def nextq(self, master, username, no, wrongset):
        if not wrongset:
            record = open('user/%s/record.txt' % username, 'r')
            k = record.readline().split(' ')
            record.close()
            record = open('user/%s/record.txt' % username, 'w+')
            nextone = int(no) + 1
            if nextone == 51:
                nextone = 1
            k[0] = str(nextone)
            record.write("%s %s %s" % (k[0], k[1], k[2]))
            record.close()
        self.mysingle.destroy()
        mysingle(self, username, wrongset, 0)

    def back(self, master, username):
        self.mysingle.destroy()
        myindex(self, username)


class myjudgement:
    def __init__(self, master, username, wrongset, num):
        self.myjudgement = tkinter.Frame()
        self.myjudgement.pack()
        if num == 0:
            no = readrecord(1, username, wrongset)
        else:
            no = num
        if not no:
            messagebox.showinfo("啊哦", "目前还没有错题\n")
            self.back(self, username)
            return
        problem = open('judgement/j%s.txt' % no, 'r', encoding='UTF-8')
        p = list()
        for i in problem:
            p.append(i)
        pp = Label(self.myjudgement, text=p[0], font=("sold", 12), wraplength=400)
        pp.grid(column=0, row=0)
        ans = p[1][0]
        explain = ''
        if len(p) == 3:
            explain = p[2]
        selected = IntVar()
        pr = Radiobutton(self.myjudgement, text='正确', value=1, variable=selected, font=("sold", 12), wraplength=400)
        pw = Radiobutton(self.myjudgement, text='错误', value=2, variable=selected, font=("sold", 12), wraplength=400)
        pr.grid(column=0, row=1)
        pw.grid(column=0, row=2)
        s = ''
        if int(no) == 50:
            s = '这是最后一题'
        feedback = Label(self.myjudgement, text=s, wraplength=400, font=("sold", 12))
        feedback.grid(column=0, row=5)
        check = Button(self.myjudgement, text='提交',
                       command=lambda: self.judge(self, selected, pr, pw, ans, explain, feedback, check, username, no,
                                                  wrongset),
                       relief=RIDGE, font=('sold', 15), width=20)
        check.grid(column=0, row=3)
        back = Button(self.myjudgement, text='返回', command=lambda: self.back(self, username), relief=RIDGE,
                      font=('sold', 15), width=20)
        back.grid(column=0, row=4)

    def judge(self, master, selected, pr, pw, ans, explain, feedback, check, username, no, wrongset):
        v = selected.get()
        if not v:
            messagebox.showinfo("提交失败", "请选择答案\n")
            return
        if int(ans) == 1:
            pr.configure(bg='green')
        elif int(ans) == 2:
            pw.configure(bg='green')
        if int(v) == int(ans):
            feedback.configure(text='回答正确, %s' % explain, fg='green')
            selfdata(username, 1, 1)
            statistics(username, no, 1, 'statisticsj')
            file = open('user/%s/wrongj.txt' % username, 'r')
            k = file.readlines()
            file.close()
            s = no + '\n'
            file = open('user/%s/wrongj.txt' % username, 'w')
            for i in k:
                if i != s:
                    file.write(i)
            file.close()
        else:
            feedback.configure(text='回答错误, %s' % explain, fg='red')
            selfdata(username, 1, 0)
            statistics(username, no, 0, 'statisticsj')
            file = open('user/%s/wrongj.txt' % username, 'r')
            k = file.readlines()
            file.close()
            s = no + '\n'
            exist = False
            for i in k:
                if i == s:
                    exist = True
            if not exist:
                file = open('user/%s/wrongj.txt' % username, 'a')
                file.write('%s\n' % no)
                file.close()
            if v == 1:
                pr.configure(bg='red')
            elif v == 2:
                pw.configure(bg='red')
        check.configure(text='下一题', command=lambda: self.nextq(self, username, no, wrongset))

    def nextq(self, master, username, no, wrongset):
        if not wrongset:
            record = open('user/%s/record.txt' % username, 'r')
            k = record.readline().split(' ')
            record.close()
            record = open('user/%s/record.txt' % username, 'w+')
            nextone = int(no) + 1
            if nextone == 51:
                nextone = 1
            k[1] = str(nextone)
            record.write("%s %s %s" % (k[0], k[1], k[2]))
            record.close()
        self.myjudgement.destroy()
        myjudgement(self, username, wrongset, 0)

    def back(self, master, username):
        self.myjudgement.destroy()
        myindex(self, username)


class mybrief:
    def __init__(self, master, username, num):
        self.mybrief = tkinter.Frame()
        self.mybrief.pack()
        if num == 0:
            no = readrecord(2, username, False)
        else:
            no = num
        problem = open('brief/b%s.txt' % no, 'r', encoding='UTF-8')
        p = list()
        for i in problem:
            p.append(i)
        pp = Label(self.mybrief, text=p[0], font=("sold", 12), wraplength=400)
        pp.grid(column=0, row=0)
        myanswer = Entry(self.mybrief, font=("sold", 25), width=30, justify=LEFT)
        myanswer.grid(column=0, row=1)
        s = ''
        if int(no) == 20:
            s = '这是最后一题'
        check = Button(self.mybrief, text='提交',
                       command=lambda: self.judge(self, feedback, check, username, no, p[1]), relief=RIDGE
                       , font=('sold', 15), width=20)
        check.grid(column=0, row=2)
        back = Button(self.mybrief, text='返回', command=lambda: self.back(self, username), relief=RIDGE
                      , font=('sold', 15), width=20)
        back.grid(column=0, row=3)
        feedback = Label(self.mybrief, text=s, wraplength=400, font=("sold", 12), justify=LEFT)
        feedback.grid(column=0, row=4)

    def back(self, master, username):
        self.mybrief.destroy()
        myindex(self, username)

    def judge(self, master, feedback, check, username, no, answer):
        feedback.configure(text=answer)
        check.configure(text='下一题', command=lambda: self.nextq(self, username, no))

    def nextq(self, master, username, no):
        record = open('user/%s/record.txt' % username, 'r')
        k = record.readline().split(' ')
        record.close()
        record = open('user/%s/record.txt' % username, 'w+')
        nextone = int(no) + 1
        if nextone == 21:
            nextone = 1
        k[2] = str(nextone)
        record.write("%s %s %s" % (k[0], k[1], k[2]))
        record.close()
        self.mybrief.destroy()
        mybrief(self, username, 0)


class myself:
    def __init__(self, master, username):
        self.myself = tkinter.Frame()
        self.myself.pack()
        file = open('user/%s/self.txt' % username, 'r')
        k = file.readline().split(' ')
        label = Label(self.myself,
                      text="%s\n你一共完成了%s道单选题，其中正确%s道\n你一共完成了%s道判断题，其中正确%s道" % (username, k[0], k[1], k[2], k[3]),
                      font=("sold", 25), wraplength=400)
        label.grid()
        back = Button(self.myself, text='返回', command=lambda: self.back(self, username), relief=RIDGE,
                      font=('sold', 15), width=20)
        back.grid()

    def back(self, master, username):
        self.myself.destroy()
        myindex(self, username)


class mystatisticss:
    def __init__(self, master, username):
        self.mystatisticss = tkinter.Frame()
        self.mystatisticss.pack()
        file = open('user/%s/%s.txt' % (username, 'statisticss'), 'r')
        k1 = list(map(int, file.readline().split(' ')[0:50]))
        k2 = list(map(int, file.readline().split(' ')))
        file.close()
        y = list()
        x = list()
        for i in range(50):
            x.append(i + 1)
            if k2[i] == 0:
                y.append(0)
            else:
                y.append(k1[i] / k2[i])
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        a.plot(x, y)
        f.supylabel('Correct rate')
        f.supxlabel('no')
        c = FigureCanvasTkAgg(f, main)
        c.draw()
        c.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(c, main)
        toolbar.update()
        back = Button(self.mystatisticss, text='返回', command=lambda: self.back(self, username, c, toolbar),
                      relief=RIDGE,
                      font=('sold', 15), width=20)
        back.grid()

    def back(self, master, username, c, toolbar):
        c.get_tk_widget().destroy()
        toolbar.destroy()
        self.mystatisticss.destroy()
        myindex(self, username)


class mystatisticsj:
    def __init__(self, master, username):
        self.mystatisticsj = tkinter.Frame()
        self.mystatisticsj.pack()
        file = open('user/%s/%s.txt' % (username, 'statisticsj'), 'r')
        k1 = list(map(int, file.readline().split(' ')[0:50]))
        k2 = list(map(int, file.readline().split(' ')))
        file.close()
        y = list()
        x = list()
        for i in range(50):
            x.append(i + 1)
            if k2[i] == 0:
                y.append(0)
            else:
                y.append(k1[i] / k2[i])
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        a.bar(x, y)
        f.supylabel('Correct rate')
        f.supxlabel('no')
        c = FigureCanvasTkAgg(f, main)
        c.draw()
        c.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(c, main)
        toolbar.update()
        back = Button(self.mystatisticsj, text='返回', command=lambda: self.back(self, username, c, toolbar),
                      relief=RIDGE,
                      font=('sold', 15), width=20)
        back.grid()

    def back(self, master, username, c, toolbar):
        c.get_tk_widget().destroy()
        toolbar.destroy()
        self.mystatisticsj.destroy()
        myindex(self, username)


if __name__ == '__main__':
    main = tkinter.Tk(className='python小助手')
    center_window(main, 500, 500)
    index(main)
    main.mainloop()
