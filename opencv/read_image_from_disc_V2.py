import cv2

def main():
    imgpath  = 'G:\\Python-Practice\\opencv\\images\\4.2.03.tiff'
    # READ IMAGE FROM DISC
    img = cv2.imread(imgpath)
    #MAKING AN EXPLICIT WINDOW
    '''
        as we are using here explicit window we controll to destroy which 
        window instead of destroying all wondow
    '''
    cv2.namedWindow('imageViewer', cv2.WINDOW_AUTOSIZE)
    #  TO VIEW IMAGE CV2.IMSHOW("NAME OF WINDOW", IMG)
    cv2.imshow('imageViewer', img)
    #TO BIND KEYBOARD EVENT WITH CV2.IMSHOW METHOD
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.destroyWindow('imageViewer')


if __name__ == '__main__':
    main()