import sys
import random
import time
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import *
import csv
import sqlite3
from PyQt5.QtGui import QPixmap

savefon = ['+', ' ', ' ', ' ']
savepref = ['+', ' ', ' ', ' ']
countbal = 0
wasquest = []


class Lose(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'Templates\neverno.ui', self)
        global wasquest
        wasquest = []
        self.gamed = open('game.txt', 'r', encoding='utf-8')
        self.dr = open('datarecords.txt', 'r', encoding='utf-8')
        self.balls = open('balls.txt', 'r', encoding='utf-8')
        self.nowballs = int(self.balls.read())
        self.balls.close()
        self.bballs = open('balls.txt', 'w', encoding='utf-8')
        self.nowballs += 1
        print(self.nowballs, file=self.bballs)
        self.bballs.close()
        self.resindata = self.dr.read()
        self.intdata = int(self.resindata)
        self.res = self.gamed.readlines()
        self.vuvodresa.display(len(self.res))
        if self.intdata < len(self.res):
            self.dr.close()
            self.op = open('datarecords.txt', 'w', encoding='utf-8')
            print(len(self.res), file=self.op)
            self.op.close()
        self.gamed.close()
        self.gamed1 = open('game.txt', 'w', encoding='utf-8')
        self.gamed1.close()
        self.naglavn.clicked.connect(self.naglav)

    def naglav(self):
        global ex
        ex = StartGame()
        ex.show()


class Game(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(r'Templates\game.ui', self)
        global wasquest
        f1 = open('data.txt', 'r', encoding='utf-8')
        self.gamedata = open('game.txt', 'a', encoding='utf-8')
        self.voprosu = f1.readlines()
        self.mx = len(self.voprosu)
        self.per = True
        # ========================================================
        while self.per:
            self.pislo = random.randint(0, self.mx - 1)
            self.vopr = self.voprosu[self.pislo].split(' : ')
            self.questionlabel.setText(self.vopr[0] + '?')
            self.pravotvet = self.vopr[1]
            self.otvetu = self.vopr[1:]
            if self.vopr[0] in wasquest:
                continue
            else:
                self.per = False
        random.shuffle(self.otvetu)
        self.gb1.setText(self.otvetu[0].strip())
        self.per1 = self.otvetu[0].strip()
        self.gb2.setText(self.otvetu[1].strip())
        self.per2 = self.otvetu[1].strip()
        self.gb3.setText(self.otvetu[2].strip())
        self.per3 = self.otvetu[2].strip()
        self.gb4.setText(self.otvetu[3].strip())
        self.per4 = self.otvetu[3].strip()
        self.gb1.clicked.connect(self.provotv1)
        self.gb2.clicked.connect(self.provotv2)
        self.gb3.clicked.connect(self.provotv3)
        self.gb4.clicked.connect(self.provotv4)

    def provotv1(self):
        global ex
        if self.per1.strip() == self.pravotvet.strip():
            print(1, file=self.gamedata)
            self.gamedata.close()
            self.gb1.setStyleSheet("background-color : green")
            time.sleep(1)
            ex = Game()
            ex.show()
        elif self.per1.strip() != self.pravotvet.strip():
            self.gamedata.close()
            self.gb1.setStyleSheet("background-color : red")
            time.sleep(1)
            ex = Lose()
            ex.show()

    def provotv2(self):
        global ex
        if self.per2.strip() == self.pravotvet.strip():
            print(1, file=self.gamedata)
            self.gamedata.close()
            self.gb2.setStyleSheet("background-color : green")
            time.sleep(1)
            ex = Game()
            ex.show()
        elif self.per2.strip() != self.pravotvet.strip():
            self.gamedata.close()
            self.gb2.setStyleSheet("background-color : red")
            time.sleep(1)
            ex = Lose()
            ex.show()

    def provotv3(self):
        global ex
        if self.per3.strip() == self.pravotvet.strip():
            print(1, file=self.gamedata)
            self.gamedata.close()
            self.gb3.setStyleSheet("background-color : green")
            time.sleep(1)
            ex = Game()
            ex.show()
        elif self.per3.strip() != self.pravotvet.strip():
            self.gamedata.close()
            self.gb3.setStyleSheet("background-color : red")
            time.sleep(1)
            ex = Lose()
            ex.show()

    def provotv4(self):
        global ex
        if self.per4.strip() == self.pravotvet.strip():
            print(1, file=self.gamedata)
            self.gamedata.close()
            self.gb4.setStyleSheet("background-color : green")
            time.sleep(1)
            ex = Game()
            ex.show()
        elif self.per4.strip() != self.pravotvet.strip():
            self.gamedata.close()
            self.gb4.setStyleSheet("background-color : red")
            time.sleep(1)
            ex = Lose()
            ex.show()


class Error(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 340, 80)
        self.setWindowTitle('ОШИБКА')
        self.lbl = QLabel(' В базе нет вопросов!', self)
        self.lbl.setFont(QFont(u"Times New Roman", 20))


class Pers(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'Templates\per.ui', self)
        with open('about.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                if index == 1:
                    self.name1 = row[0]
                    self.surname1 = row[1]
                    self.city1 = row[2]
                    self.age1 = row[3]
                    self.nick1 = row[4]
        self.vname.setText(self.name1)
        self.vsur.setText(self.surname1)
        self.vcity.setText(self.city1)
        self.vage.setText(self.age1)
        self.vnik.setText(self.nick1)
        self.fff = open('filename.txt', 'r', encoding='utf-8')
        self.avatarname = str(self.fff.readline())
        if len(self.avatarname) == 1:
            self.pixmap = QPixmap('defavatar.png')
        else:
            self.pixmap = QPixmap(self.avatarname)
        self.image = QLabel(self)
        self.image.move(570, 50)
        self.image.resize(140, 196)
        self.image.setPixmap(self.pixmap)
        self.image.setScaledContents(True)
        self.fff.close()
        self.vnizm.clicked.connect(self.izm)
        self.backg.clicked.connect(self.bb)
        self.dobavatar.clicked.connect(self.izmphoto)

    def izmphoto(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.fi = open('filename.txt', 'w', encoding='utf-8')
        print(fname, file=self.fi, end='')
        self.fi.close()
        global ex
        ex = Pers()
        ex.show()

    def izm(self):
        self.na = self.vname.text()
        self.ss = self.vsur.text()
        self.cc = self.vcity.text()
        self.aa = self.vage.text()
        self.nn = self.vnik.text()
        if (self.na == '') or (self.nn == '') or (self.aa == '') or (self.ss == '') or (self.cc == ''):
            self.osh.setText('Введены не все данные')
        else:
            with open('about.csv', 'w', newline='') as csvfile1:
                writer1 = csv.writer(
                    csvfile1, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer1.writerow(['name', 'surname', 'city', 'age', 'nick'])
                writer1.writerow([self.na, self.ss, self.cc, self.aa, self.nn])

    def bb(self):
        global ex
        ex = StartGame()
        ex.show()


class Shop(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'Templates\shop.ui', self)
        global savefon
        global savepref
        savefon = open('fonnow.txt', 'r', encoding='utf-8').readline().split(':')
        savepref = open('prefnow.txt', 'r', encoding='utf-8').readline().split(':')
        self.savefon = savefon
        self.savepref = savepref
        self.fs1 = savefon[0]
        self.fs2 = savefon[1]
        self.fs3 = savefon[2]
        self.fs4 = savefon[3]
        self.ps1 = savepref[0]
        self.ps2 = savepref[1]
        self.ps3 = savepref[2]
        self.ps4 = savepref[3]
        self.phh1.setText(self.fs1)
        self.phh2.setText(self.fs2)
        self.phh3.setText(self.fs3)
        self.phh4.setText(self.fs4)
        self.pree1.setText(self.ps1)
        self.pree2.setText(self.ps2)
        self.pree3.setText(self.ps3)
        self.pree4.setText(self.ps4)
        self.pixmap11 = QPixmap(r'fons\fon1.jpg')
        self.ii2.setPixmap(self.pixmap11)
        self.ii2.setScaledContents(True)
        self.pixmap22 = QPixmap(r'fons\fon2.jpg')
        self.ii3.setPixmap(self.pixmap22)
        self.ii3.setScaledContents(True)
        self.pixmap33 = QPixmap(r'fons\fon3.jpeg')
        self.ii4.setPixmap(self.pixmap33)
        self.ii4.setScaledContents(True)

        self.ph1.clicked.connect(self.p1)
        self.ph2.clicked.connect(self.p2)
        self.ph3.clicked.connect(self.p3)
        self.ph4.clicked.connect(self.p4)
        self.pre1.clicked.connect(self.pr1)
        self.pre2.clicked.connect(self.pr2)
        self.pre3.clicked.connect(self.pr3)
        self.pre4.clicked.connect(self.pr4)
        self.gomenu.clicked.connect(self.gm)

    def p1(self):
        with open('fonnow.txt', 'w', encoding='utf-8') as writefon:
            print('+: : : ', file=writefon)
        self.phh1.setText('+')
        self.phh2.setText(' ')
        self.phh3.setText(' ')
        self.phh4.setText(' ')
        self.errorbals.setText('')
        with open('fon.txt', 'w', encoding='utf-8') as fontxt:
            print('', file=fontxt, end='')

    def p2(self):
        global savefon
        global countbal
        if self.savefon == [' ', '+', ' ', ' ']:
            self.errorbals.setText('Данный предмет уже выбран')

        elif countbal >= 15:
            with open('fonnow.txt', 'w', encoding='utf-8') as writefon:
                print(' :+: : ', file=writefon)
            self.phh1.setText(' ')
            self.phh2.setText('+')
            self.phh3.setText(' ')
            self.phh4.setText(' ')
            self.errorbals.setText(' ')
            with open('fon.txt', 'w', encoding='utf-8') as fontxt:
                print(r'fons\fon1.jpg', file=fontxt, end='')
        else:
            self.errorbals.setText('Недостаточно баллов')


    def p3(self):
        global savefon
        global countbal
        if self.savefon == [' ', ' ', '+', ' ']:
            self.errorbals.setText('Данный предмет уже выбран')

        elif countbal >= 35:
            with open('fonnow.txt', 'w', encoding='utf-8') as writefon:
                print(' : :+: ', file=writefon)
            self.phh1.setText(' ')
            self.phh2.setText(' ')
            self.phh3.setText('+')
            self.phh4.setText(' ')
            self.errorbals.setText(' ')
            with open('fon.txt', 'w', encoding='utf-8') as fontxt:
                print(r'fons\fon2.jpg', file=fontxt, end='')
        else:
            self.errorbals.setText('Недостаточно баллов')


    def p4(self):
        global savefon
        global countbal
        if self.savefon == [' ', ' ', ' ', '+']:
            self.errorbals.setText('Данный предмет уже выбран')

        elif countbal >= 55:
            with open('fonnow.txt', 'w', encoding='utf-8') as writefon:
                print(' : : :+', file=writefon)
            self.phh1.setText(' ')
            self.phh2.setText(' ')
            self.phh3.setText(' ')
            self.phh4.setText('+')
            self.errorbals.setText(' ')
            with open('fon.txt', 'w', encoding='utf-8') as fontxt:
                print(r'fons\fon3.jpeg', file=fontxt, end='')
        else:
            self.errorbals.setText('Недостаточно баллов')


    def pr1(self):
        global savepref
        global countbal
        with open('prefnow.txt', 'w', encoding='utf-8') as writepref:
            print('+: : : ', file=writepref)
        self.pree1.setText('+')
        self.pree2.setText(' ')
        self.pree3.setText(' ')
        self.pree4.setText(' ')
        self.errorbals.setText(' ')
        with open('prefs.txt', 'w', encoding='utf-8') as pretxt:
            print('', file=pretxt, end='')

    def pr2(self):
        global savepref
        global countbal
        if self.savepref == [' ', '+', ' ', ' ']:
            self.errorbals.setText('Данный предмет уже выбран')

        elif countbal >= 10:
            with open('prefnow.txt', 'w', encoding='utf-8') as writepref:
                print(' :+: : ', file=writepref)
            self.pree1.setText(' ')
            self.pree2.setText('+')
            self.pree3.setText(' ')
            self.pree4.setText(' ')
            self.errorbals.setText(' ')
            with open('prefs.txt', 'w', encoding='utf-8') as pretxt:
                print('[pythonist]', file=pretxt)
        else:
            self.errorbals.setText('Недостаточно баллов')


    def pr3(self):
        global savepref
        global countbal
        if self.savepref == [' ', ' ', '+', ' ']:
            self.errorbals.setText('Данный предмет уже выбран')

        elif countbal >= 30:
            with open('prefnow.txt', 'w', encoding='utf-8') as writepref:
                print(' : :+: ', file=writepref)
            self.pree1.setText(' ')
            self.pree2.setText(' ')
            self.pree3.setText('+')
            self.pree4.setText(' ')
            self.errorbals.setText(' ')
            with open('prefs.txt', 'w', encoding='utf-8') as pretxt:
                print('[topchick]', file=pretxt)
        else:
            self.errorbals.setText('Недостаточно баллов')


    def pr4(self):
        global savepref
        global countbal
        if self.savepref == [' ', ' ', ' ', '+']:
            self.errorbals.setText('Данный предмет уже выбран')

        elif countbal >= 50:
            with open('prefnow.txt', 'w', encoding='utf-8') as writepref:
                print(' : : :+', file=writepref)
            self.pree1.setText(' ')
            self.pree2.setText(' ')
            self.pree3.setText(' ')
            self.pree4.setText('+')
            self.errorbals.setText(' ')
            with open('prefs.txt', 'w', encoding='utf-8') as pretxt:
                print('[vvp]', file=pretxt)
        else:
            self.errorbals.setText('Недостаточно баллов')


    def gm(self):
        global ex
        ex = StartGame()
        ex.show()


class StartGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'Templates\entergame.ui', self)
        global countbal
        self.ff1 = open('datarecords.txt', 'r', encoding='utf-8')
        self.rres = self.ff1.read()
        self.balls1 = open('balls.txt', 'r', encoding='utf-8')
        self.colvoballs = self.balls1.read()
        countbal = int(self.colvoballs)
        self.mxballs.display(int(self.colvoballs))
        self.luch.display(int(self.rres))
        if int(self.colvoballs) < 5:
            self.zvan.setText('Новичок')
        elif 5 <= int(self.colvoballs) < 10:
            self.zvan.setText('Ученик')
        elif 10 <= int(self.colvoballs) < 15:
            self.zvan.setText('Студент')
        elif 15 <= int(self.colvoballs) < 25:
            self.zvan.setText('Профи')
        elif 25 <= int(self.colvoballs) < 40:
            self.zvan.setText('Магистр')
        elif 40 <= int(self.colvoballs) < 70:
            self.zvan.setText('Гуру')
        elif 70 <= int(self.colvoballs) < 100:
            self.zvan.setText('Оракул')
        elif 100 <= int(self.colvoballs):
            self.zvan.setText('Гениус')
        self.startpref = open('prefs.txt', 'r', encoding='utf8').readline()
        self.startfon = open('fon.txt', 'r', encoding='utf8').readline()
        with open('about.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                if index == 1:
                    self.nick = row[4]
                    self.onik.setText(self.startpref + self.nick)

        self.ffff = open('filename.txt', 'r', encoding='utf-8')
        self.avatarname1 = str(self.ffff.readline())
        if len(self.avatarname1) == 1:
            self.pixmap1 = QPixmap('defavatar.png')
        else:
            self.pixmap1 = QPixmap(self.avatarname1)
        self.image1 = QLabel(self)
        self.image1.move(330, 70)
        self.image1.resize(140, 130)
        self.image1.setPixmap(self.pixmap1)
        self.image1.setScaledContents(True)
        self.ffff.close()
        self.pixmap222 = QPixmap(self.startfon)
        self.backg.setPixmap(self.pixmap222)
        self.backg.setScaledContents(True)
        # ==============================
        self.btnstart.clicked.connect(self.rung)
        self.toadm.clicked.connect(self.ta)
        self.pers.clicked.connect(self.gopers)
        self.toshop.clicked.connect(self.goshop)

    def goshop(self):
        global ex
        ex = Shop()
        ex.show()

    def ta(self):
        global ex
        ex = AdmEntry()
        ex.show()

    def rung(self):
        with open('data.txt', 'w', encoding="utf8") as fil:
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            result = cur.execute("""SELECT * FROM qqq""").fetchall()
            for i in result:
                self.vv = i[0]
                self.o1 = i[1]
                self.o2 = i[2]
                self.o3 = i[3]
                self.o4 = i[4]
                print(self.vv, file=fil, end=' : ')
                print(self.o1, file=fil, end=' : ')
                print(self.o2, file=fil, end=' : ')
                print(self.o3, file=fil, end=' : ')
                print(self.o4, file=fil)
        f2 = open('data.txt', 'r', encoding='utf-8')
        lin = f2.readlines()
        if len(lin) <= 1:
            self.erform = Error(self)
            self.erform.show()
        else:
            global ex
            ex = Game()
            ex.show()

    def gopers(self):
        global ex
        ex = Pers()
        ex.show()


class Adminka(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'Templates\adminka.ui', self)
        # self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ff2 = open('datarecords.txt', 'r', encoding='utf-8')
        self.rres2 = self.ff2.read()
        self.luchadm.display(int(self.rres2))
        dbase = QSqlDatabase.addDatabase('QSQLITE')
        dbase.setDatabaseName('database.db')
        dbase.open()
        self.model = QSqlTableModel(self, dbase)
        self.model.setTable("qqq")
        self.model.select()
        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()
        self.btndob.clicked.connect(self.adding)
        self.btndel.clicked.connect(self.delallvopr)
        self.togame.clicked.connect(self.go1)
        self.butdelone.clicked.connect(self.delone)

    def go1(self):
        global ex
        ex = StartGame()
        ex.show()

    def adding(self):
        self.vopr = self.vopros.text()
        self.ot1 = self.dob1.text()
        self.ot2 = self.dob2.text()
        self.ot3 = self.dob3.text()
        self.ot4 = self.dob4.text()
        if (self.vopr != '') and (self.ot1 != '') and (self.ot2 != '') and (self.ot3 != '') \
                and (self.ot4 != ''):
            f1 = open('data.txt', 'a', encoding='utf-8')
            print(self.vopr, file=f1, end=' : ')
            print(self.ot1, file=f1, end=' : ')
            print(self.ot2, file=f1, end=' : ')
            print(self.ot3, file=f1, end=' : ')
            print(self.ot4, file=f1)
            f1.close()
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            baz = (self.vopr, self.ot1, self.ot2, self.ot3, self.ot4)
            cur.execute("""INSERT INTO qqq VALUES(?, ?, ?, ?, ?);""", baz)
            con.commit()
            con.close()
            self.dob1.setText('')
            self.dob2.setText('')
            self.dob3.setText('')
            self.dob4.setText('')
            self.vopros.setText('')
            global ex
            ex = Adminka()
            ex.show()
        else:
            self.admerror.setText("Вы не заполнили все данные!!!")

    def delallvopr(self):
        valid = QMessageBox.question(
            self, '', "Действительно удалить все вопросы?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            f1 = open('data.txt', 'w', encoding='utf-8')
            f1.close()
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute('DELETE FROM qqq;', )
            con.commit()
            con.close()
            global ex
            ex = Adminka()
            ex.show()

    def delone(self):
        if self.tableView.selectionModel().hasSelection():
            for index in self.tableView.selectedIndexes() or []:
                self.tableView.model().removeRow(index.row())
                global ex
                ex = Adminka()
                ex.show()


class AdmEntry(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Templates\loginforadmin.ui', self)
        self.passadm.setEchoMode(QLineEdit.Password)
        self.btnenteradm.clicked.connect(self.logining)

    def logining(self):
        self.log = self.logadm.text()
        self.password = self.passadm.text()
        if (self.log == 'admin') and (self.password == 'admin'):
            global ex
            ex = Adminka()
            ex.show()
        else:
            self.errorlabel.setText("Неверный пароль")


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'Templates\entry.ui', self)
        self.btnt2.clicked.connect(self.run1)
        self.btnt1.clicked.connect(self.run2)

    def run1(self):
        global ex
        ex = AdmEntry()
        ex.show()

    def run2(self):
        global ex
        ex = StartGame()
        ex.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
