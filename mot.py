from send_mail import send_mail
from logging import basicConfig, INFO, info
from datetime import datetime
from os import getcwd


def main():
    basicConfig(filename=getcwd() + 'MoT.log', encoding='utf-8', level=INFO)
    now = datetime.now()
    info(now.strftime("%d/%m/%Y %H:%M:%S")+' Successfully sent mail.\n\n')
    send_mail()


if __name__ == '__main__':
    main()
