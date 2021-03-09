import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from info import *
from mail import *
from scrap_news import get_news
from scrap_weather import get_weather

msg = MIMEMultipart('alternative')
msg['Subject'] = f'{date.today().strftime("%m/%d/%Y")}의 메일'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

weather_info = get_weather()
news_info = get_news()
info = weather_info + news_info

mail_html = MAIL_FORMAT.format(style=STYLES, *info)
msg.attach(MIMEText(''.join(info), 'plain'))
msg.attach(MIMEText(mail_html, 'html'))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
