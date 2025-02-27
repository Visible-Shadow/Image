######################################
# Image Filter Project Starter Code  #
#                                    #
#           Project STEM             #
#                                    #
#              9/20/19               #
#                                    #
######################################
 
# Before running any code, please run the following in the shell :
# pip install -r requirement.txt
 
f1 = "Grey"
f2 = "Tinted"
f3 = "Brightness"
 
# importing PIL.Image library and os library
from PIL import Image #from PIL import Image
import os
 
# Deletes old created images if they exist
images = ["combinedFilters.jpg","Grey.jpg","Tinted.jpg","Brightness.jpg"]
for i in images:
  if os.path.exists(i):
    os.remove(i)
 
# Adds two blank lines before any output
print("\n\n")
 
# Opens image - upload a Local File into repl.it
img = Image.open('image.jpg')
 
# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )
 
########################
#    Example Filter    #
########################

 
#####################
#    Your Filter    # number 1
#####################
 
#No user input
#Averages out every single color, rgb
def Grey():
  print("Grey")
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = (r + g + b) // 3
    newg = (r + g + b) // 3
    newb = (r + g + b) // 3
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage
 
 
#####################################
#    Your Filters with User Input   # filter 2
#####################################

#Uses user input to change 1 color by a certain amount this gives the illusion that the image is tinted
def Tinted():
  print("Tinted")
  colorf2 = input("Which color do you want to change?(r/g/b) ")
  while colorf2 != "r" and colorf2 != "g" and colorf2 != "b":
    colorf2 = input("Please enter r/g/b for which color you want to change: ")
  changef2 = int(input("How much do you want to change it by?(-255, 255) "))
  # Creates an ImageCore Object from original image
  pixels = img.getdata()
  # Creates empty array to hold new pixel values
  new_pixels = []
  # For every pixel from our original image, it saves
  # a copy of that pixel to our new_pixels array
  for p in pixels:
    new_pixels.append(p)
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = r
    newg = g
    newb = b
    #This is where it adds the certain amount you inputted to the color chosen
    match colorf2:
      case "r":
        newr = r + changef2
        if newr > 255:
          newr = 255
        if newr < 0:
          newr = 0
      case "g":
        newg = g + changef2
        if newg > 255:
          newg = 255
        if newg < 0:
          newg = 0
      case "b":
        newb = b + changef2
        if newb > 255:
          newb = 255
        if newb < 0:
          newb = 0
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the new pixel values to newImage
  newImage.putdata(new_pixels)
  # Sends the newImage back to the main portion of program
  return newImage
#  print("Code for filter2")
#  newImage = img
#  return newImage
 
 
 
 
 
 
 
 
 
 
#####################################
#    Your Filters with User Input   # filter 3
#####################################
 
#Uses user input to increase or decrease each color by a certain amount which changes the brightness
def adjust_brightness():
    print("adjusting brightness    ")   # asks the user for brightness input
    answer = int(input("\nWhat percentage would you like to adjust the brightness? (Options: -100 to 100)\n"))
    # Handle valid inputs
    if answer < 100 and answer > -100:
      percentage = answer
    else:
      print("Invalid input. No changes applied.") # if the user types an invalid number this message is printed
 
    # Create an ImageCore object from the original image
    pixels = img.getdata()
    new_pixels = []
    scale = 1 + (percentage / 100) # scale
   
 
    for p in pixels:
      r = min(max(int(p[0] * scale), 0), 255)  # makes sure the vlaues are in between 0 and 255
      g = min(max(int(p[1] * scale), 0), 255)
      b = min(max(int(p[2] * scale), 0), 255)
      new_pixels.append((r, g, b))
   
    new_image = Image.new("RGB", img.size)
    new_image.putdata(new_pixels)
    return new_image

 

add = "n"
 
apply1 = input("Which filters would you like to put onto this image(g = gray, t = tinted, b = brightness, a = all)")
apply2 = "null"
if apply1 != "a":
  add = input("Would you like to add another filter to this image(y/n)")
if add != "n":
  apply2 = input("Which other filters would you like to put onto this image(g = gray, t = tinted, b = brightness)")
match apply1:
  case "g":
    a = Grey()
    a.save("Combined.jpg")
    img = Image.open('Combined.jpg')
  case "t":
    a = Tinted()
    a.save("Combined.jpg")
    img = Image.open('Combined.jpg')
  case "b":
    a = adjust_brightness()
    a.save("Combined.jpg")
    img = Image.open('Combined.jpg')
  case "a":
    a = Grey()
    a.save("Combined.jpg")
    img = Image.open('Combined.jpg')
    a = Tinted()
    a.save("Combined.jpg")
    img = Image.open('Combined.jpg')
    a = adjust_brightness()
    a.save("Combined.jpg")
  case _:
    print("Next time enter g, t, b, or a")
match apply2:
  case "g":
    a = Grey()
    a.save("Combined.jpg")
  case "t":
    a = Tinted()
    a.save("Combined.jpg")
  case "b":
    a = adjust_brightness()
    a.save("Combined.jpg")


# Creates the four filter images and saves them to our files
"""
img = Image.open('image.jpg')
b = Grey()
b.save("Grey.jpg")
c = Tinted()
c.save("Tinted.jpg")
d = adjust_brightness()
d.save("adjust_brightness.jpg")
"""
# Image filter names for use below
f1 = "Grey"
f2 = "Tinted"
f3 = "adjust_brightness"
 
# Apply multiple filters through prompts with the user
#answer = input("\nWhich filter do you want me to apply?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
#while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
 # answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
 
#while answer == "grey" or answer == f1 or answer == f2 or answer == f3:
 # if answer == "grey":
  # img = grey()
  #elif answer == f1:
  # img = filter1()
  #elif answer == f2:
   # img = filter2()
  #elif answer == f3:
   #img = filter3()
  #else:
   # break
  #print("Filter \"" + answer + "\" applied...")
  #answer = input("\nWhich filter do you want me to apply next?\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
  #while answer != "grey" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
    #answer = input("\nIncorrect filter, please enter:\n grey\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
#print("Image being created...Done")
 
# Create the combined filter image and saves it to our files
#img.save("combinedFilters.jpg")
 