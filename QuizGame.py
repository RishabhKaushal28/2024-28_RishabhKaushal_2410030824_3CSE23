"""
ENTRY POINT OF THE PROJECT
Run this file to start the application.
This project also requires gui.py, quiz_engine.py, and db_setup.py.
Please keep all project files in the same folder while testing
"""

import os

from db_setup import DB_FILE, initialize_db
from gui import QuizApp


def main():
    if not os.path.exists(DB_FILE):
        initialize_db()
    app = QuizApp()
    app.mainloop()


if __name__ == "__main__":
    main()
