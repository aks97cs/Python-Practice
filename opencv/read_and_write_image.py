import cv2

def main():
    imgpath = 'G:\\Python-Practice\\opencv\\images\\4.2.03.tiff'
    imguploadpath  = 'G:\\Python-Practice\\opencv\\savedImages\\4.2.03.jpg'
    '''
        Various mode of reading image
        1 : default mode => load image by all color of the image
        0 : in gray scale mode
        -1 : load same image and also save the alfa transparacy channel in the image

    '''
    img = cv2.imread(imgpath)
    cv2.namedWindow('imageViewer', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('imageViewer', img)
    # TO SAVE IMAGE TO A FILE
    cv2.imwrite(imguploadpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('imageViewer')
    pass
if __name__ == '__main__':
    main()