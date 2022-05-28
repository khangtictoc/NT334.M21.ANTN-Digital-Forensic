# Demo (Anti Forensic)

## File History

Link youtube: [File History](https://www.youtube.com/watch?v=SC4iRIjBpww&list=PLoDTSobb3PMKfPj7bkjgtlyLqtzxZGsOr&index=2&ab_channel=Ho%C3%A0ngKhangTr%E1%BA%A7n)
- Đọc và phân tích thông tin mà tính năng "File History" trên Window 8+ cung cấp:
  -  Đọc dữ liệu bảng bằng ESE Viewer
  -   Xem thông tin các trường liên quan và trích xuất các timestamp
  -   Convert các timestamp bằng phần mềm DCode và xác định thời gian thực tế chính xác.

- Xem thông tin file được bảo toàn rời rạc với các timestamp được append bằng backup trên thiết bị sao lưu
- File cấu hình không bị ảnh hưởng khi file bị xóa, chỉ bị tác động khi dùng tính năng "Clean up Version"

---
## Plaso(Log2Timeline)

Link youtube: 
[Memory](https://www.youtube.com/watch?v=Zcn_nKScBWM&list=PLoDTSobb3PMKfPj7bkjgtlyLqtzxZGsOr&index=4&ab_channel=Ho%C3%A0ngKhangTr%E1%BA%A7n) <br>
[Disk image](https://www.youtube.com/watch?v=GXl3lGuDJz0&list=PLoDTSobb3PMKfPj7bkjgtlyLqtzxZGsOr&index=4&ab_channel=Ho%C3%A0ngKhangTr%E1%BA%A7n)


- Sử dụng một file disk image (dd) được dump từ hệ thống và dùng log2timeline để tạo supertimeline

- Trích xuất dữ liệu thành SQLite database bằng log2timeline.py. Sử dụng một số parser (chạy khá lâu, tự thử nghiệm với mỗi loại dưới, demo sử dụng full các parsers):
	* chrome_preferences : Parser for Google Chrome Preferences files.
	* bash_history : Parser for Bash history files.
	* esedb : Parser for Extensible Storage Engine (ESE), Database File (EDB) format)
	* filestat : Parser for file system stat information.
	* gdrive_synclog : Parser for Google Drive Sync log files.
	* webhist
	* windows_usb_devices : Parser for Windows USB device Registry data.

    -  Dùng psort để trích xuất dữ liệu. Trích xuất các trường thông tin cần thiết:
    	* Browser_search

    - Sử dụng Timeline Explorer để đọc dữ liệu

- Đọc một file memory (.raw) được dump của Window và dùng plugin timeliner của volatility để generate timeline từ bộ nhớ

