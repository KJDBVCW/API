let selectedDrinkId = null;

$(document).ready(function () {
    // Hiển thị thông báo đang tải trước khi gọi API
    $("#drink-list").html("<p>Đang tải dữ liệu...</p>");

    // Lấy danh sách đồ uống từ API
    $.ajax({
        url: "http://localhost:8000/api/drinks/",
        method: "GET",
        success: function (data) {
            $('#drink-list').empty();

            if (data.length === 0) {
                $('#drink-list').append('<p>Hiện tại không có đồ uống nào.</p>');
            } else {
                data.forEach(function (drink) {
                    const drinkItem = $('<div class="product-card"></div>');

                    const imageWrapper = $('<div class="image-wrapper"></div>');
                    const drinkImage = $('<img>').attr('src', drink.image_url || 'https://via.placeholder.com/300');
                    imageWrapper.append(drinkImage);

                    const info = $('<div class="product-info"></div>');
                    const drinkName = $('<h3></h3>').text(drink.name);
                    const drinkPrice = $('<p></p>').text("Giá: " + Number(drink.price).toLocaleString('vi-VN') + " VNĐ");
                    info.append(drinkName, drinkPrice);

                    const orderButton = $('<button class="order-btn"></button>')
                        .text("Đặt hàng")
                        .click(function () {
                            selectedDrinkId = drink.id;
                            $("#drinkName").text(drink.name);
                            
                        });

                    drinkItem.append(imageWrapper, info, orderButton);
                    $('#drink-list').append(drinkItem);
                });
            }

            
        },
        error: function (error) {
            console.error("Lỗi gọi API:", error);
            alert("❌ Lỗi gọi API. Vui lòng thử lại sau.");
        }
    });

   
});
