# Yüz Tanıma Uygulaması

Bu basit Python uygulaması, [MTCNN](https://github.com/ipazc/mtcnn) (Multi-task Cascaded Convolutional Networks) kullanarak kameradan alınan görüntüdeki yüzleri tespit eder ve bu yüzleri çerçeveleme işlemi gerçekleştirir.

## Kullanılan Kütüphaneler

- [OpenCV](https://github.com/opencv/opencv): Bilgisayar görüşü ve görüntü işleme için kullanılan bir kütüphane.
- [MTCNN](https://github.com/ipazc/mtcnn): Yüz tespiti yapmak için kullanılan çoklu görevli bir derin öğrenme modeli.

## Kurulum

Bu uygulamayı çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Python yükleyin: [Python İndirme Sayfası](https://www.python.org/downloads/)
2. Gerekli kütüphaneleri yükleyin:

    ```
    pip install opencv-python
    pip install mtcnn
    ```

## Kullanım

1. Kameranızı başlatın.
2. Program, kamera görüntüsünden yüzleri tespit edip çerçeveleyecektir.
3. Çıkış için klavyeden 'q' tuşuna basın.

## Kod Açıklaması

- `cv2.VideoCapture(0)`: Kamerayı başlatma.
- `MTCNN()`: MTCNN modelini yükleme.
- `cap.read()`: Kameradan bir kare alıp, `ret` ve `frame` değişkenlerine atama.
- `detector.detect_faces(frame)`: MTCNN kullanarak yüzleri tespit etme.
- Tespit edilen yüzleri çerçeveleme ve ekranda gösterme.
- 'q' tuşuna basıldığında programdan çıkma.

## Lisans

Bu uygulama [MIT Lisansı](LICENSE) altında lisanslanmıştır.
