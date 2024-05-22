import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QHeaderView

class HorarioIU:
    def __init__(self, data, chromosome)-> None:
        ## configuracion de ventana
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle('Horario')
        self.window.setMinimumSize(720, 500)
        self.window.resize(1080, 720)
        layoutMain = QVBoxLayout()
        self.window.setLayout( layoutMain )
        
        ## creacion de elementos 
        layoutTop = QVBoxLayout()
        layoutTopFirstLine = QHBoxLayout()
        layoutTopSecondLine = QHBoxLayout()

        timetable = QTableWidget()

        ## posicion de elementos
        layoutMain.addLayout( layoutTop )
        layoutMain.addWidget( timetable )
        layoutTop.addLayout( layoutTopFirstLine )
        layoutTop.addLayout( layoutTopSecondLine )


        ## configuracion de elementos
        timetable.setRowCount(10)
        timetable.setColumnCount(6)
        timetable.setHorizontalHeaderLabels([
            'Lunes', 
            'Martes', 
            'Miercoles', 
            'Jueves', 
            'Viernes', 
            'Sabado'
        ])
        timetable.setVerticalHeaderLabels([
            '6:45 - 8:15', 
            '8:15 - 9:45', 
            '9:45 - 11:15', 
            '11:15 - 12:45', 
            '12:45 - 14:15',
            '14:15 - 15:45',
            '15:45 - 17:15',
            '17:15 - 18:45',
            '18:45 - 20:15',
            '20:15 - 21:45'
        ])
        
        header = timetable.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        
        headerVertical = timetable.verticalHeader()
        headerVertical.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        headerVertical.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        headerVertical.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        headerVertical.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        headerVertical.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        headerVertical.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        headerVertical.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        headerVertical.setSectionResizeMode(7, QHeaderView.ResizeToContents)
        headerVertical.setSectionResizeMode(8, QHeaderView.ResizeToContents)
        headerVertical.setSectionResizeMode(9, QHeaderView.ResizeToContents)
        
        
        
        ## leyendo data
        visited = {}
        genes = chromosome[1]
            
        for gen in genes:
            if gen[0] > -1:
                subject = data[gen[0]]
                group = subject['groups'][gen[1]]
                shifts = group.shifts
                
                for shift in shifts:
                    row = shift.day.value
                    column = shift.time_start.value
                    key = str(row) + str(column)
                    
                    if key in visited:
                        cellText = visited[key]
                        cellText.insertPlainText('\n--------------')
                        
                    else:
                        cellText = QPlainTextEdit()
                        cellText.setReadOnly(True)
                        cellText.setFixedWidth(200)
                        cellText.setMaximumHeight(108)
                        
                        visited[key] = cellText
                        
                    code = str(subject['code'])
                    name = subject['name']
                    teacher = group.teacher
                    subject_group = group.group
                    
                    cellText.insertPlainText( '\n' + code )
                    cellText.insertPlainText( '\n' + name + " - Grupo: " + subject_group )
                    cellText.insertPlainText( '\n' + teacher )
                    
                    timetable.setCellWidget(shift.time_start.value, shift.day.value, cellText)
        

    def show(self):
        self.window.show()
        sys.exit( self.app.exec_() )
