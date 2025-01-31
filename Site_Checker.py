#!/usr/bin/python3
# coding: utf-8

import sys
import requests
import hashlib
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer
cycle_of_min = 6　#巡回時間
terget_url = ""　#ここに監視対象サイトのURLを入れてくださいね☆

class WebsiteMonitor(QWidget):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.last_hash = self.calculate_hash(self.get_website_content())
        
        self.initUI()
        self.start_monitoring()

    def initUI(self):
        self.setWindowTitle('サイトモニタ')
        layout = QVBoxLayout()
        
        self.label = QLabel('当該サイトを監視中...')
        self.label.setStyleSheet("font-size: 18pt;")  # ここでフォントサイズを設定
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        self.show()

    def get_website_content(self):
        response = requests.get(self.url)
        return response.text

    def calculate_hash(self, content):
        return hashlib.md5(content.encode()).hexdigest()

    def check_for_updates(self):
        current_content = self.get_website_content()
        current_hash = self.calculate_hash(current_content)
        
        if current_hash != self.last_hash:
            self.last_hash = current_hash
            QMessageBox.information(self, "更新あり", "当該サイトに更新がありました。")

    def start_monitoring(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_for_updates)
        self.timer.start(cycle_of_min * 60 * 60 * 1000)  # 時間ごとにチェック

if __name__ == '__main__':
    app = QApplication(sys.argv)
    monitor = WebsiteMonitor(terget_url)
    sys.exit(app.exec_())
