import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class BotaoArrastavel(QPushButton):
    """Botão que pode ser arrastado pela janela"""
    def __init__(self, texto, parent=None):
        super().__init__(texto, parent)
        self.parent_widget = parent
        self.offset = None
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        if self.offset and event.buttons() == Qt.LeftButton:
            # Calcula nova posição
            nova_x = self.x() + event.pos().x() - self.offset.x()
            nova_y = self.y() + event.pos().y() - self.offset.y()
            
            # Mantém o botão dentro da janela
            nova_x = max(0, min(nova_x, self.parent_widget.width() - self.width()))
            nova_y = max(0, min(nova_y, self.parent_widget.height() - self.height()))
            
            self.move(nova_x, nova_y)
        super().mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)


class TesteAssistente(QDialog):
    def __init__(self):
        super().__init__()

        # Configuração da janela de diálogo ajustável
        self.setWindowTitle("Teste Assistente Lu")
        self.setGeometry(500, 200, 300, 300)
        self.setFixedSize(400, 400)  # Trava a janela em tamanho fixo

        # ===== IMAGEM GRANDE (fundo) =====
        self.imagem = QLabel(self)
        pixmap = QPixmap("Lu_do_magalu (1).png")
        self.imagem.setPixmap(pixmap)
        self.imagem.setScaledContents(True)
       

        # ===== BOTÃO SOBRE O BALÃO =====
        self.botao_inicio = QPushButton("Olá, vamos começar?", self)
        self.botao_inicio.setGeometry(257, 165, 140, 28)  

        self.botao_inicio.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid black;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #e6e6e6;
            }
        """)

        self.botao_inicio.clicked.connect(self.abrir_site)
        

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.imagem.setGeometry(0, 0, self.width(), self.height())

    def update_button_position(self):
        # Calcula tamanho do botão proporcional ao tamanho da janela
        btn_w = max(80, int(self.width() * 0.35))
        btn_h = max(25, int(self.height() * 0.05))

        # Posiciona o botão centrado
        x = (self.width() - btn_w) // 2
        y = (self.height() - btn_h) // 2

        self.botao_inicio.setGeometry(x, y, btn_w, btn_h)
        
        # Ajusta tamanho da fonte proporcional ao botão
        font_px = max(8, int(btn_h * 0.45))
        font = QFont()
        font.setPointSize(font_px)
        self.botao_inicio.setFont(font)

    def abrir_site(self):
        subprocess.Popen("start chrome https://gfl.sinclog.com.br/login", shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TesteAssistente()
    janela.show()
    sys.exit(app.exec_())
