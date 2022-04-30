import cv2
import utlis

scale = 3
path = '4.png'
wP = 210*scale
hP= 297*scale

while True:
    img = cv2.imread(path)

    img,finalContours = utlis.getContours(img,minArea=50000,filter=4)
    if len(finalContours) != 0:
        biggest = finalContours[0][2]
        # print(biggest)

        imgWarp = utlis.warpImg (img,biggest,wP,hP)
        imgContours2, conts2 = utlis.getContours(imgWarp,minArea=2000, filter=4,cThr=[50, 50], draw=False)

        if len(finalContours) != 0:
            for obj in conts2:
                cv2.polylines(imgContours2, [obj[2]], True, (0, 255, 0), 2)
                nPoints = utlis.reorder(obj[2])
                nW = round((utlis.findDis(nPoints[0][0] // scale, nPoints[1][0] // scale) / 10), 1)
                nH = round((utlis.findDis(nPoints[0][0] // scale, nPoints[2][0] // scale) / 10), 1)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]),
                                (nPoints[1][0][0], nPoints[1][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]),
                                (nPoints[2][0][0], nPoints[2][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv2.putText(imgContours2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)
                cv2.putText(imgContours2, '{}cm'.format(nH), (x - 70, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 0, 255), 2)

        cv2.imshow('A4', imgContours2)

    img = cv2.resize(img, (0,0), None, 0.5, 0.5)
    cv2.imshow('Original', img)
    cv2.waitKey(1)