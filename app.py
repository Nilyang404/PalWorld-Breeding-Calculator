import PBCalculator

import tkinter as tk
from tkinter import ttk
import pandas as pd

# 假设df是一个包含name_cn列的DataFrame
df = pd.DataFrame({'name_cn': ['选项1', '选项2', '选项3']})

# 计算函数
def calculate(event):
    # 获取下拉菜单的值
    choice1 = combo1.get()
    choice2 = combo2.get()
    # 执行一些计算（这里只是一个示例）
    result = f"您选择了：{choice1} 和 {choice2}"
    # 显示结果
    result_label.config(text=result)

# 创建主窗口
root = tk.Tk()
root.title("Pal Breeding Calculator")

# 创建Notebook（标签页容器）
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# 添加标签页
notebook.add(tab1, text='标签页1')
notebook.add(tab2, text='标签页2')
notebook.add(tab3, text='标签页3')
notebook.pack(expand=True, fill="both")

# 第一个标签页中的组件
combo1 = ttk.Combobox(tab1, values=df['name_cn'].tolist())
combo2 = ttk.Combobox(tab1, values=df['name_cn'].tolist())
result_label = tk.Label(tab1, text="结果将显示在这里")

# 放置组件
combo1.pack()
combo2.pack()
result_label.pack()

# 绑定事件
combo1.bind("<<ComboboxSelected>>", calculate)
combo2.bind("<<ComboboxSelected>>", calculate)

# 运行主循环
root.mainloop()