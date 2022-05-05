from PIL import Image
img = Image.open('transmission.png').convert('RGB') # Open file 'transmission.png' and convert to RGR 

img.show()
img.save('flag.png')