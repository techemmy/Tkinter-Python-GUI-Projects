import customtkinter as ctk
from deep_translator import GoogleTranslator


def translate_language():
    text_to_trans = user_text.get()
    lang = lang_to_var.get()

    output = GoogleTranslator(source="auto", target=lang).translate(text_to_trans)

    translated_text.configure(state="normal")
    translated_text.delete(0, "end")
    translated_text.insert(0, output)


root = ctk.CTk()
root.title("Language Translator")
root.minsize(400, 400)

ctk.CTkLabel(root, text="Language Translator", font=("Arial", 30)).pack(
    anchor=ctk.CENTER
)

app_frame = ctk.CTkFrame(root, width=500, height=500, fg_color="transparent")
app_frame.pack(fill=ctk.X, padx=20, pady=10)

ctk.CTkLabel(app_frame, text="Enter text to translate here 🔥").pack(
    expand=True, fill=ctk.X
)
user_text = ctk.CTkEntry(app_frame, height=50)
user_text.pack(fill=ctk.X)

ctk.CTkLabel(app_frame, text="Choose language to translate to: 📝").pack()
lang_to_var = ctk.StringVar(value="english")
langs_list = GoogleTranslator().get_supported_languages()
lang_to = ctk.CTkOptionMenu(app_frame, values=langs_list, variable=lang_to_var)
lang_to.set("english")
lang_to.pack(fill=ctk.X, ipady=5)

ctk.CTkLabel(app_frame, text="Translated text 👇").pack()
translated_text = ctk.CTkEntry(
    app_frame,
    height=100,
    placeholder_text="Translated text will show here.",
    placeholder_text_color="grey",
    state=ctk.DISABLED,
)
translated_text.pack(fill=ctk.X)

translate_btn = ctk.CTkButton(app_frame, text="Translate", command=translate_language)
translate_btn.pack(fill=ctk.X, pady=20)

root.mainloop()
