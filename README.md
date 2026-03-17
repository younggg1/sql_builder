# SQL Query Builder

一个基于 Python 和 PyQt6 开发的高颜值、现代化 SQL 语句可视化生成工具。采用 Fluent Design (流体设计) 风格，旨在帮助开发者快速构建常用的 SQL 语句，减少语法记忆负担。

![预览图标](预览图.png)

## ✨ 特性

- **现代化 UI**：仿 Windows 11 Fluent Design 设计方案，支持阴影、圆角卡片、平滑动效。
- **全方位支持**：
  - **DML 支持**：SELECT (带条件/排序/限制)、INSERT INTO、UPDATE、DELETE。
  - **DDL 支持**：CREATE/DROP DATABASE、CREATE/DROP TABLE、ALTER TABLE (增/删/改/更名列)、TRUNCATE。
  - **索引操作**：CREATE/DROP INDEX。
- **可视化配置**：通过表单、列表和下拉框配置参数，实时生成标准 SQL 语法。
- **代码预览与复制**：生成的 SQL 语句在右侧卡片实时预览，支持一键复制代码。
- **高性能单文件**：支持打包为独立的 EXE 执行文件，无需配置环境即可运行。

## 🚀 快速开始

### 开发模式

如果你已经安装了 Python (建议 3.8+)，可以按照以下步骤运行：

1. 克隆或下载本项目到本地。
2. 安装依赖：
   ```bash
   pip install PyQt6 Pillow
   ```
3. 启动程序：
   ```bash
   python main.py
   ```

### 打包模式

本项目配置了 PyInstaller 脚本，可以方便地生成单 EXE 文件：

```bash
pyinstaller --clean -F -w -i "logofast_1771237572568.ico" --add-data "logofast_1771237572568.png;." -n SQLBuilder main.py
```

打包完成后，在 `dist` 目录下即可找到 `SQLBuilder.exe`。

## 📂 项目结构

```text
sql_builder/
├── builder/             # SQL 生成核心逻辑
│   └── generator.py     # SQL 生成算法实现
├── ui/                  # 界面视图组件
│   ├── components.py    # 可复用的 UI 行、表单组件
│   ├── main_window.py   # 主窗口布局与逻辑
│   └── styles.py        # 全局 QSS 样式表 (Fluent Design)
├── main.py              # 程序主入口
└── logofast_xxxx.png/ico # 资源文件
```

## 🛠️ 技术栈

- **核心语言**: Python 3
- **GUI 框架**: PyQt6
- **图像处理**: Pillow (用于打包时的图标转换)
- **打包工具**: PyInstaller

## 📝 许可证

本项目遵循 [GPLv3](LICENSE) 开源协议。
