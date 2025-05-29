// JavaScript cho trang add.html
document.getElementById("addItemForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // Lấy dữ liệu từ form
    const itemName = document.getElementById("itemName").value;
    const itemPrice = document.getElementById("itemPrice").value;
    const itemDescription = document.getElementById("itemDescription").value;
  
    const newItem = {
      name: itemName,
      price: itemPrice,
      description: itemDescription
    };
  
    // Gửi POST request đến API để thêm món mới vào cơ sở dữ liệu
    fetch('http://localhost:8000/api/drinks/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newItem)
    })
    .then(response => response.json())
    .then(data => {
      console.log('Món mới đã được thêm:', data);
      // Sau khi thêm món thành công, có thể chuyển hướng hoặc hiển thị thông báo
      window.location.href = "home.html"; // Ví dụ quay lại trang chính
    })
    .catch(error => {
      console.error('Lỗi khi thêm món:', error);
    });
  });
  