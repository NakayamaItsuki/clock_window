import tkinter as tk
import time

def update_time():
    current_date = time.strftime('%m月%d日')
    current_day_of_week = time.strftime('%A')
    day_of_week_kanji = {"Monday": "月", "Tuesday": "火", "Wednesday": "水",
                         "Thursday": "木", "Friday": "金", "Saturday": "土", "Sunday": "日"}
    date_label.config(text=f'{current_date}({day_of_week_kanji[current_day_of_week]})\n')
    current_time = time.strftime('%H時%M分')
    time_label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("デジタル時計")

# ウィンドウの背景色を白に設定
root.configure(bg='white')

# ウィンドウサイズを設定
window_width = 500
window_height = 200
root.geometry(f'{window_width}x{window_height}')

# 画面の解像度を取得し、ウィンドウを中央に配置
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f'+{center_x}+{center_y}')

# 日付を表示するラベルを作成（背景色を白に設定）
date_label = tk.Label(root, font=('Helvetica', 48), fg='black', bg='white')
date_label.pack()

# 時刻を表示するラベルを作成（背景色を白に設定）
time_label = tk.Label(root, font=('Helvetica', 60), fg='black', bg='white')
time_label.pack()

update_time()

root.mainloop()

