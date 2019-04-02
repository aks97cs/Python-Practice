import cv2

def main():
	imgpath = 'G:\\Python-Practice\\opencv\\images\\4.2.03.tiff'
	img = cv2.imread(imgpath)
	cv2.imshow('imageviewer', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()