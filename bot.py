import threading
import inbox
import handler


def startBots():
    threadInbox = threading.Thread(target=inbox.main)
    threadHandler = threading.Thread(target=handler.main)
    threadInbox.start()
    threadHandler.start()
    print("Вроде заработало")


def main():
    startBots()


if __name__ == '__main__':
    main()