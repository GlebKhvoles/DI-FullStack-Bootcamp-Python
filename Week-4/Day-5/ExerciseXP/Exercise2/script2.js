let divElem = document.querySelector('div');
divElem.style.backgroundColor = 'lightblue';
divElem.style.padding = '5px';

let ul = document.querySelector('ul');
let john = document.querySelector('li');
ul.removeChild(john);

let pete = ul.lastElementChild;
pete.setAttribute('style', 'border: solid 2px;');

let body= document.querySelector('body');
body.setAttribute('style', 'font-size: 30px;');

if (divElem.style.backgroundColor = 'ligtblue') {
    alert(`Hello ${john} and ${pete} !`);
}