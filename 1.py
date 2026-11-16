"""一个用于练习 Git 提交与上传的 Qt 桌面程序。"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.greeting_count = 0
        self.setWindowTitle("Qt · Git 上传练习")
        self.resize(480, 300)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(28, 24, 28, 24)
        layout.setSpacing(16)

        title = QLabel("我的第一个 Qt 界面")
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(title)
        layout.addWidget(QLabel("输入姓名，点击按钮或按回车试一试。"))

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("请输入你的姓名")
        self.name_input.setMaxLength(80)
        self.name_input.setAccessibleName("姓名")
        layout.addWidget(self.name_input)

        actions = QHBoxLayout()
        self.greet_button = QPushButton("打个招呼")
        self.reset_button = QPushButton("重置")
        actions.addWidget(self.greet_button)
        actions.addWidget(self.reset_button)
        layout.addLayout(actions)

        self.message_label = QLabel("欢迎使用 Qt！")
        self.message_label.setTextFormat(Qt.TextFormat.PlainText)
        self.message_label.setWordWrap(True)
        layout.addWidget(self.message_label)
        layout.addStretch()
        self.statusBar().showMessage("已问候 0 次")

        self.greet_button.clicked.connect(self.greet)
        self.name_input.returnPressed.connect(self.greet)
        self.reset_button.clicked.connect(self.reset)

    def greet(self):
        name = self.name_input.text().strip() or "朋友"
        self.greeting_count += 1
        self.message_label.setText(f"你好，{name}！Qt 界面运行正常。")
        self.statusBar().showMessage(f"已问候 {self.greeting_count} 次")

    def reset(self):
        self.greeting_count = 0
        self.name_input.clear()
        self.message_label.setText("欢迎使用 Qt！")
        self.statusBar().showMessage("已问候 0 次")
        self.name_input.setFocus()


def main():
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
