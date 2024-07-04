import os
import requests
import bs4
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
myhttpheaderURL ='https://myhttpheader.com'

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0'
}

# Send a request to the Amazon product page
try:
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Parse the response content
soup = bs4.BeautifulSoup(response.content, 'lxml')

# Extract the product price and title
try:
    price = soup.find(name='span', class_='aok-offscreen').get_text().strip()
    price_as_float = float(price.replace("$", "").replace(",", ""))
    title = soup.find(name='span', id='productTitle').get_text().strip()
except AttributeError as e:
    print(f"Error parsing HTML: {e}")
    exit()

print(f"Price: {price_as_float}")
print(f"Title: {title}")

BUY_PRICE = 100

from_email = os.getenv('EMAIL')
password = os.getenv('PASSWORD') # this password should be App password
myemail = os.getenv('MY_EMAIL')


print(f"From Email: {from_email}, Password: {password}, My Email: {myemail}")

# Check if the price is below the buy price and send an email alert
if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(from_email, password)
            connection.sendmail(
                from_addr=from_email,
                to_addrs=myemail,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
            )
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
