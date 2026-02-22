import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class Assistente(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.setWindowTitle("Assistente")
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setFixedSize(180, 200)

        # Variáveis para arrastar
        self.dragging = False
        self.offset = None

        # Layout
        layout = QVBoxLayout()

        # Layout superior para o botão fechar
        top_layout = QVBoxLayout()
        top_layout.addStretch()  # Empurra o botão para a direita
        btn_fechar = QPushButton("X")
        btn_fechar.setFixedSize(30, 30)
        btn_fechar.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        btn_fechar.clicked.connect(self.close)
        top_layout.addWidget(btn_fechar)

        layout.addLayout(top_layout)

        btn_chrome = QPushButton("Abrir Chrome")
        btn_chrome.clicked.connect(lambda: self.abrir_programa("chrome"))

        btn_bloco = QPushButton("Bloco de Notas")
        btn_bloco.clicked.connect(lambda: self.abrir_programa("notepad"))


        btn_explorer = QPushButton("Explorador")
        btn_explorer.clicked.connect(lambda: self.abrir_programa("explorer"))

        layout.addWidget(btn_chrome)
        layout.addWidget(btn_bloco)
        layout.addWidget(btn_explorer)
        layout.addWidget(btn_bloco)
        layout.addWidget(btn_explorer)
        

        self.setLayout(layout)

        # Posição inicial
        self.move(1700, 200)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(self.mapToGlobal(event.pos() - self.offset))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def abrir_programa(self, comando):

        if comando == "chrome":
            caminho = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen(caminho)


        elif comando == "notepad":
            subprocess.Popen("notepad")

        elif comando == "explorer":
            subprocess.Popen("explorer")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Assistente()
    janela.show()
    sys.exit(app.exec_())