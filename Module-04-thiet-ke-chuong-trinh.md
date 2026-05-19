# Module 04: Thiết kế chương trình học cá nhân hóa

**Một chương trình tốt cân bằng chuẩn chung, nhu cầu riêng, đời sống thật và đường chuyển tiếp.**

## 1. First principles

**Bản chất:** Chương trình học là bản thiết kế có chủ đích về điều trẻ cần học, vì sao học, học theo thứ tự nào, học bằng trải nghiệm nào và biết mình đạt bằng chứng gì.

**Cơ chế:** Cá nhân hóa không có nghĩa mỗi ngày tùy hứng. Nó nghĩa là cùng một chuẩn hoặc mục tiêu có thể đi qua nhịp, tài nguyên, dự án và cách phản hồi khác nhau.

| Thành phần | Câu hỏi | Ví dụ |
|---|---|---|
| Chuẩn | Trẻ cần đạt điều gì? | Đọc hiểu văn bản, lập luận toán, viết đoạn, giao tiếp tiếng Anh. |
| Trình tự | Học gì trước để học cái sau? | Phân số trước tỉ lệ; câu trước đoạn văn. |
| Phương pháp | Học bằng cách nào? | Bài giảng ngắn, thí nghiệm, đọc sách, dự án. |
| Bằng chứng | Chứng minh đạt bằng gì? | Bài kiểm tra, sản phẩm, thuyết trình, portfolio. |
| Chuyển tiếp | Kết quả này dùng ở đâu? | Quay lại trường, thi chứng chỉ, du học, học nghề. |

## 2. Bốn lớp chương trình

| Lớp | Nội dung | Cách kiểm tra |
|---|---|---|
| Nền tảng bắt buộc | Đọc, viết, toán, khoa học, ngôn ngữ, sức khỏe, công dân. | Chuẩn theo tuổi/lớp, bài đánh giá định kỳ. |
| Năng lực học tập | Tự học, ghi chú, hỏi, tìm nguồn, quản lý thời gian. | Nhật ký học, phản tư, mức độc lập tăng dần. |
| Dự án cá nhân | Chủ đề trẻ quan tâm, sản phẩm thật. | Rubric sản phẩm và phản hồi bên ngoài. |
| Đời sống và cộng đồng | Việc nhà, tài chính cá nhân, giao tiếp, văn hóa, tình nguyện. | Hành vi quan sát được trong bối cảnh thật. |

## 3. Cách lập kế hoạch 12 tháng

1. Xác định mục tiêu chuyển tiếp: tiếp tục homeschool, quay lại trường, thi chứng chỉ, vào chương trình quốc tế, hay học linh hoạt.
2. Đánh giá điểm hiện tại của trẻ ở các năng lực nền tảng.
3. Chọn 3-5 ưu tiên chính cho năm học; không chọn 15 ưu tiên.
4. Chia năm thành chu kỳ 6-8 tuần.
5. Mỗi chu kỳ có sản phẩm, phản hồi và rà soát.
6. Giữ một ngày/tuần cho cộng đồng, vận động, thiên nhiên hoặc dự án ngoài nhà.

## 4. Ví dụ khung tuần

| Khối | Tần suất | Mục tiêu |
|---|---|---|
| Đọc sâu tiếng Việt | 4 buổi/tuần | Ngôn ngữ, tư duy, văn hóa. |
| Toán nền tảng | 4 buổi/tuần | Tư duy định lượng và giải quyết vấn đề. |
| Tiếng Anh | 3 buổi/tuần | Nghe, nói, đọc, viết theo mục tiêu chuyển tiếp. |
| Khoa học/dự án | 2 buổi/tuần | Quan sát, thí nghiệm, giải thích. |
| Nghệ thuật/vận động | 3 buổi/tuần | Cơ thể, cảm xúc, biểu đạt. |
| Cộng đồng | 1-2 buổi/tuần | Bạn bè, hợp tác, xung đột, vai trò xã hội. |

## 5. Rủi ro thiết kế

- Chương trình quá giống trường nhưng thiếu bạn học và giáo viên chuyên môn.
- Chương trình quá tự do nhưng không có chuẩn đọc, viết, toán.
- Chạy theo tài liệu nước ngoài mà bỏ ngôn ngữ, văn hóa và chuyển tiếp Việt Nam.
- Lịch kín hoạt động nhưng không có thời gian phản tư và nghỉ.

## 6. Tình huống ứng dụng

Gia đình mua ba chương trình: toán Singapore, tiếng Anh Mỹ và khoa học online. Sau hai tháng, trẻ làm nhiều bài nhưng không có sản phẩm tích hợp, phụ huynh không biết trẻ đang tiến bộ theo chuẩn nào.

**Vấn đề thật:** gia đình đang mua nội dung, chưa thiết kế chương trình. Nội dung trả lời “học cái gì”; chương trình trả lời “vì sao học, theo thứ tự nào, đến mức nào, bằng chứng gì”.

![Nhiều học liệu rời rạc chưa tạo thành chương trình học có chủ đích](assets/visuals/module-04/01-scenario.png)
*Caption: Hình này giúp người học thấy sự khác biệt giữa mua nhiều nguồn nội dung và thiết kế một chương trình có chuẩn, trình tự, trải nghiệm và bằng chứng.*

## 7. Mô hình tư duy: Từ chuẩn đến trải nghiệm

| Lớp thiết kế | Câu hỏi | Đầu ra |
|---|---|---|
| Chuẩn | Trẻ cần biết/làm được gì? | Mục tiêu đo được. |
| Chẩn đoán | Trẻ đang ở đâu? | Điểm xuất phát. |
| Lộ trình | Học gì trước/sau? | Bản đồ 12 tháng. |
| Trải nghiệm | Học bằng hoạt động nào? | Buổi học, dự án, đọc, thí nghiệm. |
| Bằng chứng | Chứng minh ra sao? | Portfolio, bài kiểm tra, sản phẩm. |

![Các lớp thiết kế chương trình từ chuẩn đến trải nghiệm và bằng chứng](assets/visuals/module-04/02-mechanism-model.png)
*Caption: Các lớp xếp chồng nhắc rằng chương trình tốt phải đi từ chuẩn và chẩn đoán đến lộ trình, trải nghiệm và bằng chứng học tập.*

## 8. Workflow thiết kế chương trình 12 tháng

1. Chọn đường chuyển tiếp: trường Việt Nam, quốc tế, hybrid, tự học dài hạn.
2. Lập bảng năng lực nền tảng theo tuổi/lớp.
3. Đánh giá điểm hiện tại bằng bài mẫu hoặc mentor.
4. Chọn 3 ưu tiên học thuật và 2 ưu tiên phát triển.
5. Chia thành 6 chu kỳ, mỗi chu kỳ 6-8 tuần.
6. Gắn mỗi chu kỳ với sản phẩm và rubric.

![Bản thiết kế chương trình 12 tháng theo chu kỳ, sản phẩm và portfolio](assets/visuals/module-04/03-workflow-practice.png)
*Caption: Hình này giúp chuyển khung chương trình 12 tháng thành các chu kỳ học có sản phẩm, phản hồi và điểm rà soát cụ thể.*

## 9. Rubric đầu ra

| Mức | Dấu hiệu |
|---|---|
| Chưa đạt | Chỉ có danh sách sách, khóa học hoặc ứng dụng. |
| Đạt | Có mục tiêu, lịch, tài nguyên và đánh giá cơ bản. |
| Xuất sắc | Có chuẩn đối chiếu, chẩn đoán đầu vào, sản phẩm theo chu kỳ, portfolio và phương án chuyển tiếp. |
