import qrcode


data = 'Don\'t forget to subscribe'
img = qrcode.make(data)

img.save('C:/Users/mehta/Documents/web_scraping/mrqr.png')
