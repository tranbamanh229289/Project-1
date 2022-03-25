# Project-1
## Cấu trúc project :
### file Data:
* Data/Articles: Chứa các article được đánh chỉ mục từ từ 0-999
* Data/nytimes_news_articles: file data gốc
* Data/list_doc_id: danh sách thẻ định vị
* Data/list_dict: bộ từ điển ánh xạ tới danh sách thẻ định vị 
* ### file app:
* app/query/service/create_iverse_index: Thực hiện đánh chỉ mục cho các articles, bao gồm các hoạt động tách các article từ file data gốc, tách từ, tổng hợp từ, sắp xếp và đánh chỉ mục ngược cho ra các file list_doc_id và list_dict 
* app/query/service/create_hash_table: tạo bảng băm để truy vấn danh sách thẻ định vị từ đầu vào là từ .
* app/query/service/query_processing: xử lý truy vấn từ người dùng , xử lý thứ tự truy vấn ưu tiên với các toán tử NOT>AND>NOT khi người dùng k có ngoặc, nếu có ngoặc thì thực hiện theo thứ tự ưu tiên ngoặc .
