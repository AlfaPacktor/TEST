from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>Поздравительная игра</title>

<link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">

<style>

body{
    font-family: 'Lobster', cursive;
    text-align:center;
    background: linear-gradient(135deg,#ffb3ba,#ffdfba,#ffffba,#baffc9,#bae1ff);
    background-size: cover;
}

.container{
    width:600px;
    margin:auto;
}

.block{
    margin:25px;
    padding:20px;
    background:white;
    border-radius:15px;
    box-shadow:0 0 10px rgba(0,0,0,0.2);
}

.hidden{
    display:none;
}

input{
    padding:10px;
    border:2px solid red;
    border-radius:8px;
    font-size:16px;
}

button{
    padding:10px 20px;
    margin-left:10px;
    border:none;
    border-radius:8px;
    cursor:pointer;
    font-size:16px;
}

.text{
    margin-top:15px;
    color:#cd7f32;
    font-size:20px;
}

h1{
    color:#cd7f32;
}

#final{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.7);
    display:none;
    align-items:center;
    justify-content:center;
}

#final div{
    background:white;
    padding:40px;
    border-radius:15px;
    font-size:28px;
    color:#cd7f32;
}

</style>

<script>

function checkPassword(blockNumber){

    let input = document.getElementById("input"+blockNumber).value;

    if(input == blockNumber){

        document.getElementById("text"+blockNumber).style.display="block";

        if(blockNumber < 7){
            document.getElementById("block"+(blockNumber+1)).style.display="block";
        } else{
            document.getElementById("final").style.display="flex";
        }

    }else{
        alert("Неверный пароль!");
    }
}

</script>

</head>

<body>

<h1>Добро пожаловать в игру</h1>

<div class="container">

{% for i in range(1,8) %}

<div class="block" id="block{{i}}" {% if i>1 %}style="display:none"{% endif %}>

<p>Это твой вопрос и ты должна на него ответить</p>

<input id="input{{i}}" type="password" placeholder="Введите пароль">

<button onclick="checkPassword({{i}})">Вперед</button>

<div class="text hidden" id="text{{i}}">
Правильно! Переходим дальше 🎉
</div>

</div>

{% endfor %}

</div>

<div id="final">
<div>
🎉 Поздравляю! Ты прошла весь квест! 🎉
</div>
</div>

</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

if name == "__main__":
    app.run(debug=True)
