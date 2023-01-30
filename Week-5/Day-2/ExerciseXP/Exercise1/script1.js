let h1 = document.querySelector('h1');
console.log(h1);

let lp = h1.parentElement.lastElementChild;
h1.parentElement.removeChild(lp);

let h2 = document.querySelector('h2');
h2.addEventListener('click', clickH2);
function clickH2() {
    this.style.backgroundColor = 'red'; 
}

let h3 = document.querySelector('h3');
h3.addEventListener('click', clickH3);
function clickH3() {
    this.style.display = 'none'; 
}

let button = document.createElement('button');
button.innerHTML = 'BOLD!';
h1.parentElement.appendChild(button);
button.addEventListener('click', clickbutton);

function clickbutton() {
    h1.parentElement.style.fontWeight = 'bold';    
}

h1.addEventListener('mouseover', overH1);
function overH1() {
    this.style.fontSize = `${Math.floor(Math.random() * 101)}px`;
}

let p = document.querySelector('p');
console.log(p);
p.addEventListener('mouseover', overP);
function overP() {
    this.style.opacity = 1;
    this.style.transition = `opacity 1000ms`;
    this.style.opacity = 0;
}