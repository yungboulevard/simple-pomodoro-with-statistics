const input = document.getElementById('input');
const blockTime = document.querySelector('.time');
let interval;
const xhr = new XMLHttpRequest();

blockTime.innerHTML = 'Стандартный помидор - 25 минут или же 1500 секунд, немного, правда? Вы можете указать кастомное значение.';
input.value = 1500;
saved_time = 0;

document.getElementById('start').addEventListener('click', () => {
    if (input.value < 0){
        input.value = 0;
        blockTime.innerHTML = 0;
    }
    blockTime.innerHTML = input.value;

    clearInterval(interval);
    interval = setInterval(substractTime, 1000);
});

document.getElementById('stop').addEventListener('click', () => {
    clearInterval(interval);
    saved_time = 0;
    blockTime.innerHTML = 'Таймер остановлен, промежуточный результат сохранён.';
});

document.getElementById('reset').addEventListener('click', () => {
    input.value = 0;
    saved_time = 0;
    blockTime.innerHTML = 'Таймер сброшен, результат сохранён.';
});


function substractTime() {
    if (blockTime.innerHTML > 0) {
        blockTime.innerHTML--;
        input.value--;
        saved_time++;
        if (input.value < 0 || blockTime.innerHTML == 0){
            input.value = 0;
            blockTime.innerHTML = 0;
        }
    } else {
        clearInterval(interval);
    }
}
