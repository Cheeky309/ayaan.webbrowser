# ayaan.webbrowser
PyQt5 Web Browser This project is a simple web browser built using PyQt5 and PyQtWebEngine. It features basic functionalities such as URL navigation, forward and backward browsing, and a clean graphical user interface.

Features URL Bar: Enter the URL of the website you want to visit. Navigation Buttons: Buttons to go forward and backward in the browsing history. Go Button: Navigate to the URL entered in the URL bar. Return Key Navigation: Pressing Enter in the URL bar navigates to the entered URL. Real-time URL Update: The URL bar updates with the current page's URL as you navigate. Installation To run this project, you'll need to have Python installed along with the following libraries:

PyQt5 PyQtWebEngine You can install these libraries using pip:

bash Copy code pip install PyQt5 PyQtWebEngine Usage Clone the Repository: Clone this repository to your local machine using the following command:

bash Copy code git clone <repository_url> Navigate to the Project Directory: Change your working directory to the project's directory:

bash Copy code cd <project_directory> Run the Application: Execute the script to start the web browser:

bash Copy code python <script_name>.py Code Overview WebBrowser Class The WebBrowser class inherits from QMainWindow and initializes the GUI components and web browser functionality.

python Copy code class WebBrowser(QMainWindow): def init(self, *args, **kwargs): super(WebBrowser, self).init(*args, **kwargs) ... Layout Setup The layout is set up using QVBoxLayout for the main layout and QHBoxLayout for the horizontal layout containing the URL bar and navigation buttons.

python Copy code self.layout = QVBoxLayout() self.horizontal = QHBoxLayout() URL Bar and Buttons The URL bar is a QLineEdit widget, and the buttons are QPushButton widgets.

python Copy code self.url_bar = QLineEdit() self.go_btn = QPushButton("Go") self.forward_btn = QPushButton(">") self.backward_btn = QPushButton("<") Web Engine View The web engine view is set using QWebEngineView to display web pages.

python Copy code self.browser = QWebEngineView() self.browser.setUrl(QUrl("http://google.com")) Event Connections The buttons and URL bar are connected to their respective functions.

python Copy code self.go_btn.clicked.connect(self.navigate_to_url) self.forward_btn.clicked.connect(self.browser.forward) self.backward_btn.clicked.connect(self.browser.back) self.url_bar.returnPressed.connect(self.navigate_to_url) self.browser.urlChanged.connect(self.update_url) Navigation and URL Update Functions Functions to handle URL navigation and updating the URL bar.

python Copy code def navigate_to_url(self): url = self.url_bar.text() if not url.startswith('http'): url = 'http://' + url self.browser.setUrl(QUrl(url))

def update_url(self, q): self.url_bar.setText(q.toString()) Future Improvements Add Bookmarks: Functionality to save and manage bookmarks. History: Display browsing history. Tabs: Support for multiple tabs.
