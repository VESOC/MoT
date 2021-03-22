from send_mail import send_mail
from logging import basicConfig, INFO, info
from datetime import datetime


def main():
    basicConfig(filename='MoT.log', encoding='utf-8', level=INFO)
    now = datetime.now()
    info(now.strftime("%d/%m/%Y %H:%M:%S"))
    send_mail()
    info('Successfully sent mail.')


if __name__ == '__main__':
    main()
