// Вариант 24 Составить программу вычисления функции: Y = x^2 + 2x + 3
function calculateY(x) {
    return Math.pow(x, 2) + (2 * x) + 3;
}

// Пример
var x = 5; // Задайте значение переменной x, для которого нужно вычислить Y
var result = calculateY(x);
console.log("Результат вычисления функции Y: " + result);
