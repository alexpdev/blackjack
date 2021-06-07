import os
import sys
from pathlib import Path

from blackJack import Driver, Application

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ["IMG_DIR"] = os.path.join(sys.path[0], "img")

def main():
    app = Application(sys.argv)
    Driver(app)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
