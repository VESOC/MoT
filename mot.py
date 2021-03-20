import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from info import EMAIL_ADDRESS, EMAIL_PASSWORD
from mail import MAIL_FORMAT, STYLES
from scrap_news import get_news_table
from scrap_weather import get_weather_table

msg = MIMEMultipart('html')
msg['Subject'] = f'{date.today().strftime("%m/%d/%Y")}의 메일'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS

weather_table = get_weather_table()
news_table = get_news_table()

mail_html = MAIL_FORMAT.format(
    STYLE=STYLES, WEATHER=weather_table, NEWS=news_table)
msg.attach(MIMEText(mail_html, 'html'))

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
