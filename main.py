import sys

from blackJack import Driver, Application


def main():
    app = Application(sys.argv)
    driver = Driver(app)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
