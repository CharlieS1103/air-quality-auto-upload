import secrets
import requests
#from PIL import Image, ImageDraw, ImageFont
import instabot
from PIL import Image, ImageDraw, ImageFont

if __name__ == "__main__":
    api_key = secrets.API_KEY
    sensor_index = secrets.SENSOR_INDEX

    # Define the URL and headers
    url = f"https://api.purpleair.com/v1/sensors/{sensor_index}"
    headers = {"X-API-Key": api_key}

    # Make the GET request
    response = requests.get(url, headers=headers)

   
    url = f"http://api.weatherapi.com/v1/forecast.json?key={secrets.WEATHER_API_KEY}&q={secrets.ZIPCODE}&days=1&aqi=yes&alerts=yes"

    weather_response = requests.get(url, headers=headers)

    print(response.json())
    # Extract the data from the response
    data = response.json()
    pm25 = data["sensor"]["stats"]["pm2.5"]
    humidity = data["sensor"]["humidity"]
    temperature = data["sensor"]["temperature"]
    print(f"PM2.5: {pm25}")
    print(f"Humidity: {humidity}")
    print(f"Temperature: {temperature}")

    # Create an image with the data
    img = Image.new("RGB", (800, 800), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/Typewriter.ttf", 36)
    d.text((10, 10), f"PM2.5: {pm25}", font=font, fill=(0, 0, 0))
    d.text((10, 50), f"Humidity: {humidity}", font=font, fill=(0, 0, 0))
    d.text((10, 90), f"Temperature: {temperature}", font=font, fill=(0, 0, 0))

    # Save the image to a file
    img.save("air_quality.png")

    # Post the image to Instagram
    # TODO: Implement Instagram posting code

    def post_to_instagram(image_path):
        # Create an instance of the InstaBot class
        bot = instabot.Bot()

        # Login to Instagram
        bot.login(username=secrets.INSTAUSER, password=secrets.INSTAPASS)

        # Post the image
        bot.upload_photo(image_path, caption="Check out this air quality data!")

        # Logout of Instagram
        bot.logout()
