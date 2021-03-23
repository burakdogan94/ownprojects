import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from sfk_sayarform import Ui_MainWindow
from datetime import datetime
class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_hesapla.clicked.connect(self.calculate)

    def calculate(self):
        start = self.ui.dateEdit_baslangic.date()
        bitis = self.ui.dateEdit_bitis.date()

        izin = self.ui.lineEdit_izin.text()
        rapor = self.ui.lineEdit_rapor.text()
        gec = self.ui.lineEdit_gec.text()
        if int(rapor) > 6: 
            toplam_cikacak_gun = (int(gec)+int(izin)+(int(rapor)-6))
        else:
            toplam_cikacak_gun = (int(gec)+int(izin))
        print(toplam_cikacak_gun)
        print(f'Cıkıs {bitis.addDays(+toplam_cikacak_gun).toString(Qt.ISODate)}')
        
        


        now = datetime.now()
        suan = QDate.currentDate()
        cikis_tarihi = suan.addDays(-toplam_cikacak_gun).daysTo(bitis)
        print(suan.toString(Qt.DefaultLocaleLongDate))
        self.ui.lbl_suan.setText('            Bu günün tarihi: '+str(suan.toString(Qt.DefaultLocaleLongDate)))
        self.ui.lbl_result.setText(f'            Çıkış Tarihi: {bitis.addDays(+toplam_cikacak_gun).toString(Qt.ISODate)} \n            Kalan gün: '+ str(cikis_tarihi))



def app():

    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()