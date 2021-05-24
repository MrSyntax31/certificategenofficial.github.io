from PIL import Image, ImageDraw, ImageFont 
import pandas as pd 
import os 
df = pd.read_csv('./csv/sample.csv')
font = ImageFont.truetype('SegoePro-Regular.ttf', 26)
for index, j in df.iterrows():
    img=Image.