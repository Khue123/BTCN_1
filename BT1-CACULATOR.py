import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi nhấn nút số hoặc toán tử
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Hàm xóa toàn bộ biểu thức đã nhập
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Hàm tính toán kết quả của biểu thức
def btn_equal():
    global expression
    try:
        # Sử dụng eval để tính kết quả
        result = str(eval(expression))
        input_text.set(result)
        expression = result  # Gán kết quả làm biểu thức tiếp theo
    except:
        # Thông báo lỗi nếu có lỗi cú pháp
        messagebox.showerror("Error", "Invalid Input")
        expression = ""

# Khởi tạo biến toàn cục cho biểu thức
expression = ""
window = tk.Tk()  # Tạo cửa sổ chính
window.geometry("312x324")  # Kích thước cửa sổ
window.resizable(0, 0)  # Không cho phép thay đổi kích thước cửa sổ
window.title("Calculator")  # Tiêu đề của cửa sổ

input_text = tk.StringVar()  # Chuỗi hiển thị biểu thức

# Khung hiển thị biểu thức
input_frame = tk.Frame(window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

# Trường nhập biểu thức bên trong khung
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # ipady để tăng chiều cao trường nhập

# Khung chứa các nút
btns_frame = tk.Frame(window, width=312, height=272.5, bg="grey")
btns_frame.pack()

# Hàng đầu tiên
tk.Button(btns_frame, text="C", width=32, height=3, bg="#eee", cursor="hand2", command=btn_clear).grid(row=0, column=0, columnspan=3)
tk.Button(btns_frame, text="/", width=10, height=3, bg="#FFA07A", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3)

# Hàng thứ hai
tk.Button(btns_frame, text="7", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0)
tk.Button(btns_frame, text="8", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1)
tk.Button(btns_frame, text="9", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2)
tk.Button(btns_frame, text="*", width=10, height=3, bg="#FFA07A", cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3)

# Hàng thứ ba
tk.Button(btns_frame, text="4", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0)
tk.Button(btns_frame, text="5", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1)
tk.Button(btns_frame, text="6", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2)
tk.Button(btns_frame, text="-", width=10, height=3, bg="#FFA07A", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3)

# Hàng thứ tư
tk.Button(btns_frame, text="1", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0)
tk.Button(btns_frame, text="2", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1)
tk.Button(btns_frame, text="3", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2)
tk.Button(btns_frame, text="+", width=10, height=3, bg="#FFA07A", cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3)

# Hàng thứ năm
tk.Button(btns_frame, text="0", width=21, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2)
tk.Button(btns_frame, text=".", width=10, height=3, bg="#fff", cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2)
tk.Button(btns_frame, text="=", width=10, height=3, bg="#FFA07A", cursor="hand2", command=btn_equal).grid(row=4, column=3)

window.mainloop()  # Chạy vòng lặp chính của ứng dụng
