from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTableWidget, QTableWidgetItem
import speech_recognition as sr
import threading

class ScoreSheetWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Score Sheet Window")

		# Table to hold user scores
		self.table = QTableWidget()
		self.table.setColumnCount(2)  # Two players
		self.table.setRowCount(5)  # Five score types: 20, 19, 18, 17, Bull

		# Set row headers
		score_types = ['20', '19', '18', '17', 'Bull']
		self.table.setVerticalHeaderLabels(score_types)

		# Set column headers for players
		self.table.setHorizontalHeaderLabels(['David', 'Garry'])

		# Layout setup
		layout = QVBoxLayout()
		layout.addWidget(self.table)
		self.setLayout(layout)

    def update_score(self, player_index, score_type):
        """Update the displayed score for a player based on the score type."""
        current_item = self.table.item(score_type, player_index)

        if current_item is None:
            current_item = QTableWidgetItem("1")  # Initialize if empty
            self.table.setItem(score_type, player_index, current_item)
        else:
            new_score = int(current_item.text()) + 1  # Increment score
            current_item.setText(str(new_score))


class ScoreBoardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Score Board Window")

        # Input field for number of users
        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Enter User Names (comma separated)")

        # Button to open the Score Sheet Window
        self.button_open = QPushButton("Open Score Sheet Window", self)
        self.button_open.clicked.connect(self.open_score_sheet_window)

        # Buttons for scoring options
        self.button_20 = QPushButton("Hit 20", self)
        self.button_19 = QPushButton("Hit 19", self)
        self.button_bull = QPushButton("Hit Bull", self)

        # Connect buttons to scoring methods
        self.button_20.clicked.connect(lambda: self.record_score(0))  # Hit 20
        self.button_19.clicked.connect(lambda: self.record_score(1))  # Hit 19
        self.button_bull.clicked.connect(lambda: self.record_score(4))  # Hit Bull

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.user_input)
        layout.addWidget(self.button_open)

        layout.addWidget(self.button_20)
        layout.addWidget(self.button_19)
        layout.addWidget(self.button_bull)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)    

        # Initialize ScoreSheetWindow reference and game state variables
        self.score_sheet_window = None
        self.active_player_index = 0
        self.throws_count = [0] * 2  # Track throws for each player

        # Start listening for voice commands in a separate thread
        threading.Thread(target=self.listen_for_commands, daemon=True).start()

    def open_score_sheet_window(self):
        """Open the ScoreSheetWindow and pass the entered user names."""

    user_names = [name.strip() for name in self.user_input.text().split(',') if name.strip()]

    if not self.score_sheet_window:
        self.score_sheet_window = ScoreSheetWindow()
        self.score_sheet_window.show()

        if len(user_names) >= 2:
            self.score_sheet_window.table.setHorizontalHeaderLabels(user_names[:2])  

    def record_score(self, score_type):
        """Record a score for the active player."""
        
        if not self.score_sheet_window:
            return
        
        print(f"Player {self.active_player_index} scored {score_type}.")
        self.score_sheet_window.update_score(self.active_player_index, score_type)  
        
        # Increment throw count for active player
        self.throws_count[self.active_player_index] += 1
        
        if self.throws_count[self.active_player_index] >= 3:
            print(f"Player {self.active_player_index} has completed their throws.")
            self.throws_count[self.active_player_index] = 0
            self.active_player_index = (self.active_player_index + 1) % len(self.throws_count)  

    def listen_for_commands(self):
        """Listen for voice commands to update scores."""
        
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            while True:
                try:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    command = r.recognize_google(audio).lower()

                    if "hit twenty" in command:
                        print("Voice Command: Hit Twenty")
                        self.record_score(0)  # Assuming index for "Hit 20"
                    elif "hit nineteen" in command:
                        print("Voice Command: Hit Nineteen")
                        self.record_score(1)  # Assuming index for "Hit 19"
                    elif "hit bull" in command:
                        print("Voice Command: Hit Bull")
                        self.record_score(4)  # Assuming index for "Hit Bull"

                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")

    def closeEvent(self, event):
        """Handle close event to ensure proper closure of both windows."""
        
        if self.score_sheet_window:
            self.score_sheet_window.close()  
        event.accept()  


if __name__ == "__main__":
    app = QApplication([])
    main_win = ScoreBoardWindow()
    main_win.show()
    app.exec_()