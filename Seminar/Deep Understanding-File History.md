# File History - "Take it seriously now"

**Mô tả**: Tìm hiểu kỹ hơn về thông tin được lưu trữ và các file liên quan trong File History, phục vụ cho Memory Forensic

**Yêu cầu**: Tham khảo bài trước [Tutorial - File History](Fundamental-File%20History-Window.md)

## Forensic trên Config File:

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

Đuôi mở rộng .edb - Extensible Storage Engine (ESE) Database (Tham khảo thêm: [Extensible Storage Engine](https://en.wikipedia.org/wiki/Extensible_Storage_Engine)). Là một dạng database được sử dụng rộng rãi bởi Windows cho nhiều chức năng như  Microsoft Exchange Server, Active Directory, Windows Search, ... Và ở đây file **Catalog1.edb** lưu trữ các thông tin cần thiết để cho việc backup hoạt động một cách hợp lý như metadata, id, tên file, ... 

Để hiểu rõ hơn, ta sẽ mở file bằng ứng dụng `ESEDatabaseView`. File _Catalog1.edb_ thông thường gồm 7 tables. Ta sẽ xem những table chủ yếu phục vụ cho Giám định (Examination), xem xét 4 tables sau:
- `backupset`
- `file`
- `namespace`
- `string`

Thông tin cơ bản: 

| Table | Column | Description (all time-related values are Windows 64-bit timestamps) |
| ----- | ----- | ------ |
| backupset | id | Index of backup operation
|  | timestamp | Start time of backup operation
| file | id | Index of file
| | childId | Foreign key to id column of ‘string’ table (for a file’s name)
| | parentId | Foreign key to id column of ‘string’ table (for a folder where childId is located)
| | fileSize | Backed up file’s size
| namespace | childId | Foreign key to id column of ‘string’ table (for a file or folder’s name)
| | parentId | Foreign key to id column of ‘string’ table (for a folder where childId is located)
| | fileRecordId | Foreing key to id column of ‘file’ table
| | fileCreated | File creation time
| | fileModified | File modification time
| | tCreated | Foreign key to id column of ‘backupset’ table
| | usn | Backed up file’s USN
| string | id | Index of string
| | string | Backed up file’s name or folder path

Ví dụ về quan hệ giữa các tables trong file `Catalog.edb`

![image](https://user-images.githubusercontent.com/48288606/164501421-4ff003e3-178f-4751-9595-6333c692da10.png)

Những tables khác (có thể tồn tại ):
- `library`
- `MsysLocales`
- `MsysObjects`
- `MsysObjectsShadow`
- `MSysObjids`

### Catalog2.edb

Hỗ trợ làm backup cho `Catalog1.edb`

### Config1.xml

Một file định dạng XML, lưu các trường giá trị và có thể thay đổi tùy theo nhu cầu cấu hình và sử dụng. Cấu trúc các trường thông tin cơ bnar như sau:

- `DataProtectionUserConfig `
  - `UserName` : Tên user của nơi được backup
  - `PCName` : ComputerName của nơi được backup
  - `UserId` : Id của user
  - `Library`
    - `LibraryName`
    - `Folder`
  - `UserFolder` : Những folders của user sẽ được backup.
  - `LocalCatalogPath1` : Nơi lưu giữ (local) file "Catalog.edb"
  - `StagingArea`
    - `StagingAreaPath`
    - `StagingAreaMaximumCapacity`
    - `StagingAreaWarningThreshold`
  - `AvailabilityPolicies`
    - `TargetAbsenceTime`
    - `TimeInUnprotectedState`
  - `RetentionPolicies`
    - `RetentionPolicyType` : Thông thường ta để thời gian giữ một _backup version_ là **Forever** trong "Control Panel". Tương đương với việc **DISABLED** chức năng này đi
    - `MinimumRetentionAge` : Thời gian tối thiểu để giữ một _backup version_ trước khi xóa nó vĩnh viễn.
  - `DPFrequency` : Khoảng thời gian tạo các bản sao lưu với các version khác nhau của ổ đĩa
  - `DPStatus` : ENABLED hoặc DISABLED tính năng trên.
  - `Target`: Cấu hình cho nơi lưu trữ tại ổ cứng/Network Drive
    - `TargetName` : Tên/nhãn(label) của ổ đĩa
    - `TargetUrl` : Tên Drive
    - `TargetVolumePath` : chỉ định "id" của ổ đĩa, sẽ nói rõ hơn trong phần liên quan đến registry
    - `TargetDriveType` : có thể là ‘Fixed’, ‘Removable’, hoặc ‘Remote’ dựa theo loại kết nối đến target. Nếu ổ cứng rời sẽ là "Fixed"
    - `TargetConfigPath1` : Nơi chứa file config "Config1.xml"
    - `TargetConfigPath2` : Nơi chứa file config (dự phòng) "Config2.xml"
    - `TargetCatalogPath1` : Nơi chứa file catalog "Catalog1.edb"
    - `TargetCatalogPath2` : Nơi chứa file catalog (dự phòng) "Catalog2.edb"
    - `TargetBackupStorePath` : Đường dẫn lưu trữ file đích trong ổ cứng/Network Drive được chuẩn bị để lưu.
    - `TargetWarningThreshold`


### Config2.xml

Hỗ trợ làm backup cho `Config1.xml`

## Forensic trên Registry:

## Forensic trên Event Log:
