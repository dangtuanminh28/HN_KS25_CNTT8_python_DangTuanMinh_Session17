import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def show_product(product_list) :
    if product_list == [] :
        print("Danh sách trống!")
        return
    else :
        print("--- DANH SÁCH TEM NHÃN ---")
        for product in product_list :
            prod = product.split('-')
            print(f"Mã: {prod[0]:<10} | Tên: {prod[1]:<20} | Giá: {int(prod[2]):,} | Rating: {prod[3]}*")

def get_price(item):
    return item[2]

def get_rating(item):
    return item[3]

def sort_product(product_list) :
    processed_list = []
    if product_list == [] :
        print("Danh sách trống!")
        return
    else :
        for product in product_list:
            prod = product.split('-')
            prod[2] = int(prod[2])
            prod[3] = float(prod[3])
            processed_list.append(prod)

        processed_list.sort(key=get_price)
        processed_list.sort(key=get_rating, reverse=True)
        print("--- SẮP XẾP SẢN PHẨM ---")
        print("Đã sắp xếp thành công! Cập nhật danh sách:")
        for prod in processed_list:
            print(f"Mã: {prod[0]:<10} | Tên: {prod[1]:<20} | Giá: {int(prod[2]):,} | Rating: {prod[3]}*")

def total_product(product_list) :
    if product_list == [] :
        print("Danh sách trống!")
        return
    else :
        count = 0
        print("--- TỔNG GIÁ TRỊ KHO ---")
        for product in product_list :
            prod = product.split('-')
            count += int(prod[2])
    print(f"Tổng giá trị các mặt hàng hiện tại là: {count:,} VND")

while True :
    print("""
============= E-COMMERCE ANALYTICS =============
1. Hiển thị tem nhãn sản phẩm (format_map & F-String)
2. Sắp xếp sản phẩm thông minh (sort key)
3. Tính tổng giá trị kho hàng (reduce)
4. Đóng hệ thống
================================================
""")
    choice = input("Chọn chức năng (1-4): ").strip()
    if choice == '1' :
        show_product(product_list)
    elif choice == '2' :
        sort_product(product_list)
    elif choice == '3' :
        total_product(product_list)
    elif choice == '4':
        print("Thoát chương trình")
        break
    else :
        print("Vui lòng nhập lại(1-4)!")
        