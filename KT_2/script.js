// Вариант 26: Составить программу вычисления функции: y=x^2 -1,еслиX≤-6,  y= 8+x,еслиX >-6
function calculateY(x) {
    if (x <= -6) {
        return Math.pow(x, 2) - 1;
    } else {
        return 8 + x;
    }
}

// Пример использования функции
var x = -8; // Задайте значение переменной x, для которого нужно вычислить Y
var result = calculateY(x);
console.log("Результат вычисления функции Y: " + result);