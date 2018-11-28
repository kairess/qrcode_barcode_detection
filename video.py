import pyzbar.pyzbar as pyzbar
import cv2

cap = cv2.VideoCapture(0)

i = 0
while(cap.isOpened()):
  ret, img = cap.read()

  if not ret:
    continue

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     
  decoded = pyzbar.decode(gray)

  for d in decoded: 
    x, y, w, h = d.rect

    barcode_data = d.data.decode("utf-8")
    barcode_type = d.type

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    text = '%s (%s)' % (barcode_data, barcode_type)
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

  cv2.imshow('img', img)

  key = cv2.waitKey(1)
  if key == ord('q'):
    break
  elif key == ord('s'):
    i += 1
    cv2.imwrite('c_%03d.jpg' % i, img)

cap.release()
cv2.destroyAllWindows()
