import tkinter as tk
from tkinter import filedialog, messagebox

class TextReader:
    def __init__(self, root):
        # 初始化窗口
        self.root = root
        self.root.title("本地阅读器")
        
        # 创建文本显示区域
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(expand=1, fill="both")
        
        # 创建菜单栏
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="打开", command=self.open_file)
        self.file_menu.add_command(label="退出", command=self.root.quit)
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)

    def open_file(self):
        # 打开文件对话框
        file_path = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if file_path:
            try:
                # 读取文件内容并显示
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)  # 清空文本区域
                    self.text_area.insert(tk.END, content)  # 插入新内容
            except Exception as e:
                # 处理文件打开错误
                messagebox.showerror("错误", f"无法打开文件：{e}")

# 启动程序
if __name__ == "__main__":
    root = tk.Tk()
    app = TextReader(root)
    root.mainloop()