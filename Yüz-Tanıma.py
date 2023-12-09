import cv2
from mtcnn.mtcnn import MTCNN

# Kamera başlatma
cap = cv2.VideoCapture(0)

# MTCNN modelini yükleme
detector = MTCNN()

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Yüzleri tespit et
    faces = detector.detect_faces(frame)

    # Tespit edilen yüzleri çerçevele
    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Görüntüyü ekrana göster
    cv2.imshow('Yüz Tanıma', frame)

    # Çıkış için 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera kapatma
cap.release()
cv2.destroyAllWindows()
