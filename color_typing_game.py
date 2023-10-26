import customtkinter as ctk
import random


COLORS = ["red", "green", "blue", "yellow", "violet", "black", "white"]
TOTAL_GAME_TIME = 5

time_left = TOTAL_GAME_TIME
score = 0
curr_color = random.choice(COLORS)


def reset_game():
    global time_left, score

    time_left = TOTAL_GAME_TIME
    score = 0

    timer.configure(text=f"Time left: {time_left}s", text_color="white")
    user_score.configure(text=f"Score: {score}")


def changeText():
    global curr_color

    curr_color = random.choice(COLORS)
    changing_text.configure(text=random.choice(COLORS), text_color=curr_color)


def run_timer():
    global time_left

    if time_left > 0:
        time_left -= 1
        timer.configure(text=f"Time left: {time_left}s")
        root.after(1000, run_timer)
    elif time_left == 0:
        timer.configure(text="Time up!", text_color="red")
        reset_btn.configure(state=ctk.NORMAL)


def start_game(event):
    global score

    if time_left == TOTAL_GAME_TIME:
        reset_btn.configure(state=ctk.DISABLED)
        run_timer()

    if time_left > 0:
        if user_input.get().lower() == curr_color:
            score += 1
            user_score.configure(text=f"Score: {score}")

        user_input.delete(0, "end")
        changeText()


root = ctk.CTk()
root.title("Color Typing Game")
root.minsize(500, 350)

app_frame = ctk.CTkFrame(root, width=700)
app_frame.pack(padx=20, pady=20, expand=True, fill=ctk.BOTH)

time_and_score_frame = ctk.CTkFrame(app_frame)
time_and_score_frame.pack(fill=ctk.X)

timer = ctk.CTkLabel(time_and_score_frame, text=f"Time left: {TOTAL_GAME_TIME}s")
timer.pack(side="left", padx=10)

user_score = ctk.CTkLabel(time_and_score_frame, text=f"Score: 0")
user_score.pack(side="right", padx=10)

ctk.CTkLabel(
    app_frame,
    text="Instruction: Enter the color of the text you see\nand not the text",
    font=("Montserrat", 18, "italic"),
    text_color="lightblue",
).pack(padx=10, pady=20)

changing_text = ctk.CTkLabel(app_frame, text="blue", font=("Montserrat", 30, "bold"))
changing_text.pack(pady=20, fill=ctk.X)

user_input = ctk.CTkEntry(app_frame, width=300, height=50)
user_input.pack()
user_input.bind("<Return>", start_game)

ctk.CTkLabel(
    app_frame, text="Press enter to start the game...", text_color="grey"
).pack()

reset_btn = ctk.CTkButton(app_frame, text="Reset Game", command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()
