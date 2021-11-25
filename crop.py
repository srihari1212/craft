from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'


def detect_text(im,left,top,right,bottom):
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    #im1.save("cropped.jpg")
    data = pytesseract.image_to_string(im1,lang='eng', config='--psm 6')
    # Shows the image in image viewer
    #im1.show()
    res = {
        "data" : data.replace("\n\x0c",""),
        "left" : left,
        "top" : top,
        "right" : right,
        "bottom" : bottom
    }
    return res

def get_result(boxes):

    result = []
    for each in boxes:
        left = each[0][0]
        top = each[0][1]
        right = each[1][0]
        bottom = each[2][1]


        # Opens a image in RGB mode
        img = Image.open("sample/pan_sample.jpg")

        res = detect_text(img,left,top,right,bottom)
        result.append(res)
        
    print(result)
    return result