from bs4 import BeautifulSoup
import requests
import lxml
import smtplib 


#target buy price
BUY_PRICE = 200


email = "your gmail"
password = "your password"

#product page to track
url = "https://www.amazon.com/PetSafe-ScoopFree-Self-Cleaning-Automatic-Disposable/dp/B016PXH9R2/ref=sr_1_7?dchild=1&keywords=automatic+pet+litter&qid=1619718116&sr=8-7"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

#soups
price = soup.find(id="priceblock_ourprice").get_text()
title = soup.find(id="productTitle").get_text().strip()
split_price = float(price.split("$")[1])

#email if price requirement is met
if split_price < BUY_PRICE:
    message = f"{title} is now {split_price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
            )

