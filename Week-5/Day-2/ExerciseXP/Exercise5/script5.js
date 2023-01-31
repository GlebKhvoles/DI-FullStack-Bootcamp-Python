let divElem = document.querySelector('div');

divElem.addEventListener('click', clickDivElem);
divElem.addEventListener('mouseover', hover);
divElem.addEventListener('mouseout', passDiv);
divElem.addEventListener('dblclick', dblclickrDivElem);

function hover() {
    divElem.style.backgroundColor = 'lightgreen';
}

function passDiv() {
    divElem.style.backgroundColor = 'aqua';
}

function clickDivElem() {
    divElem.style.width = '400px';   
    divElem.style.height = '50px';
    divElem.style.fontWeight = 'bold';
}

function dblclickrDivElem() {
    divElem.style.width = '300px';   
    divElem.style.height = '35px';
    divElem.style.fontWeight = 'lighter';
}