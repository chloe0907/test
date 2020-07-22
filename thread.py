import logging
import logging.config
import threading
from time import sleep

logging.config.fileConfig("log.conf")
logging = logging.getLogger()


def loop0():
    logging.info("start loop0")
    sleep(4)
    logging.info("end loop0")


def loop1():
    logging.info("start loop1")
    sleep(2)
    logging.info("end loop1")


def main():
    logging.info("start all")
    t1 = threading.Thread(target=loop0, args=())
    t2 = threading.Thread(target=loop1, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    logging.info("end all")


if __name__ == "__main__":
    main()
