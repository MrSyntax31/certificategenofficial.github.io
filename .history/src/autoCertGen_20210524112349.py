from PIL import Image, ImageDraw, ImageFont 
import pandas as pd 
import os 
df = pd.read_csv('./csv/sample.csv')
font = ImageFont.truetype('SegoePro-Regular.ttf', 26)
for index, j in df.iterrows():
    img=Image.open('CertITDICT.jpg')
    draw=ImageDraw.Draw.(img)
    draw.text(xy=(1279,1008), text='{}'.format(j['name']),fill=(0,0,0),font=font)
    img.save('template/{}.jpg'.format)