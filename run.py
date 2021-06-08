import sys

from core.app import App


def main():
    n = len(sys.argv)
    v = int(sys.argv[1]) if n > 1 else 1

    app = App(v)
    app.run()


if __name__ == '__main__':
    main()
