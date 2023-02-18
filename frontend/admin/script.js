let sharks = document.querySelectorAll('.shark');
let sharkHolder = document.querySelector('#sharkHolder').getBoundingClientRect();
let center = [sharkHolder.width / 2, sharkHolder.height / 2];
let angleIncrement = Math.PI * 2 / sharks.length;
let distance = 300;

for (let i = 0; i < sharks.length; i++) {
    let offset = [Math.sin(angleIncrement * i) * distance, Math.cos(angleIncrement * i) * distance];
    sharks[i].style.left = center[0] + offset[0] + 'px';
    sharks[i].style.top = center[1] - offset[1] + 'px';
}