import tkinter as tk
import tkinter.messagebox


grid = [["", "", ""], ["", "", ""], ["", "", ""]]
sign = "X"
turns = 1


def button_click(button, current_sign):
    global sign, turns
    if button == "button1":
        grid[0][0] = current_sign
        button1.config(text=current_sign)
    elif button == "button2":
        grid[0][1] = current_sign
        button2.config(text=current_sign)
    elif button == "button3":
        grid[0][2] = current_sign
        button3.config(text=current_sign)
    elif button == "button4":
        grid[1][0] = current_sign
        button4.config(text=current_sign)
    elif button == "button5":
        grid[1][1] = current_sign
        button5.config(text=current_sign)
    elif button == "button6":
        grid[1][2] = current_sign
        button6.config(text=current_sign)
    elif button == "button7":
        grid[2][0] = current_sign
        button7.config(text=current_sign)
    elif button == "button8":
        grid[2][1] = current_sign
        button8.config(text=current_sign)
    elif button == "button9":
        grid[2][2] = current_sign
        button9.config(text=current_sign)
    if turns < 9:
        check_for_winner(grid, current_sign)
        if current_sign == "X":
            sign = "O"
        else:
            sign = "X"
        turns += 1
    else:
        tkinter.messagebox.showinfo("Message", "Nobody wins the game!")


def get_winner_name(current_sign):
    if current_sign == "X":
        return "Player 1"
    return "Player 2"


def check_for_winner(grid, current_sign):
    if grid[0][0] == current_sign:
        if (
            (grid[0][1] == current_sign and grid[0][2] == current_sign)
            or (grid[1][0] == current_sign and grid[2][0] == current_sign)
            or (grid[1][1] == current_sign and grid[2][2] == current_sign)
        ):
            tkinter.messagebox.showinfo(
                "Message", f"{get_winner_name(current_sign)} wins the game!"
            )
    elif grid[0][2] == current_sign:
        if (grid[1][2] == current_sign and grid[2][2] == current_sign) or (
            grid[1][1] == current_sign and grid[2][0] == current_sign
        ):
            tkinter.messagebox.showinfo(
                "Message", f"{get_winner_name(current_sign)} wins the game!"
            )
    elif grid[0][1] == current_sign:
        if grid[1][1] == current_sign and grid[2][1] == current_sign:
            tkinter.messagebox.showinfo(
                "Message", f"{get_winner_name(current_sign)} wins the game!"
            )
    elif grid[1][0] == current_sign:
        if grid[1][1] == current_sign and grid[1][2] == current_sign:
            tkinter.messagebox.showinfo(
                "Message", f"{get_winner_name(current_sign)} wins the game!"
            )
    elif grid[2][0] == current_sign:
        if grid[2][1] == current_sign and grid[2][2] == current_sign:
            tkinter.messagebox.showinfo(
                "Message", f"{get_winner_name(current_sign)} wins the game!"
            )


def reset_game():
    global grid, sign, turns
    button1.config(text="  ")
    button2.config(text="  ")
    button3.config(text="  ")
    button4.config(text="  ")
    button5.config(text="  ")
    button6.config(text="  ")
    button7.config(text="  ")
    button8.config(text="  ")
    button9.config(text="  ")
    grid = [["", "", ""], ["", "", ""], ["", "", ""]]
    sign = "X"
    turns = 1


my_tk = tk.Tk()

button1 = tk.Button(
    text="  ", height=4, width=8, command=lambda: button_click("button1", sign)
)
button1.grid(row=3, column=0)
button2 = tk.Button(
    text="  ", height=4, width=8, command=lambda: button_click("button2", sign)
)
button2.grid(row=3, column=1)
button3 = tk.Button(
    text="  ", height=4, width=8, command=lambda: button_click("button3", sign)
)
button3.grid(row=3, column=2)

button4 = tk.Button(
    text="  ", height=4, width=8, command=lambda: button_click("button4", sign)
)
button4.grid(row=4, column=0)
button5 = tk.Button(
    text="  ", height=4, width=8, command=lambda: button_click("button5", sign)
)
button5.grid(row=4, column=1)
button6 = tk.Button(
    text="  ", height=4, width=8, command=lambda: button_click("button6", sign)
)
button6.grid(row=4, column=2)

button7 = tk.Button(
    text="  ", height=4, width=8, command=lambda: button_click("button7", sign)
)
button7.grid(row=5, column=0)
button8 = tk.Button(
    text="  ", height=4, width=8, command=lambda: button_click("button8", sign)
)
button8.grid(row=5, column=1)
button9 = tk.Button(
    text="  ", height=4, width=8, command=lambda: button_click("button9", sign)
)
button9.grid(row=5, column=2)

bottom_left_frame = tk.LabelFrame()
bottom_left_frame.grid(row=6, column=0)
bottom_right_frame = tk.LabelFrame()
bottom_right_frame.grid(row=6, column=2)


restart_button = tk.Button(bottom_left_frame, text="Reset", command=reset_game)
restart_button.pack()
quit_button = tk.Button(bottom_right_frame, text="Quit", command=quit)
quit_button.pack()


my_tk.title("Tic Tac Toe")
my_tk.mainloop()
