from PIL import Image
import numpy as np


def predict(imgs, model):
    image = Image.open(imgs)
    imageBW = image.convert('L')

    imageResized = imageBW.resize([22, 30], Image.ANTIALIAS)

    pixelSize = 15

    pixelProgression = np.percentile(imageResized, pixelSize)

    invertedImage = np.clip(imageResized - pixelProgression, 0, 255)

    maxPixelValue = np.max(imageResized)
    arr = np.asarray(invertedImage) // maxPixelValue
    sampleImg = np.array(arr).reshape(1, 660)

    prediction = model.predict(sampleImg)

    image.close()

    return prediction[0]
