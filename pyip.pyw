import sys
import requests
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtCore import Qt

# Fetch the internal IP address
def get_internal_ip():
    import socket
    return socket.gethostbyname(socket.gethostname())

# Fetch the external IP address
def get_external_ip():
    try:
        response = requests.get("https://api64.ipify.org")
        return response.text
    except:
        return "Unable to fetch external IP"

# Check if VPN is active
def is_vpn_active(internal_ip, external_ip):
    return internal_ip != external_ip

def copy_to_clipboard(text):
    clipboard = QApplication.clipboard()
    clipboard.setText(text)

def main():
    app = QApplication()

    # Set the theme colors
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Highlight, QColor(142, 45, 197))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    # Create the main window
    window = QWidget()
    window.setWindowTitle("PyIP")
    window.resize(325, 100)
    window.setWindowIcon(QIcon("icon.png"))
    
    # Set the window position
    window.move(75, 75)
    
    layout = QVBoxLayout(window)

    internal_ip = get_internal_ip()
    external_ip = get_external_ip()

    # Button stylesheet
    button_stylesheet = """
    QPushButton {
        background-color: #3E3E3E; 
        color: white;
        border: 1px solid #5E5E5E;
        border-radius: 5px;
        padding: 5px;
    }
    QPushButton:hover {
        background-color: #5E5E5E;
        border: 1px solid #3E3E3E;
    }
    """

    # Create internal IP row
    internal_layout = QHBoxLayout()
    internal_ip_label = QLabel(f"Internal IP:   {internal_ip}")
    internal_copy_button = QPushButton("Copy")
    internal_copy_button.setStyleSheet(button_stylesheet)
    internal_copy_button.clicked.connect(lambda: copy_to_clipboard(internal_ip))
    internal_layout.addWidget(internal_ip_label)
    internal_layout.addWidget(internal_copy_button)

    # Create external IP row
    external_layout = QHBoxLayout()
    external_ip_label = QLabel(f"External IP:   {external_ip}")
    external_copy_button = QPushButton("Copy")
    external_copy_button.setStyleSheet(button_stylesheet)
    external_copy_button.clicked.connect(lambda: copy_to_clipboard(external_ip))
    external_layout.addWidget(external_ip_label)
    external_layout.addWidget(external_copy_button)

    # Create VPN check button
    vpn_button = QPushButton()
    if is_vpn_active(internal_ip, external_ip):
        vpn_button.setText("VPN is active")
        vpn_button.setStyleSheet("background-color: green; border-radius: 5px;")
    else:
        vpn_button.setText("VPN is not active")
        vpn_button.setStyleSheet("background-color: red; border-radius: 5px;")

    layout.addLayout(internal_layout)
    layout.addLayout(external_layout)
    layout.addWidget(vpn_button)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
