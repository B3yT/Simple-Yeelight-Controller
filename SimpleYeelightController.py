from PySide2 import QtWidgets
from yeelight import Bulb
from yeelight import *
import pickle




class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('YeeControl')
        self.setup_ui()
        try:    
                file =open ("lip.bin","rb")
                self.imp_pass.setText(pickle.load(file))
                file.close()
                        
        except OSError:
                print ("error")
        else:
                print ("Successfully loaded")
        
    def setup_ui(self):
        self.create_Widgets()
        self.setup_css()
        self.setup_connections()
        self.create_layouts()
        self.add_widgets_layouts()
        self.imp_pass.text()
        self.imp_pass.setPlaceholderText("yeelight ip adress")
        
    def create_Widgets(self):    
        self.btn_enc =QtWidgets.QPushButton("save")
        self.btn_load =QtWidgets.QPushButton("load")
        self.imp_pass =QtWidgets.QLineEdit()
        self.int_btn = QtWidgets.QPushButton("toogle")
        self.min_btn = QtWidgets.QPushButton("Minimum")
        self.moy_btn = QtWidgets.QPushButton("Middle")
        self.max_btn = QtWidgets.QPushButton("Maximum")
        
        self.blue_btn = QtWidgets.QPushButton("Blue")
        self.green_btn = QtWidgets.QPushButton("green")
        self.red_btn = QtWidgets.QPushButton("red")
        self.pink_btn = QtWidgets.QPushButton("pink")
        self.white_btn = QtWidgets.QPushButton("white")
        self.yellow_btn = QtWidgets.QPushButton("yellow")
       
    
    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)    
        
        
    def  add_widgets_layouts(self):    
        
        self.main_layout.addWidget(self.btn_enc)
        self.main_layout.addWidget(self.btn_load)
        self.main_layout.addWidget(self.imp_pass)
        self.main_layout.addWidget(self.int_btn)
        self.main_layout.addWidget(self.min_btn)
        self.main_layout.addWidget(self.moy_btn)
        self.main_layout.addWidget(self.max_btn)
        
        self.main_layout.addWidget(self.blue_btn)
        self.main_layout.addWidget(self.green_btn)
        self.main_layout.addWidget(self.red_btn)
        self.main_layout.addWidget(self.yellow_btn)
        self.main_layout.addWidget(self.white_btn)
        self.main_layout.addWidget(self.pink_btn)
    
    def setup_css(self):
        self.setStyleSheet( """
        
        background-color: rgb(54,54,54);                   
        color: rgb(240,240,240);
                          
                        """)
    
    def setup_connections(self):
       self.btn_enc.clicked.connect(self.bouton_enc_clic)
       self.btn_load.clicked.connect(self.bouton_load_clic)
       self.int_btn.clicked.connect(self.interupteur_btn)
       self.min_btn.clicked.connect(self.minimum_btn)
       self.moy_btn.clicked.connect(self.moyen_btn)
       self.max_btn.clicked.connect(self.maximum_btn)
       
       self.blue_btn.clicked.connect(self.bleu_btn)
       self.green_btn.clicked.connect(self.vert_btn)
       self.red_btn.clicked.connect(self.rouge_btn)
       self.pink_btn.clicked.connect(self.rose_btn)
       self.yellow_btn.clicked.connect(self.jaune_btn)
       self.white_btn.clicked.connect(self.blanc_btn)

    def bouton_enc_clic(self):
        try:
            file=open ("lip.bin","wb")
            pickle.dump(self.imp_pass.text(),file)
            file.close()
        except OSError:
                print ("error!")
        else:
                print ("Successfully saved") 
    
    def bouton_load_clic(self):
        try:    
            file =open ("lip.bin","rb")
            
            self.imp_pass.setText(pickle.load(file))
            file.close()
              
        except OSError:
                        print ("error")
        else:
                        print ("Successfully loaded")
        
    def interupteur_btn(self):
        
        bulb = Bulb(self.imp_pass.text())
        bulb.toggle()
        
    def maximum_btn(self):
        bulb = Bulb(self.imp_pass.text())
        bulb.set_brightness(100)
    def moyen_btn(self):
        bulb = Bulb(self.imp_pass.text())
        bulb.set_brightness(50)
    def minimum_btn(self):
        bulb = Bulb(self.imp_pass.text())
        bulb.set_brightness(1)
        
    def bleu_btn(self):
        bulb = Bulb(self.imp_pass.text())
        bulb.set_rgb(0, 0, 255)
    def rouge_btn(self):
        bulb = Bulb(self.imp_pass.text())
        bulb.set_rgb(255, 0, 0)
    def vert_btn(self):
        bulb = Bulb(self.imp_pass.text())
        bulb.set_rgb(0, 255, 0)
    def rose_btn(self):
        bulb = Bulb(self.imp_pass.text())
        bulb.set_rgb(255, 0, 255)
    def jaune_btn(self):
        bulb = Bulb(self.imp_pass.text())
        bulb.set_color_temp(2700)
    def blanc_btn(self):
        bulb = Bulb(self.imp_pass.text())
        bulb.set_color_temp(6700)

    



app = QtWidgets.QApplication([])
win = App()
win.show()
win.resize(230,380)
app.exec_()        