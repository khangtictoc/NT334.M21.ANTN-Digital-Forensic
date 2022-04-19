# File History (Supported in Window 8+)

## Môi trường demo và chuẩn bị:

**OS**: Window 11 Home Single Language - Version 21H2 (OS Build 22000.613)

**Hard Drive**: Ổ cứng drive HDD (1TB) (có thể sử dụng bất kỳ **thiết bị lưu trữ ngoại vi** nào SSD, USB drive, hoặc có thể là một Drive trên một network )

## Thao tác sử dụng: 

Kết nối ổ cứng ngoài vào máy. Đảm bảo File System trên Window đọc và nhận diện được ổ đĩa.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/164041273-f0316228-f943-4d50-b5d3-0cafc6cc12ca.png" > </p>

Ở đây ổ cứng của mình có 3 drive đang trống là **OS(F:), DATA(G:), MEDIA(H:)**

Vào _Search -> File History_

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/164043460-11bcfad9-ecc5-4cfe-8b55-6c61d93fd18e.png" > </p>

Chọn drive để lưu là _DATA(G:) -> OK_

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/164044092-da202630-1920-48ee-a867-c382297385ae.png" > </p>

File History sẽ giúp chúng ta sao lưu file và version trong một số folder tại đường dẫn `%HOMEPATH%`, lưu các file trong các folder chính như **Desktop, Downloads, ...**. Trong mục "Advanced settings" chúng ta có thể tùy chỉnh dược _thời gian lưu file tại 1 version_ và _khoảng thời gian (interval) để lưu 1 một version mới của file_. Mình set khoảng thời gian này là **10 minutes** để tí nữa thấy rõ các version của file

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/164046387-2d6f2cb1-fde8-48aa-bfa7-a0dd53b4a827.png" > </p>

Vào mục "Restore personal files" để xem thông tin file được sao lưu:

![image](https://user-images.githubusercontent.com/48288606/164047838-7ab67ab9-aa43-494f-b0a6-d3a6a87d2a6e.png)

Giờ ta thử tạo một file ở bên ngoài "Desktop" đặt tên file là `new_verion.txt` với nội dung là `hello world`. Sau tầm 10 phút, click "Run now" để saved lại.

![image](
<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/164051639-855b008a-e853-46bf-b132-fb6a9e6eb266.png" > </p>

Vào lại "Restore personal files" ta thấy có 2 versions. Version 1 của "Desktop":

![image](https://user-images.githubusercontent.com/48288606/164052412-13e0fc38-38a4-406c-af74-37a20573cae8.png)

Version 2 chứa file `new_version.txt` với nội dung là `hello world`

![image](https://user-images.githubusercontent.com/48288606/164052698-fde1b9ab-b786-4de1-af44-f8fe5002e93f.png)

Chúng ta có thể chọn từng version, chọn folders/files cụ thể muốn sao lưu. Click vào nút xanh bên dưới để save vào ổ đĩa 

> NOTE: Phiên bản mới nhất của folders và files sẽ tự động được lưu vào đĩa. Với thao tác trên sẽ cho ta tùy biến lưu những files/folders với version cũ hơn.

<p align="center"> <img src="https://user-images.githubusercontent.com/48288606/164053775-b1ddcde6-93dd-4fe6-8de3-4618f9913fda.png" > </p>

