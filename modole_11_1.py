
import requests
import pandas as pd
from PIL import Image, ImageFilter

#requests
response = requests.get('https://httpbin.org/get')
print(response.status_code)
print(response.json())
print()

#pandas
data = {'Name': ['Слава', 'Катя', 'Ксюша'], 'Age': [47, 38, 24]}
df = pd.DataFrame(data)
print(df)
df.describe()
print()


#Pillow
img = Image.open('img.jpg')
img = img.resize((1600, 1200))
img = img.filter(ImageFilter.BLUR)
img.save('modified_image.jpg')
