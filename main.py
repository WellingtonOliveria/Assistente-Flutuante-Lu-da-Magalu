import sys
import subprocess
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QHBoxLayout, QTabWidget, QLabel)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap


class Layout(QWidget):
    """Widget contendo apenas o layout da caixa flutuante"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Layout superior para o botão fechar
        top_layout = QHBoxLayout()
        top_layout.addStretch()  # Empurra o botão para a direita
        btn_fechar = QPushButton("X")
        btn_fechar.setFixedSize(30, 30)
        btn_fechar.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        btn_fechar.clicked.connect(self.fechar)
        top_layout.addWidget(btn_fechar)
        
        layout.addLayout(top_layout)
        
        # Carregar imagem da Lu
        imagem_path = r"c:\Users\wton1\OneDrive\Assitente Flutuante Lu\Lu_do_magalu (1).png"
        
        btn_chrome = QPushButton("Abrir Chrome")
        btn_chrome.setIcon(QIcon(imagem_path))
        btn_chrome.setIconSize(QSize(80, 80))
        btn_chrome.setFixedSize(150, 150)
        btn_chrome.clicked.connect(lambda: self.abrir_programa("chrome", "http://gfl.sinclog.com.br/"))

       

        btn_explorer = QPushButton("Explorador")
        btn_explorer.setIcon(QIcon(imagem_path))
        btn_explorer.setIconSize(QSize(80, 80))
        btn_explorer.setFixedSize(150, 150)
        btn_explorer.clicked.connect(lambda: self.abrir_programa("explorer"))

        layout.addWidget(btn_chrome)
        layout.addWidget(btn_explorer)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def fechar(self):
        """Fechar a aplicação"""
        QApplication.quit()
    
    def abrir_programa(self, comando, url="http://gfl.sinclog.com.br/"):
        """Abrir programas externos"""
        if comando == "chrome":
            caminho = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            if url:
                subprocess.Popen([caminho, url])
            else:
                subprocess.Popen(caminho)

        elif comando == "notepad":
            subprocess.Popen("notepad")

        elif comando == "explorer":
            subprocess.Popen("explorer")


class JanelaPrincipal(QWidget):
    """Janela principal com abas"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Assistente Lu - Sistema com Abas")
        self.setGeometry(100, 100, 500, 400)
        
        # Criar widget com abas
        self.abas = QTabWidget()
        
        # Aba 1: Layout da Caixa Flutuante
        layout_assistente = Layout()
        self.abas.addTab(layout_assistente, "Caixa Flutuante")
        
        # Aba 2: Vazia (para adicionar mais conteúdo depois)
        aba_vazia = QWidget()
        label = QLabel("Adicione conteúdo aqui...")
        layout_vazia = QVBoxLayout()
        layout_vazia.addWidget(label)
        aba_vazia.setLayout(layout_vazia)
        self.abas.addTab(aba_vazia, "Outra Aba")
        
        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.abas)
        self.setLayout(layout_principal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec_())