import threading
import loop
import handler


def startBots():
    threadInbox = threading.Thread(target=loop.main)
    threadHandler = threading.Thread(target=handler.main)
    threadInbox.start()
    threadHandler.start()
    print("Вроде заработало")


def main():
    startBots()


if __name__ == '__main__':
    main()