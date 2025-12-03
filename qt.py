

# # # Prints PySide6 version
# # print(PySide6.__version__)

# # # Prints the Qt version used to compile PySide6
# # print(PySide6.QtCore.__version__)

# class main(QtWidgets.QMainWindow):
# # class main(QtWidgets.QWidget):

#     def __init__(self):
#         super().__init__()
#         # self.initUI()  # or write the UI code directly here 
#         self.handel_ui()
#     def handel_button_click(self):
#         pass



#     # def initUI(self):
#     #             # Code to set up the user interface
#     #             pass


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     ex = main()
#     ex.show()
#     # this is method to show the application window
#     sys.exit(app.exec())
#         # this is the infinit loop to run the application








import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMessageBox ,QApplication
import urllib.request
import threading



class main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.handel_ui()
        self.url = self.Video_URL_input.text()


    def handel_button_click(self):
        try:
            # threading.Thread(target=self.download_file).start()
            t = threading.Thread(target=self.download_file)
            t.start()
        except:
            urllib.request.HTTPError("Error: Invalid URL")

    def handel_browes_click(self):
        file_dialog = QtWidgets.QFileDialog(self)
        save_location, _ = file_dialog.getSaveFileName(self, "Save File", "", "All Files (*)")
        if save_location:
            self.Save_location_input.setText(save_location)
    
    def handel_progress(self, block_num, block_size, total_size):
        if total_size > 0:
            downloaded = block_num * block_size
            progress = int(downloaded * 100 / total_size)
            self.Progress_bar.setValue(progress)
            # QApplication.processEvents() # for not responding UI
                                            # concurrently  >> threading 

    def download_file(self):
        fix_url = self.fix_link_url(self.url)
        save_location = self.Save_location_input.text()
        urllib.request.urlretrieve(fix_url, save_location, self.handel_progress)
        
        # try:
        #     urllib.request.urlretrieve(url, save_location, self.handel_progress)
        # except Exception as e:
        #     return QMessageBox.warning(self, "Download Error", f"An error occurred: {e}")

        QMessageBox.information(self, "Download Complete", "The video has been downloaded successfully.")
        self.Progress_bar.setValue(0)
        self.Video_URL_input.clear()
        self.Save_location_input.clear()


# #################### add function to fix google drive links ########################
###### bocause urllib cant download from google drive directy ########################
######################################################################################
    
    def fix_link_url(self, url):
        url = self.Video_URL_input.text()
        if url == "":
            return QMessageBox.warning(self, "Input Error", "Please enter a valid URL.")
        if "drive.google.com" in url:
            file_id = None
            if "/d/" in url:
                file_id = url.split("/d/")[1].split("/")[0]
            elif "id=" in url:
                file_id = url.split("id=")[1]
            if file_id:
                url = f"https://drive.google.com/uc?export=download&id={file_id}"
        return url

##########################    setgometry(x, y, width, height)   ########################################    
    def handel_ui(self):
        self.setWindowTitle("pydownloader")
        self.setWindowIcon(QtGui.QIcon("download.jpg"))
        self.setFixedSize(800, 460)
        

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction("New")
        file_menu.addAction("Open")

        
        help_menu = menubar.addMenu("Help")
        about_menu = menubar.addMenu("About")


        self.Video_URL_input = QtWidgets.QLineEdit(self)
        self.Video_URL_input.setGeometry(200, 50, 500, 30)



        self.Save_location_input = QtWidgets.QLineEdit(self)
        self.Save_location_input.setGeometry(200, 150, 450, 30)
        




        self.Progress_bar = QtWidgets.QProgressBar(self)
        self.Progress_bar.setGeometry(200, 250, 500, 30)
        # self.Progress_bar.setValue(20)  # Initial value of the progress bar



        self.Download = QtWidgets.QPushButton("Download Video", self)
        self.Download.setGeometry(350, 400, 100, 30)
        self.Download.clicked.connect(self.handel_button_click)



        self.Video_URL = QtWidgets.QLabel("Video URL:", self)
        self.Video_URL.setGeometry(50, 50, 100, 30)



        self.Save_location = QtWidgets.QLabel("Save location:", self)
        self.Save_location.setGeometry(50, 150, 100, 30)



        self.Browse = QtWidgets.QPushButton("Browse", self)
        self.Browse.setGeometry(660, 150, 100, 30)
        self.Browse.clicked.connect(self.handel_browes_click)



        # text = QtWidgets.QPlainTextEdit(self)
        # text.setGeometry(50, 200, 700, 150)
        # text.setPlaceholderText("Enter any additional information here...")







        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }

            QMenuBar {
                background-color: #1e1e1e;
                color: #ffffff;
            }

            QMenuBar::item:selected {
                background-color: #ff4757;
            }

            QPushButton {
                background-color: #3d3d3d;
                color: #ffffff;
                border-radius: 10px;
                font-size: 10px;
            }

            QPushButton:hover {
                background-color: #ff4757;
            }

            QPushButton:pressed {
                background-color: #d63031;
            }

            QLabel {
                color: #ffffff;
            }

            QLineEdit, QTextEdit {
                background-color: #3d3d3d;
                color: #ffffff;
            }
            QMessageBox{
                background-color: #2b2b2b;
                color: #ffffff;
            }
        """)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = main()
    ex.show()
    sys.exit(app.exec())
