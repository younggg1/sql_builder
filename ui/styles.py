"""
Fluent Design 风格样式
"""

STYLESHEET = """
/* 全局 */
* {
    font-family: "Microsoft YaHei", "Segoe UI", sans-serif;
}

QMainWindow {
    background-color: #f3f3f3;
}

/* 输入框 */
QLineEdit {
    padding: 8px 12px;
    border: 1px solid #d1d1d1;
    border-radius: 4px;
    background-color: white;
    color: #323232;
    selection-background-color: #0078d4;
}

QLineEdit:hover {
    border-color: #0078d4;
}

QLineEdit:focus {
    border: 2px solid #0078d4;
    padding: 7px 11px;
}

/* 下拉框 */
QComboBox {
    padding: 8px 12px;
    border: 1px solid #d1d1d1;
    border-radius: 4px;
    background-color: white;
    color: #323232;
    min-width: 120px;
}

QComboBox:hover {
    border-color: #0078d4;
}

QComboBox:focus {
    border: 2px solid #0078d4;
    padding: 7px 11px;
}

QComboBox::drop-down {
    border: none;
    width: 24px;
}

QComboBox QAbstractItemView {
    border: 1px solid #d1d1d1;
    border-radius: 4px;
    background-color: white;
    selection-background-color: #f0f0f0;
    outline: none;
    padding: 4px;
}

QComboBox QAbstractItemView::item {
    height: 32px;
    padding: 4px 8px;
    border-radius: 4px;
}

QComboBox QAbstractItemView::item:hover {
    background-color: #f0f0f0;
}

QComboBox QAbstractItemView::item:selected {
    background-color: #e5f3ff;
    color: #0078d4;
}

/* 按钮 */
QPushButton {
    padding: 8px 20px;
    border: none;
    border-radius: 4px;
    font-weight: 600;
    font-size: 13px;
}

/* 主按钮 */
QPushButton#primary_btn {
    background-color: #0078d4;
    color: white;
}

QPushButton#primary_btn:hover {
    background-color: #106ebe;
}

QPushButton#primary_btn:pressed {
    background-color: #005a9e;
}

/* 成功按钮 */
QPushButton#success_btn {
    background-color: #107c10;
    color: white;
}

QPushButton#success_btn:hover {
    background-color: #0b5a0b;
}

/* 危险按钮 */
QPushButton#danger_btn {
    background-color: #d13438;
    color: white;
}

QPushButton#danger_btn:hover {
    background-color: #a80000;
}

/* 删除小按钮 */
QPushButton#remove_btn {
    background-color: transparent;
    color: #d13438;
    padding: 4px 8px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton#remove_btn:hover {
    background-color: #d13438;
    color: white;
}

/* 文本预览区 */
QTextEdit#sql_preview {
    font-family: "Consolas", "Monaco", monospace;
    font-size: 13px;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
    background-color: #1e1e1e;
    color: #d4d4d4;
    selection-background-color: #264f78;
}

/* 滚动条 */
QScrollArea {
    border: none;
    background-color: transparent;
}

QScrollBar:vertical {
    background-color: #f3f3f3;
    width: 10px;
    border-radius: 5px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background-color: #c8c8c8;
    border-radius: 5px;
    min-height: 20px;
}

QScrollBar::handle:vertical:hover {
    background-color: #a0a0a0;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* 分割器 */
QSplitter::handle {
    background-color: #e0e0e0;
    border-radius: 2px;
}

QSplitter::handle:horizontal {
    width: 4px;
}

QSplitter::handle:hover {
    background-color: #0078d4;
}

/* 状态栏 */
QStatusBar {
    background-color: white;
    border-top: 1px solid #e0e0e0;
    color: #606060;
    font-size: 12px;
}

/* 工具提示 */
QToolTip {
    background-color: #323232;
    color: white;
    border: none;
    padding: 6px 10px;
    border-radius: 4px;
    font-size: 12px;
}
"""
