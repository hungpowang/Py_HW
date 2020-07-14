import cv2
import numpy as np


''' Read image '''
lena = cv2.imread("./src/lena.jpg", 1)
lena_gray = cv2.imread("./src/lena.jpg", 0)
m1 = cv2.imread("./src/hw3_img.png", 1)
pen_gray = cv2.imread("./src/hw3_img.png", 0)
#apple = cv2.imread("./src/apple.png", -1)

''' 影像二值化
1. cv2.threshold
    回傳門檻值, 結果圖像=cv2.threshold(圖像變數, 門檻值, 最大值, 方法)
        方法：
        • cv2.THRESH_BINARY =>超過門檻值的像素設為最大值，小於的設為0
        • cv2.THRESH_BINARY_INV =>超過門檻值的像素設為0，小於的設為最大值
        • cv2.THRESH_OTSU => 自動計算門檻值來做二值化，可配合其他方法使用
                            (只接受單一通道的色彩空間)

2. cv2.adaptiveThreshold
    結果圖像=cv2.adaptiveThreshold( 圖像變數,
                        最大值, 方法一, 方法二, 區塊大小, 微調值)
    "adaptiveThreshold"會自動計算門檻值，跟「threshold」 函式的
    THRESH_OTSU」方法不同點在於他會將整張圖像分 成數個小區塊分別去計
    算(只接受單一通道的色彩空間)
        方法一：
        • cv2.ADAPTIVE_THRESH_MEAN_C: 計算區塊大小內的平均值再減去微調值
        • cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 計算區塊大小內的高斯加權平均值值再減去 微調值
        方法二：
        • cv2.THRESH_BINARY
        • cv2.THRESH_BINARY_INV

'''
#TH, out = cv2.threshold(pen, 128, 200, cv2.THRESH_BINARY)
# print('Return threshold:', TH)

# TH, out_2 = cv2.threshold(pen, 128, 200, cv2.THRESH_BINARY_INV)
# print('Return threshold:', TH)
# 
# m2 = m1.copy()
# th, m2[:,:,0] = cv2.threshold(m1[:,:,0], 128, 200, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print('Return threshold:', th)
# th, m2[:,:,1] = cv2.threshold(m1[:,:,0], 128, 200, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print('Return threshold:', th)
# th, m2[:,:,2] = cv2.threshold(m1[:,:,0], 128, 200, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print('Return threshold:', th)

# 對明暗差異大的處理比較好
# out = cv2.adaptiveThreshold(pen_gray,
#                             230,
#                             #cv2.ADAPTIVE_THRESH_MEAN_C,
#                             cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                             cv2.THRESH_BINARY,
#                             5,
#                             3
# )


''' 影像邊緣偵測
    透過一大一小的門檻值，來計算圖象中的邊線
    結果圖像=cv2.Canny( 圖像變數, 門檻值1, 門檻值2 )
        先用大的門檻值檢測邊緣，再用小的門檻值將檢測出來的結 果線條連起來
'''
# out = cv2.Canny(lena, 130, 250)


''' 平均值模糊法(統計範圍內的色彩值平均) '''
# out = cv2.blur(
#     lena,
#     (5, 5)  # 範圍大小(tuple)
# )


''' 中值模糊法(將處理範圍內的色彩值做排序，取順序在中間的) '''
# out = cv2.medianBlur(
#     lena,
#     7  # 純數值，必須是單數
# )


''' 影像銳利化
    直方圖均衡化法: 結果圖像=cv2.equalizeHist(圖像變數)
    只接受單一通道色彩空間
'''
#out = cv2.equalizeHist(lena_gray)

# m2 = lena.copy()
# m2[:,:,0] = cv2.equalizeHist(lena[:,:,0])
# m2[:,:,1] = cv2.equalizeHist(lena[:,:,1])
# m2[:,:,2] = cv2.equalizeHist(lena[:,:,2])



'''侵蝕(色彩值低的會侵蝕色彩值高的):
    結果圖像=cv2.erode(圖像變數, 結構陣列)
    結構陣列在圖像上會有方向性
    暗的變大，亮的變小 '''
# m2 = cv2.erode(lena, np.ones((5,5)))

'''膨脹(色彩值高的會侵蝕色彩值低的) 
    結果圖像=cv2.dilate(圖像變數, 結構陣列)
    結構陣列在圖像上會有方向性
    亮變大暗變小'''
# m2 = cv2.dilate(lena, np.ones((5,5)))


'''
結果圖像=cv2.morphologyEx(圖像變數, 方法, 結構陣列)
    • cv2.MORPH_OPEN:先執行侵蝕後執行膨脹
    • cv2.MORPH_CLOSE:先執行膨脹後執行侵蝕
    • cv2.MORPH_GRADIENT:執行膨脹與侵蝕產生的變化差
'''
# m2 = cv2.morphologyEx(lena, cv2.MORPH_OPEN, np.ones((5,5)))


'''
判斷圖像裡的各項素是否在指定色彩範圍內
    結果圖像=cv2.inRange(圖像變數, 顏色下限, 顏色上限)
'''
# m2 = cv2.inRange(lena, 1, 254)


m2 = cv2.inRange(m1, (100, 30, 20), (200, 80, 55))
m2 = cv2.dilate(m2, np.ones((25,25)))
m2 = cv2.erode(m2, np.ones((25,25)))
#m3 = np.full(m1.shape, 255, np.uint8)
a, b = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(m1,a,-1,(0,0,255),3)
#print(a)
#print(b)
x, y, w, h = cv2.boundingRect(a[0])
print((x, y, w, h))
cv2.rectangle(m1, (x,y), (x + w, y + h), (10, 0, 239), 5)

# 一個一個輪廓畫出來
# for i in range(0, len(a)):
#     print(i)
#     cv2.drawContours(m3, a,i,(0,0,255),2)

''' Show image '''
#cv2.imshow("lena original", lena)
# cv2.imshow("lena gray", lena_gray)
cv2.imshow("m1", m1)
#cv2.imshow("m2", m2)
#cv2.imshow("m3", m3)

# cv2.imshow("out", out)

# cv2.imshow("out1", m2[:,:,0])
# cv2.imshow("out2", m2[:,:,1])
# cv2.imshow("out3", m2[:,:,2])

# cv2.imshow("output_2", out_2)
# cv2.imshow("output_3", out_3)


cv2.waitKey(7000)  # 10 sec
cv2.destroyAllWindows()

