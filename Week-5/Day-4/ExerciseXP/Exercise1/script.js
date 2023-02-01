//Part1
let clearElem = document.getElementById('clear');

function helloWorld() {
    alert("Hello World");
}
setTimeout(helloWorld, 2000);

//Part2
function helloWorld2() {
    let p = document.createElement('p');
    let int = document.getElementById('container');
    int.appendChild(p);
    let pText = document.createTextNode('Hello World');
    p.appendChild(pText);
}
setTimeout(helloWorld2, 2000);

//Part3
let hwInterval = setInterval(helloWorld3, 2000);
function helloWorld3() {
    let p = document.createElement('p');
    let int = document.getElementById('container');
    int.appendChild(p);
    let pText = document.createTextNode('Hello World');
    p.appendChild(pText);
    if (int.getElementsByTagName('p').length == 5) {
        clearInterval(hwInterval);
    }
}


clearElem.addEventListener('click', clearelem)
function clearelem() {
    clearInterval(hwInterval);
    clearElem.style.backgroundColor = 'red';
};


