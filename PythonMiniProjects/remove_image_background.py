from rembg import remove
from PIL import Image
input_path = 'earth.jpg'
output_path='earth1.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)