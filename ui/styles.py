"""
Fluent Design 风格样式
"""

STYLESHEET = """
/* 全局 */
* {
    font-family: "Segoe UI Variable", "Microsoft YaHei UI", "Segoe UI", sans-serif;
    color: #1c1c1c;
}

QMainWindow {
    background-color: #f9f9f9;
}

QWidget {
    background-color: transparent;
}

/* 主容器背景 */
QWidget#central_widget {
    background-color: #f3f3f3;
}

/* 标题栏 */
QWidget#title_bar {
    background-color: #ffffff;
    border-bottom: 1px solid #e0e0e0;
}

QLabel#main_title {
    color: #0078d4;
    font-size: 20px;
    font-weight: 700;
}

/* 分组标题 */
QLabel#group_title {
    font-size: 13px;
    font-weight: 600;
    color: #5c5c5c;
    margin-top: 12px;
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* 输入框 */
QLineEdit {
    padding: 8px 12px;
    border: 1px solid #d1d1d1;
    border-radius: 4px;
    background-color: #ffffff;
    color: #1c1c1c;
    font-size: 13px;
}

QLineEdit:hover {
    background-color: #fcfcfc;
    border-color: #999999;
}

QLineEdit:focus {
    background-color: #ffffff;
    border-bottom: 2px solid #0078d4;
    padding-bottom: 7px;
}

/* 下拉框 */
QComboBox {
    padding: 8px 12px;
    border: 1px solid #d1d1d1;
    border-radius: 4px;
    background-color: #ffffff;
    color: #1c1c1c;
    min-width: 140px;
    font-size: 13px;
}

QComboBox:hover {
    background-color: #fcfcfc;
    border-color: #999999;
}

QComboBox::drop-down {
    border: none;
    width: 32px;
}

QComboBox::down-arrow {
    image: none;
    border: none;
}

QComboBox QAbstractItemView {
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    background-color: #ffffff;
    selection-background-color: #f3f3f3;
    color: #1c1c1c;
    outline: none;
    padding: 4px;
}

/* 按钮 */
QPushButton {
    padding: 8px 20px;
    border-radius: 4px;
    font-weight: 500;
    font-size: 13px;
    background-color: #ffffff;
    border: 1px solid #d1d1d1;
    color: #1c1c1c;
}

QPushButton:hover {
    background-color: #f5f5f5;
    border-color: #c0c0c0;
}

QPushButton:pressed {
    background-color: #eeeeee;
    border-color: #b0b0b0;
}

/* 主按钮 */
QPushButton#primary_btn {
    background-color: #0078d4;
    color: #ffffff;
    border: 1px solid #006abc;
    font-weight: 600;
}

QPushButton#primary_btn:hover {
    background-color: #106ebe;
    border-color: #005a9e;
}

QPushButton#primary_btn:pressed {
    background-color: #005a9e;
}

/* 成功按钮 */
QPushButton#success_btn {
    background-color: #107c10;
    color: #ffffff;
    border: 1px solid #0e700e;
}

QPushButton#success_btn:hover {
    background-color: #0b5a0b;
}

/* 危险按钮 */
QPushButton#danger_btn {
    background-color: #ffffff;
    color: #d13438;
    border: 1px solid #d1d1d1;
}

QPushButton#danger_btn:hover {
    background-color: #fff4f4;
    border-color: #d13438;
}

/* 移除按钮 */
QPushButton#remove_btn {
    background-color: transparent;
    border: none;
    color: #666666;
    font-size: 16px;
    padding: 0;
}

QPushButton#remove_btn:hover {
    color: #d13438;
    background-color: #fff4f4;
    border-radius: 4px;
}

/* 卡片 */
QFrame#card {
    background-color: #ffffff;
    border-radius: 8px;
    border: 1px solid #e0e0e0;
}

/* 预览区 */
QTextEdit#sql_preview {
    font-family: "Cascadia Code", "Consolas", monospace;
    font-size: 14px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
    background-color: #fafafa;
    color: #1c1c1c;
    line-height: 1.5;
}

/* 状态栏 */
QStatusBar {
    background-color: #ffffff;
    border-top: 1px solid #e0e0e0;
    color: #666666;
    font-size: 12px;
}

/* 滚动条 */
QScrollBar:vertical {
    border: none;
    background: #f9f9f9;
    width: 8px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: #d1d1d1;
    min-height: 30px;
    border-radius: 4px;
}

QScrollBar::handle:vertical:hover {
    background: #c1c1c1;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    border: none;
    background: none;
}

/* 分割器 */
QSplitter::handle {
    background-color: transparent;
}

QSplitter::handle:hover {
    background-color: #0078d4;
}
"""


