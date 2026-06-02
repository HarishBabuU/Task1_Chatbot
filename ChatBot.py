import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()

root.title("Future Study & Career Assistant")

root.geometry("600x700")

root.config(bg="#0f172a")

def get_reply(user_message):

    user_message = user_message.lower()

    if "hello" in user_message or "hi" in user_message:

        return (
            "Hello. I can help you with higher studies, "
            "career guidance, AI domains, certifications, "
            "and resume building."
        )

    elif "study abroad" in user_message or "ms" in user_message:

        return (
            "Studying abroad is a great option for global exposure. "
            "Popular destinations include USA, Canada, Germany, "
            "and the UK. Exams like IELTS, TOEFL, and GRE may "
            "be required depending on the university."
        )

    elif "mtech" in user_message or "gate" in user_message:

        return (
            "M.Tech is a good choice for technical specialization. "
            "Preparing for GATE can help you get admission into "
            "top institutes like IITs and NITs."
        )

    elif "ai" in user_message or "artificial intelligence" in user_message:

        return (
            "Artificial Intelligence is one of the fastest-growing fields. "
            "You can learn Python, Machine Learning, Deep Learning, "
            "and frameworks like TensorFlow and PyTorch."
        )

    elif "data science" in user_message:

        return (
            "Data Science involves data analysis, visualization, "
            "machine learning, and statistics. "
            "Python, SQL, and Pandas are important skills."
        )

    elif "cyber security" in user_message:

        return (
            "Cyber Security focuses on protecting systems and networks. "
            "Learning Linux, networking, and ethical hacking "
            "can help build a strong career in this field."
        )

    elif "web development" in user_message:

        return (
            "Web Development includes frontend and backend technologies. "
            "You can start with HTML, CSS, JavaScript, and later "
            "learn React and backend frameworks."
        )

    elif "certificate" in user_message or "certification" in user_message:

        return (
            "Popular certifications include Google Data Analytics, "
            "AWS Cloud Certifications, Microsoft Azure, "
            "and Coursera professional certificates."
        )

    elif "resume" in user_message:

        return (
            "A strong resume should include projects, internships, "
            "technical skills, certifications, and GitHub links."
        )

    elif "github" in user_message:

        return (
            "Maintain clean GitHub repositories with proper README files, "
            "project descriptions, and organized code."
        )

    elif "internship" in user_message:

        return (
            "Internships help improve practical knowledge and strengthen "
            "your resume. Building unique projects is very important."
        )

    elif "motivate" in user_message or "motivation" in user_message:

        return (
            "Stay consistent and continue learning. "
            "Small improvements every day lead to long-term success."
        )

    elif "bye" in user_message:

        return "Goodbye. Wishing you success in your career journey."

    else:

        return (
            "I can help with higher studies, career guidance, "
            "AI domains, certifications, internships, and resume tips."
        )

def send_message():

    message = user_input.get().strip()

    if message == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(
        tk.END,
        f"\nYou: {message}\n"
    )

    reply = get_reply(message)

    chat_area.insert(
        tk.END,
        f"Bot: {reply}\n"
    )

    chat_area.config(state=tk.DISABLED)

    chat_area.yview(tk.END)

    user_input.delete(0, tk.END)

title = tk.Label(

    root,

    text="Future Study & Career Assistant",

    font=("Arial", 22, "bold"),

    bg="#0f172a",

    fg="white"
)

title.pack(pady=20)

chat_area = scrolledtext.ScrolledText(

    root,

    wrap=tk.WORD,

    font=("Arial", 12),

    bg="#1e293b",

    fg="white",

    insertbackground="white",

    relief="flat"
)

chat_area.pack(

    padx=20,

    pady=10,

    fill=tk.BOTH,

    expand=True
)

chat_area.insert(

    tk.END,

    "Bot: Hello. Ask me anything about higher studies, careers, AI, certifications, or internships.\n"
)

chat_area.config(state=tk.DISABLED)

input_frame = tk.Frame(

    root,

    bg="#0f172a"
)

input_frame.pack(

    fill=tk.X,

    padx=20,

    pady=20
)

user_input = tk.Entry(

    input_frame,

    font=("Arial", 13),

    bg="#1e293b",

    fg="white",

    insertbackground="white",

    relief="flat"
)

user_input.pack(

    side=tk.LEFT,

    fill=tk.X,

    expand=True,

    ipady=12,

    padx=(0,10)
)

send_button = tk.Button(

    input_frame,

    text="Send",

    font=("Arial", 12, "bold"),

    bg="#2563eb",

    fg="white",

    relief="flat",

    padx=20,

    pady=10,

    cursor="hand2",

    command=send_message
)

send_button.pack(side=tk.RIGHT)

root.bind(

    "<Return>",

    lambda event: send_message()
)

root.mainloop()