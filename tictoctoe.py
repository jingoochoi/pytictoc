import tkinter as tk
import tkinter.messagebox as mbox
import random
window=tk.Tk()
window.title('tictoctoe')
window.geometry('264x282')
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
labels = []  # 레이블 객체를 저장하는 리스트
clicked=set()
def check_winner(player):
    win_conditions = [
        [labels[0], labels[1], labels[2]],  # 가로 1줄
        [labels[3], labels[4], labels[5]],  # 가로 2줄
        [labels[6], labels[7], labels[8]],  # 가로 3줄
        [labels[0], labels[3], labels[6]],  # 세로 1줄
        [labels[1], labels[4], labels[7]],  # 세로 2줄
        [labels[2], labels[5], labels[8]],  # 세로 3줄
        [labels[0], labels[4], labels[8]],  # 대각선 ↘
        [labels[2], labels[4], labels[6]]   # 대각선 ↙
    ]
    
    for condition in win_conditions:
        if all(label.cget("text") == player for label in condition):  
            return True
    return False

def oo(ko):
    if ko in clicked:return  # 리스트에서 제거 (존재할 때만)
    
    
    ko.config(text='o')  # 클릭한 레이블은 'o'로 변경
    clicked.add(ko)
    remain=[l for l in labels if l not in clicked]
    if remain:  # 리스트에 남은 레이블이 있다면
        chosen=random.choice(remain)
        chosen.config(text='x')  # 무작위 레이블을 선택해 'x'로 변경
        clicked.add(chosen)
    if check_winner('o'):
        print('win')
        mbox.showinfo('result','YOU WIN!')
    elif check_winner('x'):mbox.showinfo('result','YOU LOSE.T.T')
for i in range(3):
    for j in range(3):
        label = tk.Label(window, cursor='hand2', borderwidth=1, relief='solid', width=12, height=6)
        label.grid(row=i, column=j)
        label.bind('<Button-1>', lambda event, l=label: oo(l))  # 클릭 이벤트 바인딩
        labels.append(label)  # 리스트에 레이블 추가
window.mainloop()