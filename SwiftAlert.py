# Requests to grab the page
import requests
# BeautifulSoup to parse the downloaded page
from bs4 import BeautifulSoup
# Time for our sleepy loop
import time
# Pushbullet for our notifications
from pushbullet import Pushbullet


def getButtonText( url ):
    "Get Button Text for Product Availability"
    # Download page
    page = requests.get(url)

    # Quit if the page has been taken down
    if page.status_code == 404:
        print("Page not found! Please check the url parameter.")
        raise SystemExit(0)

    # Parse page
    soup = BeautifulSoup(page.text, "html.parser")

    # Find the add to cart button
    cart = soup.find('button', class_='ProductForm__AddToCart')

    # Return the button element text
    return cart.text.strip()

# Product page
url = "https://store.taylorswift.com/products/the-limited-edition-signed-in-the-trees-edition-deluxe-cd-international-customers-only"

# Pushbullet API Key
pbKey = 'welovetaylorswift'

# Time between checking the page
waitTime = 60

# Keep trying while product is not available
while (getButtonText(url) == "Not Available"):
    print("Not available")
    time.sleep(waitTime)

# Double check we can add to cart
if(getButtonText(url) == "Add to cart"):
    print("~~~ PRODUCT AVAILABLE - SENDING NOTIFICATION! ~~~")
    # Pushbullet notification to BUY!
    pb = Pushbullet(pbKey)
    pb.push_note("TAYTAY", url)