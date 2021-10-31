# Project-1
## Cấu trúc project :
* data/Articles: Chứa các article từ 1-1000
* data/nytimes_news_articles: file data gốc
* service/Split_Articles: Tách article
* service/Split_Words: Tách từ 
* service/Summarize_Words: Tổng hợp cặp <từ, MVB> ở tất cả các văn bản.
* service/Inverse_Index: Sắp xếp và tạo chỉ mục ngược (Chưa có)
* service/Logic_Operator: Định nghĩa các thuật toán lấy AND, OR, NOT giữa 2 ds thẻ định vị 
## Lưu ý : 
* Danh sách từ điển là list_dict chứa các phần tử : <word, len (ds thẻ định vị ) , index xác định vị trí ds thẻ định vị>
* Danh sách thẻ định vị là list_doc_id chứa tất cả các danh sách các thẻ định vị của các từ trong văn bản 
