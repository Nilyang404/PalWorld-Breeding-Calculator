from PBCalculator import PBCalculator

import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import font

cal = PBCalculator()
def calculate_child(event):
    choice_1 = combo_1_tab1.get().split(" ")[1]
    choice_2 = combo2_tab1.get().split(" ")[1]
    no_1 = cal.name_cn_to_no(choice_1)
    no_2 = cal.name_cn_to_no(choice_2)
    no = cal.get_breed_result(no_1,no_2)
    name_cn = cal.no_to_name_cn(no)
    result = "NO." + no + " " + name_cn
    result_output_lable.config(text=result)
    print(combo_1_tab1.get() +" + " + combo2_tab1.get() + " = " + result)

def calculate_parents(event):
    child_name = combo_3_tab2.get().split(" ")[1]
    no = cal.name_cn_to_no(child_name)
    combos = cal.get_parents_by_child(no)
    print(combos)
    result = ""
    for combo in combos:
        no_1, no_2 = combo[0],combo[1]
        name_1, name_2 = cal.no_to_name_cn(no_1), cal.no_to_name_cn(no_2)
        item = "NO." + no_1 + " " + name_1 + " + " + "NO." + no_2 + " " + name_2
        result = result + item + "\n"

    result_output_lable_tab_2.delete("1.0", "end")
    result_output_lable_tab_2.insert("1.0",result)

if __name__ == '__main__':

    cal = PBCalculator()
    df = cal.data
    df["combined"] = "NO." + df['NO'].astype(str) + " " + df['name_cn']
    pal_list_cn =df["combined"] .tolist()
    pal_list_en =df["combined"] .tolist()

    root = tk.Tk()
    root.title("Pal Breeding Calculator 0.1")

    # style configure
    style = ttk.Style()
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(size=10)

    style.configure("Title", font=("Helvetica", 16))
    style.configure("TContent", font=("Helvetica", 14))
    style.configure("TLable", font=("Helvetica", 14))
    style.configure("TButton", font=("Helvetica", 14))

    window_width = 350
    window_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # create tab
    notebook = ttk.Notebook(root)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)

    # table content
    notebook.add(tab1, text='预测子女')
    notebook.add(tab2, text='父母组合')
    notebook.add(tab3, text='繁殖方案')
    notebook.pack(expand=True, fill="both")

    # page 1 content
    combo_1_tab1 = ttk.Combobox(tab1, values=pal_list_cn)
    plus_label = tk.Label(tab1, text="+")
    combo2_tab1 = ttk.Combobox(tab1, values=pal_list_cn)
    result_label = tk.Label(tab1, text="预测结果:")
    result_output_lable= tk.Label(tab1, text="NO.1 绵悠悠")

    # defalut values
    combo_1_tab1.set(pal_list_cn[0])
    combo2_tab1.set(pal_list_cn[1])

    # put
    combo_1_tab1.pack(pady = (50,10))
    plus_label.pack(pady=2)
    combo2_tab1.pack(pady = 10)
    result_label.pack(pady = 10)
    result_output_lable.pack(pady = 10)

    # bind event
    # triger by selecting
    combo_1_tab1.bind("<<ComboboxSelected>>", calculate_child)
    combo2_tab1.bind("<<ComboboxSelected>>", calculate_child)

    # page 2 content
    combo_3_tab2 = ttk.Combobox(tab2, values=pal_list_cn)
    result_label_tab_2 = tk.Label(tab2, text="父母组合(顺序不分先后):")
    result_output_lable_tab_2= tk.Text(tab2,
                                       borderwidth=2,
                                       width=250,
                                       )

    # defalut values
    # combo3.set(pal_list_cn[0])

    # put
    combo_3_tab2.pack(pady = (20,10))
    result_label_tab_2.pack(pady = 10)
    result_output_lable_tab_2.pack(pady = 10)

    # bind event
    combo_3_tab2.bind("<<ComboboxSelected>>", calculate_parents)


    # page 3 content

    content_label = tk.Label(tab3, text="施工中...")
    content_label.pack(pady=(180, 10))

    root.mainloop()