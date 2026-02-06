import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class SumCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PyQt5 Sum Calculator")
        self.setGeometry(100, 100, 350, 200)
        
        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Instructions
        self.label = QLabel("Enter numbers (comma/space separated):")
        layout.addWidget(self.label)
        
        # Input field
        self.entry = QLineEdit()
        self.entry.setPlaceholderText("e.g., 10 20 30 or 1,2,3")
        layout.addWidget(self.entry)
        
        # Sum button
        self.sum_button = QPushButton("Sum")
        self.sum_button.clicked.connect(self.calculate_sum)
        layout.addWidget(self.sum_button)
        
        # Result label
        self.result_label = QLabel("Result will appear here")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)
    
    def calculate_sum(self):
        try:
            input_text = self.entry.text().strip()
            if not input_text:
                self.result_label.setText("Enter numbers first!")
                return
            
            # Split by comma or space
            numbers_str = input_text.replace(',', ' ').split()
            numbers = [float(num) for num in numbers_str]
            total = sum(numbers)
            self.result_label.setText(f"Sum: {total}")
            
        except ValueError:
            QMessageBox.critical(self, "Error", "Enter valid numbers!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SumCalculator()
    window.show()
    sys.exit(app.exec_())
