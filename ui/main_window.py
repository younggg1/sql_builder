"""
主窗口 - Fluent Design 风格
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QTextEdit, QLabel, QComboBox, QScrollArea, QSplitter, 
    QLineEdit, QStatusBar, QApplication, QSizePolicy, QGridLayout,
    QFrame
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QIcon

from .styles import STYLESHEET
from .components import ConditionRow, ColumnRow, SetRow
from builder.generator import SQLGenerator

import os
import sys

class MainWindow(QMainWindow):
    """主窗口"""
    
    def __init__(self):
        super().__init__()
        self.generator = SQLGenerator()
        self.current_operation = "SELECT"
        self.init_ui()
    
    def get_resource_path(self, relative_path):
        """获取资源绝对路径，兼容 PyInstaller"""
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        # 开发模式下返回项目根目录的路径
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)
    
    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle("SQL Builder")
        self.setGeometry(150, 150, 1400, 900)
        
        # 设置窗口图标
        try:
            icon_path = self.get_resource_path("logofast_1771237572568.png")
            self.setWindowIcon(QIcon(icon_path))
        except:
            pass
        
        self.setStyleSheet(STYLESHEET)
        
        # 中央组件
        central = QWidget()
        central.setObjectName("central_widget")
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # 标题栏 - 左上角
        title_bar = self.create_title_bar()
        main_layout.addWidget(title_bar)
        
        # 主内容区 - 灰色背景铺满
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(20, 12, 20, 20)
        self.content_layout.setSpacing(16)
        main_layout.addWidget(self.content_widget, 1)
        
        # 分割器
        splitter = QSplitter(Qt.Orientation.Horizontal)
        self.content_layout.addWidget(splitter)
        
        # 左侧面板
        left_panel = self.create_left_panel()
        left_panel.setMinimumWidth(400)
        splitter.addWidget(left_panel)
        
        # 右侧面板
        right_panel = self.create_right_panel()
        right_panel.setMinimumWidth(400)
        splitter.addWidget(right_panel)
        
        # 50:50 比例 - 启动后设置
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)
        splitter.setHandleWidth(4)
        
        # 关键：设置初始比例为 50:50
        QTimer.singleShot(100, lambda: self.set_splitter_sizes(splitter))
        
        # 状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("就绪")
        
        # 初始化 SELECT 界面
        self.build_select_ui()
    
    def set_splitter_sizes(self, splitter):
        """设置分割器初始比例为 50:50"""
        total_width = splitter.width()
        splitter.setSizes([total_width // 2, total_width // 2])
    
    def create_title_bar(self):
        """创建标题栏"""
        widget = QWidget()
        widget.setObjectName("title_bar")
        widget.setFixedHeight(64)
        widget.setStyleSheet("background-color: white; border-bottom: 1px solid #e0e0e0;")
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(24, 0, 24, 0)
        
        # 标题 - 左上角
        title = QLabel("SQL Query Builder")
        title.setObjectName("main_title")
        layout.addWidget(title)
        
        subtitle = QLabel("SQL 语句生成工具")
        subtitle.setStyleSheet("color: #666666; margin-left: 10px; font-size: 14px;")
        layout.addWidget(subtitle)
        
        layout.addStretch()
        
        return widget
    
    def create_left_panel(self):
        """创建左侧面板"""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 8, 0)
        
        # 包装在卡片中
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(16, 16, 16, 16)
        
        # 滚动区
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self.left_content = QWidget()
        self.left_layout = QVBoxLayout(self.left_content)
        self.left_layout.setContentsMargins(0, 0, 10, 0)
        self.left_layout.setSpacing(16)
        
        scroll.setWidget(self.left_content)
        card_layout.addWidget(scroll)
        layout.addWidget(card)
        
        return container
    
    def create_right_panel(self):
        """创建右侧面板"""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(8, 0, 0, 0)
        
        # 包装在卡片中
        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(16, 16, 16, 16)
        card_layout.setSpacing(12)
        
        # 预览标题
        preview_title = QLabel("📄 SQL 预览")
        preview_title.setStyleSheet("font-size: 13px; font-weight: 600; color: #5c5c5c; text-transform: uppercase; letter-spacing: 0.5px;")
        card_layout.addWidget(preview_title)
        
        # SQL 预览
        self.sql_preview = QTextEdit()
        self.sql_preview.setObjectName("sql_preview")
        self.sql_preview.setPlaceholderText("生成的 SQL 将显示在这里...")
        self.sql_preview.setReadOnly(True)
        self.sql_preview.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )
        card_layout.addWidget(self.sql_preview, 1)
        
        # 按钮组
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)
        
        copy_btn = QPushButton("📋 复制 SQL")
        copy_btn.setObjectName("primary_btn")
        copy_btn.setFixedHeight(40)
        copy_btn.clicked.connect(self.copy_sql)
        btn_layout.addWidget(copy_btn)
        
        clear_btn = QPushButton("🗑️ 清空")
        clear_btn.setObjectName("danger_btn")
        clear_btn.setFixedHeight(40)
        clear_btn.clicked.connect(self.clear_all)
        btn_layout.addWidget(clear_btn)
        
        card_layout.addLayout(btn_layout)
        layout.addWidget(card)
        
        return container
    
    def clear_left(self):
        """清空左侧布局"""
        while self.left_layout.count():
            item = self.left_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    def add_group_title(self, text):
        """添加分组标题"""
        label = QLabel(text)
        label.setObjectName("group_title")
        self.left_layout.addWidget(label)
        # 增加一些底部边距
        label.setStyleSheet("margin-top: 4px;")
    
    def create_text_input(self, placeholder, obj_name):
        """创建文本输入框"""
        input_widget = QLineEdit()
        input_widget.setPlaceholderText(placeholder)
        setattr(self, obj_name, input_widget)
        return input_widget
    
    def create_combo_input(self, items, obj_name, fixed_width=None):
        """创建下拉框"""
        combo = QComboBox()
        combo.addItems(items)
        if fixed_width:
            combo.setFixedWidth(fixed_width)
        setattr(self, obj_name, combo)
        return combo
    
    def on_operation_changed(self, text):
        """操作类型变化"""
        op = text.split(" - ")[0]
        self.current_operation = op
        
        # 完全清空再重建
        self.clear_left()
        
        # 添加操作选择器
        self.add_group_title("选择操作类型")
        op_combo = QComboBox()
        op_combo.addItems([
            "SELECT - 查询数据",
            "INSERT INTO - 插入数据",
            "UPDATE - 更新数据",
            "DELETE - 删除数据",
            "CREATE DATABASE - 创建数据库",
            "DROP DATABASE - 删除数据库",
            "CREATE TABLE - 创建表",
            "ALTER TABLE - 修改表",
            "DROP TABLE - 删除表",
            "TRUNCATE TABLE - 清空表",
            "CREATE INDEX - 创建索引",
            "DROP INDEX - 删除索引"
        ])
        op_combo.setCurrentText(text)
        op_combo.currentTextChanged.connect(self.on_operation_changed)
        self.left_layout.addWidget(op_combo)
        
        # 构建对应 UI
        builders = {
            "SELECT": self.build_select_ui,
            "INSERT INTO": self.build_insert_ui,
            "UPDATE": self.build_update_ui,
            "DELETE": self.build_delete_ui,
            "CREATE DATABASE": self.build_create_database_ui,
            "DROP DATABASE": self.build_drop_database_ui,
            "CREATE TABLE": self.build_create_table_ui,
            "ALTER TABLE": self.build_alter_table_ui,
            "DROP TABLE": self.build_drop_table_ui,
            "TRUNCATE TABLE": self.build_truncate_table_ui,
            "CREATE INDEX": self.build_create_index_ui,
            "DROP INDEX": self.build_drop_index_ui,
        }
        
        builder = builders.get(op)
        if builder:
            builder(skip_header=True)
    
    def build_select_ui(self, skip_header=False):
        """SELECT 界面"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("如：users", "select_table"))
        
        self.add_group_title("SELECT 字段")
        self.left_layout.addWidget(self.create_text_input("如：id, username 或 *", "select_fields"))
        
        self.add_group_title("WHERE 条件 (可选)")
        self.conditions_container = QVBoxLayout()
        self.conditions_container.setSpacing(8)
        cond_widget = QWidget()
        cond_widget.setStyleSheet("background-color: #f3f3f3;")
        cond_widget.setLayout(self.conditions_container)
        self.left_layout.addWidget(cond_widget)
        
        add_btn = QPushButton("➕ 添加条件")
        add_btn.setObjectName("success_btn")
        add_btn.setFixedHeight(36)
        add_btn.clicked.connect(self.add_condition)
        self.left_layout.addWidget(add_btn)
        
        self.add_group_title("ORDER BY (可选)")
        order_widget = QWidget()
        order_widget.setStyleSheet("background-color: #f3f3f3;")
        order_layout = QHBoxLayout(order_widget)
        order_layout.setContentsMargins(0, 0, 0, 0)
        order_layout.setSpacing(8)
        order_layout.addWidget(self.create_text_input("排序字段", "order_field"))
        order_layout.addWidget(self.create_combo_input(["ASC", "DESC"], "order_dir", 80))
        self.left_layout.addWidget(order_widget)
        
        self.add_group_title("LIMIT (可选)")
        limit_widget = QWidget()
        limit_widget.setStyleSheet("background-color: #f3f3f3;")
        limit_layout = QHBoxLayout(limit_widget)
        limit_layout.setContentsMargins(0, 0, 0, 0)
        limit_layout.setSpacing(8)
        limit_layout.addWidget(QLabel("LIMIT"))
        limit_layout.addWidget(self.create_text_input("记录数", "limit_input"))
        self.left_layout.addWidget(limit_widget)
        
        self.add_generate_button()
    
    def add_condition(self):
        """添加条件行"""
        row = ConditionRow()
        row.removed.connect(lambda: row.deleteLater())
        self.conditions_container.addWidget(row)
    
    def build_insert_ui(self, skip_header=False):
        """INSERT 界面"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("如：users", "insert_table"))
        
        self.add_group_title("字段列表")
        self.left_layout.addWidget(self.create_text_input("如：username, email, age", "insert_fields"))
        
        self.add_group_title("VALUES 值")
        self.left_layout.addWidget(self.create_text_input("如：'张三', 'zhang@example.com', 25", "insert_values"))
        
        self.add_generate_button()
    
    def build_update_ui(self, skip_header=False):
        """UPDATE 界面"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("如：users", "update_table"))
        
        self.add_group_title("SET 要更新的字段")
        self.sets_container = QVBoxLayout()
        self.sets_container.setSpacing(8)
        sets_widget = QWidget()
        sets_widget.setStyleSheet("background-color: #f3f3f3;")
        sets_widget.setLayout(self.sets_container)
        self.left_layout.addWidget(sets_widget)
        
        self.add_set_row()
        
        add_btn = QPushButton("➕ 添加字段")
        add_btn.setObjectName("success_btn")
        add_btn.setFixedHeight(36)
        add_btn.clicked.connect(self.add_set_row)
        self.left_layout.addWidget(add_btn)
        
        self.add_group_title("WHERE 条件 (必填)")
        self.update_conditions_container = QVBoxLayout()
        self.update_conditions_container.setSpacing(8)
        cond_widget = QWidget()
        cond_widget.setStyleSheet("background-color: #f3f3f3;")
        cond_widget.setLayout(self.update_conditions_container)
        self.left_layout.addWidget(cond_widget)
        
        add_btn = QPushButton("➕ 添加条件")
        add_btn.setObjectName("primary_btn")
        add_btn.setFixedHeight(36)
        add_btn.clicked.connect(self.add_update_condition)
        self.left_layout.addWidget(add_btn)
        
        self.add_generate_button()
    
    def add_set_row(self):
        """添加 SET 行"""
        row = SetRow()
        row.removed.connect(lambda: row.deleteLater())
        self.sets_container.addWidget(row)
    
    def add_update_condition(self):
        """添加 UPDATE 条件"""
        row = ConditionRow()
        row.removed.connect(lambda: row.deleteLater())
        self.update_conditions_container.addWidget(row)
    
    def build_delete_ui(self, skip_header=False):
        """DELETE 界面"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("如：users", "delete_table"))
        
        self.add_group_title("WHERE 条件 (必填)")
        self.delete_conditions_container = QVBoxLayout()
        self.delete_conditions_container.setSpacing(8)
        cond_widget = QWidget()
        cond_widget.setStyleSheet("background-color: #f3f3f3;")
        cond_widget.setLayout(self.delete_conditions_container)
        self.left_layout.addWidget(cond_widget)
        
        add_btn = QPushButton("➕ 添加条件")
        add_btn.setObjectName("danger_btn")
        add_btn.setFixedHeight(36)
        add_btn.clicked.connect(self.add_delete_condition)
        self.left_layout.addWidget(add_btn)
        
        warning = QLabel("⚠️ 不带 WHERE 将删除所有记录！")
        warning.setStyleSheet("color: #d13438; font-weight: 600; padding: 8px; background: #fff0f0; border-radius: 4px;")
        self.left_layout.addWidget(warning)
        
        self.add_generate_button()
    
    def add_delete_condition(self):
        """添加 DELETE 条件"""
        row = ConditionRow()
        row.removed.connect(lambda: row.deleteLater())
        self.delete_conditions_container.addWidget(row)
    
    def build_create_database_ui(self, skip_header=False):
        """CREATE DATABASE"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("数据库名")
        self.left_layout.addWidget(self.create_text_input("如：mydb", "create_db_name"))
        self.add_generate_button()
    
    def build_drop_database_ui(self, skip_header=False):
        """DROP DATABASE"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("数据库名")
        self.left_layout.addWidget(self.create_text_input("要删除的数据库名", "drop_db_name"))
        self.add_generate_button()
    
    def build_create_table_ui(self, skip_header=False):
        """CREATE TABLE"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("如：users", "create_table_name"))
        
        self.add_group_title("列定义")
        self.columns_container = QVBoxLayout()
        self.columns_container.setSpacing(8)
        cols_widget = QWidget()
        cols_widget.setStyleSheet("background-color: #f3f3f3;")
        cols_widget.setLayout(self.columns_container)
        self.left_layout.addWidget(cols_widget)
        
        for _ in range(3):
            self.add_column_row()
        
        add_btn = QPushButton("➕ 添加列")
        add_btn.setObjectName("success_btn")
        add_btn.setFixedHeight(36)
        add_btn.clicked.connect(self.add_column_row)
        self.left_layout.addWidget(add_btn)
        
        self.add_generate_button()
    
    def add_column_row(self):
        """添加列定义行"""
        row = ColumnRow()
        row.removed.connect(lambda: row.deleteLater())
        self.columns_container.addWidget(row)
    
    def build_alter_table_ui(self, skip_header=False):
        """ALTER TABLE"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("表名", "alter_table_name"))
        
        self.add_group_title("操作类型")
        self.alter_action = self.create_combo_input(
            ["ADD COLUMN", "DROP COLUMN", "MODIFY COLUMN", "RENAME COLUMN"],
            "alter_action"
        )
        self.alter_action.currentTextChanged.connect(self.on_alter_action_changed)
        self.left_layout.addWidget(self.alter_action)
        
        self.add_group_title("参数")
        self.alter_params_widget = QWidget()
        self.alter_params_widget.setStyleSheet("background-color: #f3f3f3;")
        self.alter_params_layout = QVBoxLayout(self.alter_params_widget)
        self.alter_params_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.addWidget(self.alter_params_widget)
        
        self.on_alter_action_changed()
        self.add_generate_button()
    
    def on_alter_action_changed(self):
        """ALTER 操作变化"""
        while self.alter_params_layout.count():
            item = self.alter_params_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        action = self.alter_action.currentText()
        
        if action in ["ADD COLUMN", "MODIFY COLUMN"]:
            row = ColumnRow()
            self.alter_params_layout.addWidget(row)
        elif action == "DROP COLUMN":
            self.alter_params_layout.addWidget(self.create_text_input("列名", "alter_drop_column"))
        elif action == "RENAME COLUMN":
            widget = QWidget()
            widget.setStyleSheet("background-color: #f3f3f3;")
            layout = QHBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(8)
            layout.addWidget(self.create_text_input("原列名", "alter_old_name"))
            layout.addWidget(self.create_text_input("新列名", "alter_new_name"))
            self.alter_params_layout.addWidget(widget)
    
    def build_drop_table_ui(self, skip_header=False):
        """DROP TABLE"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("要删除的表名", "drop_table_name"))
        self.add_generate_button()
    
    def build_truncate_table_ui(self, skip_header=False):
        """TRUNCATE TABLE"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("要清空的表名", "truncate_table_name"))
        self.add_generate_button()
    
    def build_create_index_ui(self, skip_header=False):
        """CREATE INDEX"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("索引名")
        self.left_layout.addWidget(self.create_text_input("如：idx_username", "index_name"))
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("表名", "index_table"))
        
        self.add_group_title("索引列")
        self.left_layout.addWidget(self.create_text_input("如：username, email", "index_columns"))
        self.add_generate_button()
    
    def build_drop_index_ui(self, skip_header=False):
        """DROP INDEX"""
        if not skip_header:
            self.add_group_title("选择操作类型")
            op_combo = QComboBox()
            op_combo.addItems([
                "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
                "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
                "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
                "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
            ])
            op_combo.currentTextChanged.connect(self.on_operation_changed)
            self.left_layout.addWidget(op_combo)
        
        self.add_group_title("索引名")
        self.left_layout.addWidget(self.create_text_input("要删除的索引名", "drop_index_name"))
        
        self.add_group_title("表名")
        self.left_layout.addWidget(self.create_text_input("表名", "drop_index_table"))
        self.add_generate_button()
    
    def add_generate_button(self):
        """添加生成按钮"""
        btn = QPushButton("⚡ 生成 SQL")
        btn.setObjectName("primary_btn")
        btn.setFixedHeight(44)
        btn.setFont(QFont("Microsoft YaHei", 13, QFont.Weight.Bold))
        btn.clicked.connect(self.generate_sql)
        self.left_layout.addWidget(btn)
    
    def generate_sql(self):
        """生成 SQL"""
        try:
            op = self.current_operation
            sql = ""
            
            if op == "SELECT":
                sql = self.generator.select(
                    table=getattr(self, 'select_table', None).text().strip() if hasattr(self, 'select_table') else "",
                    fields=getattr(self, 'select_fields', None).text().strip() if hasattr(self, 'select_fields') else "*",
                    conditions=self.get_conditions(self.conditions_container) if hasattr(self, 'conditions_container') else None,
                    order_by=getattr(self, 'order_field', None).text().strip() if hasattr(self, 'order_field') else None,
                    order_dir=getattr(self, 'order_dir', None).currentText() if hasattr(self, 'order_dir') else "ASC",
                    limit=getattr(self, 'limit_input', None).text().strip() if hasattr(self, 'limit_input') else None
                )
            elif op == "INSERT INTO":
                sql = self.generator.insert(
                    table=getattr(self, 'insert_table', None).text().strip() if hasattr(self, 'insert_table') else "",
                    fields=getattr(self, 'insert_fields', None).text().strip() if hasattr(self, 'insert_fields') else "",
                    values=getattr(self, 'insert_values', None).text().strip() if hasattr(self, 'insert_values') else ""
                )
            elif op == "UPDATE":
                sets = []
                if hasattr(self, 'sets_container'):
                    for i in range(self.sets_container.count()):
                        row = self.sets_container.itemAt(i).widget()
                        if row:
                            sets.append(row.get_set())
                
                conditions = self.get_conditions(self.update_conditions_container) if hasattr(self, 'update_conditions_container') else None
                sql = self.generator.update(
                    table=getattr(self, 'update_table', None).text().strip() if hasattr(self, 'update_table') else "",
                    sets=sets,
                    conditions=conditions
                )
            elif op == "DELETE":
                conditions = self.get_conditions(self.delete_conditions_container) if hasattr(self, 'delete_conditions_container') else None
                sql = self.generator.delete(
                    table=getattr(self, 'delete_table', None).text().strip() if hasattr(self, 'delete_table') else "",
                    conditions=conditions
                )
            elif op == "CREATE DATABASE":
                sql = self.generator.create_database(
                    getattr(self, 'create_db_name', None).text().strip() if hasattr(self, 'create_db_name') else ""
                )
            elif op == "DROP DATABASE":
                sql = self.generator.drop_database(
                    getattr(self, 'drop_db_name', None).text().strip() if hasattr(self, 'drop_db_name') else ""
                )
            elif op == "CREATE TABLE":
                columns = []
                if hasattr(self, 'columns_container'):
                    for i in range(self.columns_container.count()):
                        row = self.columns_container.itemAt(i).widget()
                        if row:
                            columns.append(row.get_column())
                sql = self.generator.create_table(
                    name=getattr(self, 'create_table_name', None).text().strip() if hasattr(self, 'create_table_name') else "",
                    columns=columns
                )
            elif op == "ALTER TABLE":
                action = getattr(self, 'alter_action', None).currentText() if hasattr(self, 'alter_action') else ""
                params = {}
                if hasattr(self, 'alter_params_layout'):
                    row = self.alter_params_layout.itemAt(0).widget()
                    if row:
                        if action in ["ADD COLUMN", "MODIFY COLUMN"]:
                            params['col_def'] = f"{row.name_input.text()} {row.type_combo.currentText()}"
                            if row.size_input.text():
                                params['col_def'] += f"({row.size_input.text()})"
                        elif action == "DROP COLUMN":
                            params['column'] = row.text()
                        elif action == "RENAME COLUMN":
                            params['old'] = row.layout().itemAt(0).widget().text()
                            params['new'] = row.layout().itemAt(1).widget().text()
                sql = self.generator.alter_table(
                    table_name=getattr(self, 'alter_table_name', None).text().strip() if hasattr(self, 'alter_table_name') else "",
                    action=action,
                    params=params
                )
            elif op == "DROP TABLE":
                sql = self.generator.drop_table(
                    getattr(self, 'drop_table_name', None).text().strip() if hasattr(self, 'drop_table_name') else ""
                )
            elif op == "TRUNCATE TABLE":
                sql = self.generator.truncate_table(
                    getattr(self, 'truncate_table_name', None).text().strip() if hasattr(self, 'truncate_table_name') else ""
                )
            elif op == "CREATE INDEX":
                sql = self.generator.create_index(
                    name=getattr(self, 'index_name', None).text().strip() if hasattr(self, 'index_name') else "",
                    table=getattr(self, 'index_table', None).text().strip() if hasattr(self, 'index_table') else "",
                    columns=getattr(self, 'index_columns', None).text().strip() if hasattr(self, 'index_columns') else ""
                )
            elif op == "DROP INDEX":
                sql = self.generator.drop_index(
                    name=getattr(self, 'drop_index_name', None).text().strip() if hasattr(self, 'drop_index_name') else "",
                    table=getattr(self, 'drop_index_table', None).text().strip() if hasattr(self, 'drop_index_table') else ""
                )
            
            self.sql_preview.setPlainText(sql)
            self.statusBar.showMessage("SQL 生成成功", 3000)
            
        except Exception as e:
            self.statusBar.showMessage(f"生成失败：{str(e)}", 5000)
    
    def get_conditions(self, container):
        """获取条件列表"""
        conditions = []
        for i in range(container.count()):
            row = container.itemAt(i).widget()
            if row:
                conditions.append(row.get_condition())
        return conditions
    
    def copy_sql(self):
        """复制 SQL"""
        clipboard = QApplication.clipboard()
        clipboard.setText(self.sql_preview.toPlainText())
        self.statusBar.showMessage("✅ SQL 已复制到剪贴板", 3000)
    
    def clear_all(self):
        """清空"""
        self.sql_preview.clear()
        
        # 重置到 SELECT
        self.clear_left()
        self.add_group_title("选择操作类型")
        op_combo = QComboBox()
        op_combo.addItems([
            "SELECT - 查询数据", "INSERT INTO - 插入数据", "UPDATE - 更新数据",
            "DELETE - 删除数据", "CREATE DATABASE - 创建数据库", "DROP DATABASE - 删除数据库",
            "CREATE TABLE - 创建表", "ALTER TABLE - 修改表", "DROP TABLE - 删除表",
            "TRUNCATE TABLE - 清空表", "CREATE INDEX - 创建索引", "DROP INDEX - 删除索引"
        ])
        op_combo.currentTextChanged.connect(self.on_operation_changed)
        self.left_layout.addWidget(op_combo)
        self.current_operation = "SELECT"
        self.build_select_ui(skip_header=True)
        
        self.statusBar.showMessage("已清空", 2000)
