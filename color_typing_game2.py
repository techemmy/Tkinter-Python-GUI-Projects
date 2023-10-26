import customtkinter as ctk
import random

root = ctk.CTk()
root.title("Color Typing Game")
root.minsize(500, 350)


def reset_game():
    timer_var.set(TOTAL_GAME_TIME)
    score_var.set(0)

    timer.configure(text=f"Time left: {timer_var.get()}s", text_color="white")
    user_score.configure(text=f"Score: {score_var.get()}")


def run_timer():
    time_left = timer_var.get() - 1
    timer_var.set(time_left)
    timer.configure(text=f"Time left: {time_left}s")

    timer_id_var.set(root.after(1000, run_timer))

    if timer_var.get() <= 0:
        root.after_cancel(timer_id_var.get())
        timer.configure(text="Time up!", text_color="red")
        game_running_var.set(False)

def verify_answer(answer):
    if answer == current_color_var.get():
        score_var.set(score_var.get() + 1)
    user_score.configure(text=f"Score: {score_var.get()}")


def set_next_text():
    current_color_var.set(random.choice(COLORS))
    changing_text.configure(
        text=random.choice(COLORS), text_color=current_color_var.get()
    )


def start_game(e):
    if game_running_var.get() == False:
        game_running_var.set(True)
        reset_game()
        run_timer()
        set_next_text()
    elif game_running_var.get() == True and timer_var.get() > 0:
        verify_answer(user_input.get())
        set_next_text()
        user_input.delete(0, "end")


COLORS = ["red", "green", "blue", "yellow", "violet", "black", "white"]
TOTAL_GAME_TIME = 20

game_running_var = ctk.BooleanVar()
game_running_var.set(False)

timer_var = ctk.IntVar()
timer_var.set(TOTAL_GAME_TIME)

score_var = ctk.IntVar()
score_var.set(0)

timer_id_var = ctk.StringVar()

current_color_var = ctk.StringVar()

app_frame = ctk.CTkFrame(root, width=700)
app_frame.pack(padx=20, pady=20, expand=True, fill=ctk.BOTH)

time_and_score_frame = ctk.CTkFrame(app_frame)

timer = ctk.CTkLabel(time_and_score_frame, text=f"Time left: {timer_var.get()}s")
timer.pack(side="left", padx=10)

user_score = ctk.CTkLabel(time_and_score_frame, text=f"Score: {score_var.get()}")
user_score.pack(side="right", padx=10)

time_and_score_frame.pack(fill=ctk.X)

ctk.CTkLabel(
    app_frame, text="Instruction: Enter the color of the text you see\nand not the text",
    font=("Montserrat", 18, "italic"), text_color='lightblue'
).pack(padx=10, pady=20)

changing_text = ctk.CTkLabel(app_frame, text="Blue", font=("Montserrat", 30, "bold"))
changing_text.pack(pady=20, fill=ctk.X)

user_input = ctk.CTkEntry(app_frame, width=300, height=50)
user_input.pack()
user_input.bind("<Return>", start_game)

ctk.CTkLabel(app_frame, text="Press enter to start/reset the game...", text_color="grey").pack()


root.mainloop()
