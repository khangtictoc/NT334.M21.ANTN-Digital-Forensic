# File History - "Take it seriously now"

**Mô tả**: Tìm hiểu kỹ hơn về thông tin được lưu trữ và các file liên quan trong File History, phục vụ cho Memory Forensic

**Yêu cầu**: Tham khảo bài trước [Tutorial - File History](Fundamental-FileHistory-Window.md)

## Hệ thống quản lý và cấu hình:

Các file cấu hình và cài đặt được lưu tại đường dẫn `%LOCALAPPDATA%\Microsoft\Windows\FileHistory\Configuration`.


  
Bao gồm những file (sẽ dùng cho Forensic):
  
| File | Type (Extension) |
| ---- | ---------------- |
| [Catalog1.edb](#catalog1edb) | EDB - Extensible Storage Engine (ESE) Database |
| [Catalog2.edb](#catalog2edb)| EDB - Extensible Storage Engine (ESE) Database |
| Catalog1.jfm | (Không liên quan) |
| Catalog2.jfm | (Không liên quan) |
| [Config1.xml](#config1xml) | XML - extensible markup language |
| [Config2.xml](#config2xml) | XML - extensible markup language |



### Catalog1.edb

### Catalog2.edb

Hỗ trợ làm backup cho `Catalog1.edb`

### Config1.xml

### Config2.xml


Hỗ trợ làm backup cho `Config1.xml`

