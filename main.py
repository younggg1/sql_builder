"""
SQL Builder - 主入口
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from ui.main_window import MainWindow
 

def main():
    app = QApplication(sys.argv)
    
    # 全局字体
    app.setFont(QFont("Microsoft YaHei", 10))
    
    # 应用样式
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
