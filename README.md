# Yüz Tanıma Uygulaması

Bu basit Python uygulaması, [MTCNN](https://github.com/ipazc/mtcnn) (Multi-task Cascaded Convolutional Networks) kullanarak kameradan alınan görüntüdeki yüzleri tespit eder ve bu yüzleri çerçeveleme işlemi gerçekleştirir.

## Kullanılan Kütüphaneler

- [OpenCV](https://github.com/opencv/opencv): Bilgisayar görüşü ve görüntü işleme için kullanılan bir kütüphane.
- [MTCNN](https://github.com/ipazc/mtcnn): Yüz tespiti yapmak için kullanılan çoklu görevli bir derin öğrenme modeli.

## Kurulum

Bu uygulamayı çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Python yükleyin: [Python İndirme Sayfası](https://www.python.org/downloads/)
2. Gerekli kütüphaneleri yükleyin:

    ```bash
    pip install opencv-python
    ```

    ```bash
    pip install mtcnn
    ```

## Kod

* Gerekli kütüphaneleri projeye dahil edelim

    ```python
    import cv2
    from mtcnn.mtcnn import MTCNN
    ```

* Kamerayı başlatma

    ```python
    cap = cv2.VideoCapture(0)
    ```
    
* MTCNN Modelinin yükleme

    ```python
    detector = MTCNN()
    ```

* Kameradan bir kare al

    ```python
    ret, frame = cap.read()
    ```

* Yüzleri tespit et

    ```python
    faces = detector.detect_faces(frame)
    ```

* Tespit edilen yüzleri çerçevele

    ```python
    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    ```

* Görüntüyü ekrana göster

    ```python
    cv2.imshow('Yüz Tanıma', frame)
    ```

* Çıkış için 'q' tuşuna basın

    ```python
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ```

* Kamerayı kapatma

    ```python
    cap.release()
    cv2.destroyAllWindows()
    ```

## Kodun Tamamı

```python
import cv2
from mtcnn.mtcnn import MTCNN

cap = cv2.VideoCapture(0)

detector = MTCNN()

while True:
    # Kameradan bir kare al
    ret, frame = cap.read()

    faces = detector.detect_faces(frame)

    for face in faces:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Yüz Tanıma', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
```

## Kullanım

1. Kameranızı başlatın.
2. Program, kamera görüntüsünden yüzleri tespit edip çerçeveleyecektir.
3. Çıkış için klavyeden 'q' tuşuna basın.


