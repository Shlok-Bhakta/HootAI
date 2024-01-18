from taipy.gui import Gui
from taipy.gui import Markdown
from taipy.gui import navigate
from taipy.gui import Html
import openai

questions = ["Whats the biggest planet in the solar system?", "When was the declaration of independence signed?", "What is the capital of Mexico?"]
ans = [["Jupiter", "Neptune", "Earth", "Mars"], ["1776", "1923", "1056", "1329"], ["Quebec", "Italy", "Texas", "Mexico City"]]
right_ans = [0, 0, 3]

answered = 0
question = questions[answered]
ans1, ans2, ans3, ans4 = ans[answered]
right_ans_index = right_ans[answered]
url_ans1 = "correct"
url_ans2 = "incorrect"
url_ans3 = "incorrect"
url_ans4 = "incorrect"

# Highlight the correct answer
highlight_styles = ['background-color: #e74c3c;', 'background-color: #3498db;', 'background-color: #2ecc71;', 'background-color: #f39c12;']
highlight_style = highlight_styles[right_ans_index]

student_md = Html(f"""
<!DOCTYPE html>
<html>

<head>
    <style>

        h1 {{ 
            color: white;
            text-align: center;
        }}

        .grid-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            grid-gap: 10px;
            padding: 10px;
            margin-top: 20%;
            grid-template-areas:
                "button1 button2"
                "button3 button4";
        }}
        .button{{
            padding: 10px;
            font-size: 16px;
        }}
        .grid-container > a {{
            {highlight_style}\
            color:black;
            text-align: center;
            padding: 60px 0;
            font-size: 30px;
            border-radius: 10px;
        }}

        .grid-container > a:hover {{
            background-color: #555;
            color: white;
            border: 2px solid white;
            border-radius: 10px;
        }}

        .item1 {{
            grid-row: 1 / 2;
        }}

        .item2 {{
            grid-row: 1 / 2;
            grid-column: 2 / 3;
        }}

        .item3 {{
            grid-row: 2 / 3;
        }}

        .item4 {{
            grid-row: 2 / 3;
            grid-column: 2 / 3;
        }}
    </style>
</head>

<body>
    <h1>{question}</h1>
    <div class="grid-container">
        <a href="{url_ans1}" class="item1 button">{ans1}</a>
        <a href="{url_ans2}" class="item2 button">{ans2}</a>
        <a href="{url_ans3}" class="item3 button">{ans3}</a>
        <a href="{url_ans4}" class="item4 button">{ans4}</a>
    </div>
</body>

</html>
""")

def aiBot(question, ans, status):
    messages = [
        {"role": "system", "content": "You are student helper who will be given a question, an answer, and wether the student was correct or not, your job is to explain to the student why they were wrong or right. The questions will in the format 'question: answer' your job is to check if the quesiton is right and wrong and say why"}
    ]

    print("Your new assistant is ready!")


    message = (f"{question}: {ans}: {status}")
    messages.append({"role": "user", "content": message})
    print(message)
    response = openai.ChatCompletion.create(

    model="gpt-3.5-turbo",
    messages=messages)
    reply = response["choices"][0]["message"]["content"]

    return reply


text2 = "this would be an ai response but we didnt want to leak the api key"# aiBot(question, "Neptune", "wrong");
incorrect_md = Html(f"""

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <title>My Page</title>
    <style>
        body {{
            padding-top: 5%;
        }}
        .anotherone{{
            display: flex;
            justify-content: center; /* aligns the item horizontally */
            align-items: center; /* aligns the item vertically */
        }}
        .checkmark {{
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background-color: white;
            box-shadow: 0 0 10px red;
            position: relative;
        }}
        .checkmark i {{
            color: red;
            font-size: 50px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }}
        .message {{
            color: white;
            text-align: center;
            font-size: 24px;
            margin-top: 20px;
        }}
        .chatbox {{
            border: 2px solid black;
            color: white;
            padding: 40px;
            margin-top: 20px;
            border-radius: 10px;
            width: 75%;
        }}
        .whiten{{
            color: white;
        }}
    </style>
</head>
<body>
    <div class="message" style="font-size: 50pt">+0</div>
    <div class="message" style="font-size: 70pt">Try Again</div>
    <div class="anotherone">
        <div class="checkmark">
            <i class="fa fa-times"></i>
        </div>
    </div>
    <div class="anotherone">
        <div class="chatbox">
            <h1>{text2}</h1>
        </div>
    </div>
</body>

</html>
""")

correct_md = Html(
f"""
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>
        body {{
            padding-top: 5%;
        }}
        .anotherone{{
            display: flex;
            justify-content: center; /* aligns the item horizontally */
            align-items: center; /* aligns the item vertically */
        }}
        .checkmark {{
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background-color: white;
            box-shadow: 0 0 10px #06cf49;
            position: relative;
        }}
        .checkmark i {{
            color: green;
            font-size: 50px;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }}
        .message {{
            color: white;
            text-align: center;
            font-size: 24px;
            margin-top: 20px;
        }}
        .chatbox {{
            border: 2px solid black;
            padding: 40px;
            margin-top: 20px;
            border-radius: 10px;
            width: 75%;
        }}
    </style>
</head>
<body>
    <div class="message" style="font-size: 50pt">+100</div>
    <div class="message" style="font-size: 70pt">Correct</div>
    <div class="anotherone">
        <div class="checkmark">
            <i class="fa fa-check"></i>
        </div>
    </div>
    <div class="anotherone">
        <div class="chatbox">
            <h1>{text2}</h1>
        </div>
    </div>
</body>
</html>


""")


pages = {
    "student": student_md,
    "incorrect": incorrect_md,
    "correct": correct_md,
}

def go_correct(state):
    navigate(state, "correct")
    
def go_incorrect(state):
    navigate(state, "incorrect")


gui = Gui(pages=pages)
gui.run()