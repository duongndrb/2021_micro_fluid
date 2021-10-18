# 2021_micro_fluid
the folder sum up code of microfluid project

## CÁCH KIỂM TRA CỔNG PORT TRONG RASPBERRY PI
- Link page: https://mechasolution.vn/Blog/bai-10-giao-tiep-arduino-va-raspberry-pi-uart
### Thư viện
Để giao tiếp với Arduino qua Serial, chúng ta cần cài thư viện pyserial cho Python3
- pip install pyserial
- pip3 install pyserial
### Kiểm tra cổng USB
Không giống với Window, khi bạn gắn cổng USB vào thì Window sẽ báo. Ở Raspbian, các bạn vào Terminal gõ
- ls /dev/tty*
Sau đó gắn cổng USB vào và gõ lại 1 lần nữa
- ls /dev/tty*
Khi đó, các bạn sẽ thấy 1 file mới được tạo ra so với ban đầu, đó là đường dẫn đến cổng USB bạn mới gắn vào. Như trong phần mềm sẽ là /dev/ttyUSB0.
Các cổng nối port với Raspberry pi ở project này hiển thị có dạng /dev/ttyUSB.. 

### File Code run: 
home/pi/Downloads/microfluid/test_parallel/ => do_thong_so_3_1.py (chưa có phần camera)
home/pi/Downloads/microfluid/test_parallel/pi_stream_android => final_code.py (đã có phần stream cam)

## CÁCH HOẠT ĐỘNG:
### Kiểm tra kết nối các cổng port trên Pi : 
1, mở terminal
- ls /dev/tty* 

2, Nối dây các công Arduino với PI (phù hợp với code):
- Cổng 1: bên trái phía trên( cạnh cổng Ethernet) : Nối với Arduino 1 ( cổng port /dev/ttyUSB0)
- Cổng 2: bên trái phía dưới ( cạnh cổng Ethernet): Cổng kết nối với màn hình cảm ứng / hoặc kết nối với cổng chia để kết nối( màn hình, chuột, bàn phím)
- Cổng 3: bên phải phía trên: Nối với Arduino 2 ( Arduino cho máy bơm 2) (cổng port /dev/ttyUSB1)
- Cổng 4 : bên phải phía dưới: Nối với Arduino 3 (arduino cho máy bơm 3) (cổng port /dev/ttyUSB2)

3, Sau khi nối dây và kiểm tra cổng Serial trên Pi, mở file code chạy chương trình giao diện và truyền tín hiệu lên (file Code Run để phía trên) 

4, Sửa code phần các port Serial nếu có lỗi với các công Run ( sửa lại số cho đúng với các số hiển thị trên cổng port Serial của Pi /dev/ttyUSB..)

5, RUN code python và màn hình hiển thị

6, Sau khi màn hình hiển thị giao diện, bật Monitor ở các file Arduino nối với động cơ lên. 
- Arduino 1: home/pi/Downloads/microfluid/test_parallel/Arduino1
- Arduino 2: home/pi/Downloads/microfluid/test_parallel/Arduino2
- Arduino 3: home/pi/Downloads/microfluid/test_parallel/Arduino3

7, mở monitor cho từng file Arduino. monitor cho arduino 1 là /dev/ttyUSB0
file arduino 2, chỉnh sửa cổng port nhận sang /dev/ttyUSB1. Tools -> Port : chọn /dev/ttyUSB1 => chạy monitor
tương tự với Arduino 3 => /dev/ttyUSB2 
Lưu ý: lựa chọn Board Arduino cho phù hợp với hệ : ví dụ Mạch Board Arduino Uno R3

8, Quay lại màn hình giao diện, lựa chọn các thông số

9, Sau khi lựa chọn thông số thì nhấn SET để truyền thông số sang Arduino 

10, Mở cổng monitor tương ứng trên Arduino với máy bơm tương ứng để kiểm tra truyền thông số
Lưu ý: mở tất cả monitor của 3 file arduino tương ứng lên để theo dõi 

11,Khi nhấn nút SET trên màn hình giao diện và đã thấy thông số truyền qua được Arduino thì người dùng sẽ nhấn nút RUN để chạy 
Lưu ý: nhấn SET với từng máy bơm rồi mới nhấn RUN từng máy 

