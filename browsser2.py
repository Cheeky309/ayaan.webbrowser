from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(WebBrowser, self).__init__(*args, **kwargs)
        self.window = QWidget()
        self.window.setWindowTitle("Ayaan")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()  # Use QLineEdit for URL input
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)
        self.backward_btn = QPushButton("<")
        self.backward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.backward_btn)

        self.browser = QWebEngineView()
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://aniwatch.to"))  
        self.window.setLayout(self.layout)
        self.setCentralWidget(self.window)

        # Connect buttons to functions
        self.go_btn.clicked.connect(self.navigate_to_url)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.backward_btn.clicked.connect(self.browser.back)
        self.url_bar.returnPressed.connect(self.navigate_to_url)  # Allow pressing Enter to navigate

        self.browser.urlChanged.connect(self.update_url)

        self.window.show()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication([])
window = WebBrowser()
window.show()
app.exec()
