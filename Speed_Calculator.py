from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QGridLayout,\
    QWidget, QPushButton, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Metric (km)', 'Imperial (miles)'])

        time_label = QLabel("Time (hours)")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_age)

        self.output_label = QLabel("")
        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        # Get distance and time from the input boxes
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        # Calculate average speed
        speed = distance / time
        # Check what user chose in the combo
        if self.unit_combo.currentText() == "Metric (km)":
            speed = round(speed, 2)
            unit = "km/h"
        if self.unit_combo.currentText() == "Imperial (miles)":
            speed = round(speed * 0.621371, 2)
            unit = "mph"
        # Display the result
        self.output_label.setText(f"Average speed is {speed} {unit}.")


app = QApplication(sys.argv)
age_calculator = SpeedCalculator()
age_calculator.show()
sys.exit(app.exec())
