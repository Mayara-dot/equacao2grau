<?php
if($_SERVER['REQUEST_METHOD'] == 'POST') {
    $a = $_POST['a'];
    $b = isset($_POST['b']) ? $_POST['b'] : 0;
    $c = isset($_POST['c']) ? $_POST['c'] : 0;
    $coeficientes = "<p>Os coeficientes foram: a = {$a}, b = {$b}, c = {$c}.</p>";
    $error = "<p>Não foi possível calcular.</p>";

    if($a != 0 && $b != 0 && $c != 0) {
        $delta = pow($b, 2) - 4 * $a * $c;
        $resultPositive = ((-$b) + sqrt($delta)) / 2 * $a;
        $resultNegative = ((-$b) - sqrt($delta)) / 2 * $a;
        echo $coeficientes;
        echo "<p>Duas raízes {$resultPositive} e {$resultNegative}.<p>";
    } else if($b == 0 && $a != 0) {
        $resultNegative = (-(sqrt((-$c) / $a)));
        $resultPositive = (+(sqrt((-$c) / $a)));
        echo $coeficientes;
        echo "<p>Duas raízes {$resultPositive} e {$resultNegative}.<p>";
    } else if($c == 0 && $a != 0) {
        $result = - ($b) / $a;
        echo $coeficientes;
        echo "<p>Uma raíz é 0 e outra {$result}.<p>";
    } else {
        echo $coeficientes;
        echo $error;
    }
} else {
    echo $error;
}
