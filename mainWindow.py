import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from body import *
from urls import URLs
from form import form
from record import output
from graph import graph
from two_url_form import two_url_form
new_url = 'new_url'
pick_two_urls = "choose two urls"
get_two_compared_urls = "get two used urls"
get_graph = 'get_score'
class Menu(QtWidgets.QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.init_top_menu()
        
        self.app.body = Body(app)

        self.input_new_url_form()

        self.input_two_urls_form()

        self.init_graph()

        self.setCentralWidget(app.body)

    def init_top_menu(self):
        viewBtn = QtWidgets.QPushButton("urls")
        exitAct = QtWidgets.QAction('Exit', self)
        aboutAct = QtWidgets.QAction('About', self)
        
        toolbar = self.addToolBar("Exit")

        toolbar.addWidget(viewBtn)
        toolbar.addAction(exitAct)
        toolbar.addAction(aboutAct)

        menu = QtWidgets.QMenu()
        menu.addAction(new_url)
        menu.addAction(pick_two_urls)
        menu.addAction(get_two_compared_urls)
        menu.addAction(get_graph)

        viewBtn.setMenu(menu)

        exitAct.triggered.connect(self.close)
        aboutAct.triggered.connect(self.introduce_me)
        menu.triggered.connect(lambda action: self.p(action) )

    def input_two_urls_form(self):
        self.app.two_url_form = two_url_form(self.app)

    def input_new_url_form(self):
        self.app.new_url_form = form(self.app)

    def init_graph(self):
        self.app.graph = graph(self.app)

    def introduce_me(self):
        print("event introduce")
        # reply = QMessageBox.question(self, 'Message',
        #     "about me", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        # if reply == QtGui.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

    def p(self, action):
        act = action.text()
        print(act)
        if act == new_url:
            self.app.new_url_form.show()
            pass
        elif act == pick_two_urls:
            self.app.two_url_form.show()
            pass
        elif act == get_two_compared_urls:
            # two_used_url_form
            print(self.app.body.urls.get_all_used_urls())
        elif act == get_graph:
            import pprint      
            pp = pprint.PrettyPrinter(indent=4)
            score = self.app.graph.getScores()
            pp.pprint(score)
        
    def closeEvent(self, event):
        close = QMessageBox()
        self.app.body.urls.save_set()
        self.app.graph.save()
        
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    menu = Menu(app)
    menu.show()
    sys.exit(app.exec_())