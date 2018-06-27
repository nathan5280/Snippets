from app.application import Application

print("run.py")


def main():
    print("run.main()", locals())
    flask_app = Application()
    flask_app.run()


if __name__ == '__main__':
    main()