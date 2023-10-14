#  To make this project to run well in every system it is applied to , please do the following:
#    If you dont have any python interpreter , kindly download python 3.11.5 from python.org website
#      If you see some errors in the import , just go to terminal and go to the correct directory and justdo "pip install <module-name>" for each modules.
#        Here the module-name's are:
#          1) "os" (Actually pre-installed , so wont be needed to be installed again )
#          2) (Highly Recommended) "openai" (might not be preinstalled)
#          3) (Another important point) "customtkinter" (not just tkinter)(might not be preinstalled)
#
#
# I found out one thing that many can't get API keys or the FREE trial for the API key would have run out.
# SO please make sure to find necessary means , such as creating a new API key from another account which has logged on to openai/personal
# Only old users who have logged into openai.com like a long time ago , or had early access can get an API Key free trial for upto $5.
# You can find other means of using AI , by connecting this directly to ChatGPT or other AI sources.
#                     THANK YOU
#
import os
import openai
import customtkinter as ctk



def generate():
    prompt = "Please generate 10 ideas for coding projects. "
    language = language_dropdown.get()
    prompt += "the programming language is " + language + ". "
    domain= domain_dropdown.get()
    prompt += "the programming domain is " + domain + ". "
    prompt += "Suggest me a different domain or language if the provided is not working together properly."
    level = level_Value.get()
    prompt += "level is " + level + ". "

    if database_Checkbox.get():
        prompt += " The project should include a database."

    if api_Checkbox.get():
        prompt += "The project should include an API."

    if security_Checkbox.get():
        prompt += " The project should include security based features."

    if game_Checkbox.get():
        prompt += " The project should include games with responsive features and a really cool design with example."

    if user_c_Checkbox.get():
        prompt += " The project must be user customizable and really easy for customers or clients to understand."

    if friendly_Checkbox.get():
        prompt += " The project should be really understandable for everyone and explain the project with a lot of hinted words, services and guides as sources."

    if entry_box.get():
        entry = entry_box.get()
        prompt += " The project should include" + entry + "."

#  Here the code might not run and show some errors , so please do the following necessary
#    Go to the openai and create your own APIKEY, install it and and copy that key  
#      Go to the Settings(System Settings)-->System-->About-->Advanced system settings(in the right side)-->Advanced
#                                                                                                              |
#                                                                                                             \|/
# Paste the key value in variable value<--New<--In the User or system variables or system variables<--Environmental Variables
#        Give it a variable name like "OPENAI_API_KEY"
#        If you want to give it a different name , then , also change the name in the os.getenv('the_name_you_gave')

    openai.api_key = os.getenv('OPENAI_API_KEY')

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    answer = completion.choices[0].message.content
    result.delete(0.0, ctk.END)  #Clears the previous result
    result.insert(ctk.END, answer)


#Please change the color to your liking , if you feel that the color is making you uncomfortable in the color and its attributed form options

root = ctk.CTk()
root.geometry("900x900")
root.title("Project Idea Generator Using AI - Simplified Version")

title_label = ctk.CTkLabel(root, text="Project Idea Generator", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(4, 2))

frame = ctk.CTkFrame(root, fg_color="dark green")
frame.pack(fill="x",padx=10)

top_frame = ctk.CTkScrollableFrame(frame, fg_color="light grey", height=200)
top_frame.pack(fill="x", padx=10, pady=10)

language_frame = ctk.CTkFrame(top_frame)
language_frame.pack(padx=10, pady=10, fill="both")

language_label = ctk.CTkLabel(language_frame, text="Programming Language")
language_label.pack()

language_dropdown = ctk.CTkComboBox(language_frame,width=300,
                                    values=["Python", "Java", "C++", "Javascript and it's Branches", 
                                            "Any different programming language for domain provided"])
language_dropdown.pack(pady=5)

domain_frame = ctk.CTkFrame(top_frame)
domain_frame.pack(padx=10, fill="both")

domain_label = ctk.CTkLabel(domain_frame, text="Domain")
domain_label.pack()

domain_dropdown = ctk.CTkComboBox(domain_frame,width=300,
                                    values=["Artificial intelligence", "Web Technology", "Data Science And Analysis",
                                            "Cyber Security", "Iot", "Frontend", "Backend", "Cloud Computing", "Web Development", 
                                            "Software And Web Testing", "Any different domain for programming language provided"])
domain_dropdown.pack(pady=5)

level_frame = ctk.CTkFrame(top_frame)
level_frame.pack(padx=10, pady=10, fill="both")

level_label = ctk.CTkLabel(level_frame, text="Project difficulty", font=ctk.CTkFont(weight="bold"))
level_label.pack()

level_Value = ctk.StringVar(value="Beginner")
beginner_radiobutton = ctk.CTkRadioButton(level_frame, text="Beginner", variable=level_Value, value="Beginner")
beginner_radiobutton.pack(side="left", padx=(20, 10), pady=5)

intermediate_radiobutton = ctk.CTkRadioButton(level_frame, text="Intermediate", variable=level_Value,
                                              value="Intermediate")
intermediate_radiobutton.pack(side="left", padx=(20, 10), pady=5)

advanced_radiobutton = ctk.CTkRadioButton(level_frame, text="Advanced", variable=level_Value, value="Advanced")
advanced_radiobutton.pack(side="left", padx=(20, 10), pady=5)

expert_radiobutton = ctk.CTkRadioButton(level_frame, text="Expert", variable=level_Value, value="Expert")
expert_radiobutton.pack(side="left", padx=(20, 10), pady=5)

feature_frame = ctk.CTkFrame(top_frame)
feature_frame.pack(padx=10, fill="both")

feature_label = ctk.CTkLabel(feature_frame, text="Features", font=ctk.CTkFont(weight="bold"))
feature_label.pack()

database_Checkbox = ctk.CTkCheckBox(feature_frame, text="Database")
database_Checkbox.pack(side="left", padx=10, pady=5)

api_Checkbox = ctk.CTkCheckBox(feature_frame, text="API")
api_Checkbox.pack(side="left", padx=10, pady=5)

security_Checkbox = ctk.CTkCheckBox(feature_frame, text="Security")
security_Checkbox.pack(side="left", padx=10, pady=5)

game_Checkbox = ctk.CTkCheckBox(feature_frame, text="Game Based")
game_Checkbox.pack(side="left", padx=10, pady=5)

user_c_Checkbox = ctk.CTkCheckBox(feature_frame, text="User Customizable")
user_c_Checkbox.pack(side="left", padx=10, pady=5)

friendly_Checkbox = ctk.CTkCheckBox(feature_frame, text="Beginner and Challenger Friendly")
friendly_Checkbox.pack(side="left", padx=10, pady=5)

custom_frame = ctk.CTkFrame(top_frame)
custom_frame.pack(padx=10, pady=10, fill="both")

custom_label = ctk.CTkLabel(custom_frame, text="Custom input", font=ctk.CTkFont(weight="bold"))
custom_label.pack()

entry_box = ctk.CTkEntry(custom_frame, width=500)
entry_box.pack(padx=10, pady=10)

mid_frame = ctk.CTkFrame(root, fg_color="dark green")
mid_frame.pack(fill="x",padx=10, pady=10)

button = ctk.CTkButton(mid_frame, text="Generate The Ideas", command=generate, text_color="black", fg_color="white")
button.pack(padx=190, fill="x", pady=10)

bottom_frame = ctk.CTkFrame(root, fg_color="dark blue")
bottom_frame.pack(padx=10, fill="x")

result_frame = ctk.CTkFrame(bottom_frame, fg_color="light blue")
result_frame.pack(pady=10, fill="x", padx=10)

result_label = ctk.CTkLabel(result_frame, text="The Ideas Generated Are", font=ctk.CTkFont(weight="bold"),
                            text_color='black')
result_label.pack(fill="x", padx=10)

result = ctk.CTkTextbox(result_frame, font=ctk.CTkFont(size=15), height=300)
result.pack(fill="x", padx=10, pady=10)

root.mainloop()
