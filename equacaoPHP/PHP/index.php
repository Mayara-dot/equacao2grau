<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>XPEPE</title>
</head>
<body>
<p>Escreva os coeficientes da equação de segundo grau</p>
    <form method="POST">
        <div class="row">
            <label for="a">a</label>
            <input type="number" name="a" id="a" required>
        </div>

        <div class="row">
            <label for="b">b</label>
            <input type="number" name="b" id="b" required>
        </div>

        <div class="row">
            <label for="c">c</label>
            <input type="number" name="c" id="c" required>
        </div>
        <button>Calcular</button>
    </form>
    <?php
    require_once('calcular.php');?>
</body>
</html>