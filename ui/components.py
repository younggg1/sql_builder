"""
可复用的 Fluent Design 组件
"""

from PyQt6.QtWidgets import (
    QWidget, QHBoxLayout, QLineEdit, QComboBox, QPushButton, QFrame, QLabel
)
from PyQt6.QtCore import pyqtSignal


class ConditionRow(QFrame):
    """条件输入行 - 移除 AND/OR 选择"""
    
    removed = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setStyleSheet("""
            ConditionRow {
                background-color: #fafafa;
                border-radius: 6px;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(8)
        
        # 字段
        self.field_input = QLineEdit()
        self.field_input.setPlaceholderText("字段")
        self.field_input.setFixedWidth(100)
        layout.addWidget(self.field_input)
        
        # 操作符
        self.op_combo = QComboBox()
        self.op_combo.addItems(["=", "!=", ">", "<", ">=", "<=", "LIKE", "IN", "IS NULL", "IS NOT NULL"])
        self.op_combo.setFixedWidth(100)
        self.op_combo.currentTextChanged.connect(self.on_op_changed)
        layout.addWidget(self.op_combo)
        
        # 值
        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("值")
        self.value_input.setFixedWidth(120)
        layout.addWidget(self.value_input)
        
        # 删除按钮
        remove_btn = QPushButton("✕")
        remove_btn.setObjectName("remove_btn")
        remove_btn.setFixedWidth(28)
        remove_btn.clicked.connect(self.removed.emit)
        layout.addWidget(remove_btn)
    
    def on_op_changed(self, op):
        """操作符变化时隐藏/显示值输入框"""
        if op in ["IS NULL", "IS NOT NULL"]:
            self.value_input.setEnabled(False)
            self.value_input.setVisible(False)
        else:
            self.value_input.setEnabled(True)
            self.value_input.setVisible(True)
    
    def get_condition(self):
        return {
            'field': self.field_input.text().strip(),
            'op': self.op_combo.currentText(),
            'value': self.value_input.text().strip(),
            'logic': 'AND'  # 固定使用 AND
        }


class ColumnRow(QFrame):
    """列定义行"""
    
    removed = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setStyleSheet("""
            ColumnRow {
                background-color: #fafafa;
                border-radius: 6px;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(8)
        
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("列名")
        self.name_input.setFixedWidth(100)
        layout.addWidget(self.name_input)
        
        self.type_combo = QComboBox()
        self.type_combo.addItems(["INT", "VARCHAR", "TEXT", "DATE", "DATETIME", "DECIMAL", "BOOLEAN"])
        self.type_combo.setFixedWidth(90)
        layout.addWidget(self.type_combo)
        
        self.size_input = QLineEdit()
        self.size_input.setPlaceholderText("长度")
        self.size_input.setFixedWidth(60)
        layout.addWidget(self.size_input)
        
        self.constraint_combo = QComboBox()
        self.constraint_combo.addItems(["", "PRIMARY KEY", "NOT NULL", "UNIQUE", "AUTO_INCREMENT"])
        self.constraint_combo.setFixedWidth(110)
        layout.addWidget(self.constraint_combo)
        
        remove_btn = QPushButton("✕")
        remove_btn.setObjectName("remove_btn")
        remove_btn.setFixedWidth(28)
        remove_btn.clicked.connect(self.removed.emit)
        layout.addWidget(remove_btn)
    
    def get_column(self):
        return {
            'name': self.name_input.text().strip(),
            'type': self.type_combo.currentText(),
            'size': self.size_input.text().strip(),
            'constraint': self.constraint_combo.currentText()
        }


class SetRow(QFrame):
    """SET 行 (UPDATE)"""
    
    removed = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setStyleSheet("""
            SetRow {
                background-color: #fafafa;
                border-radius: 6px;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 6, 8, 6)
        layout.setSpacing(8)
        
        self.field_input = QLineEdit()
        self.field_input.setPlaceholderText("字段")
        self.field_input.setFixedWidth(120)
        layout.addWidget(self.field_input)
        
        eq_label = QLabel("=")
        eq_label.setStyleSheet("font-weight: bold; color: #0078d4;")
        layout.addWidget(eq_label)
        
        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("新值")
        layout.addWidget(self.value_input)
        
        remove_btn = QPushButton("✕")
        remove_btn.setObjectName("remove_btn")
        remove_btn.setFixedWidth(28)
        remove_btn.clicked.connect(self.removed.emit)
        layout.addWidget(remove_btn)
    
    def get_set(self):
        return {
            'field': self.field_input.text().strip(),
            'value': self.value_input.text().strip()
        }
