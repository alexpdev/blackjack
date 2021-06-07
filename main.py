import os
import sys
from pathlib import Path

TOP = Path(__file__).resolve().parent
IMG_DIR = TOP / "img"
os.environ["IMG_DIR"] = str(IMG_DIR)

from blackJack import Driver, Application

def main():
    app = Application(sys.argv)
    driver = Driver(app)
    driver.play()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
