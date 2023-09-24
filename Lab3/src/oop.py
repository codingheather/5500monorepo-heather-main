import random
from enum import Enum


class MObject:
    def __init__(self):
        pass


class Image:
    def __init__(self, w, h):
        print("Constructor called")
        self.m_width = w
        self.m_height = h
        self.m_colorChannels = 3  # Assume we support RGB channels only.
        self.m_Pixels = [random.randint(0, 255) for _ in range(w * h * self.m_colorChannels)]

    """
    def __del__(self):
        # https://docs.python.org/3/reference/datamodel.html#object.__del__
    """

    def getWidth(self):
        return self.m_width

    def getHeight(self):
        return self.m_height


    def getPixelColorR(self, x, y):
        return self.m_Pixels[self.m_width * self.m_colorChannels * y + x]

    def getPixels(self):
        return self.m_Pixels

    def setPixelsToRandomValue(self):
        value = random.randint(0, 255)
        # Set the entire list to one color in one function call
        self.m_Pixels = [value] * (self.m_width * self.m_height * self.m_colorChannels)


class Texture():
    def __init__(self, image, material):
        self.m_image = image
        self.m_material = material

    def getImage(self):
        return self.m_image
    
    def getMaterial(self):
        return self.m_material

class Material(Enum):
    METAL = 1
    LEATHER = 2
    FABRICS =  3
    WOOD = 4
    PLASTIC = 5

def main():
    random.seed()

    # Create a first image
    image1 = Image(100, 200)
    # Create a second image
    image2 = Image(image1.getWidth(), image1.getHeight())

    print(f"image1: {image1.getWidth()}, {image1.getHeight()}")
    print(f"image1 red color at (0, 0): {image1.getPixelColorR(0, 0)}")
    print(f"image2: {image2.getWidth()}, {image2.getHeight()}")
    print(f"image2 red color at (0, 0): {image2.getPixelColorR(0, 0)}")

    texture = Texture(image1, Material.FABRICS)
    print(f"texture's image: {texture.getImage().getWidth()}, {texture.getImage().getHeight()}")
    print(f"texture's material: {texture.getMaterial().name}")

if __name__ == "__main__":
    main()
