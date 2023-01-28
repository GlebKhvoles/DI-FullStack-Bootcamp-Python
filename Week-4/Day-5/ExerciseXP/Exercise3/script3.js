let divElem = document.getElementById('navBar');
divElem.setAttribute('id', 'socialNetworkNavigation;');

let ulElem = document.querySelector('ul');
let newLi = document.createElement('li');
let aElem = document.createElement('a');

aElem.innerHTML = 'Logout';
aElem.setAttribute('href', '#');

newLi.appendChild(aElem);
ulElem.appendChild(newLi);

console.log(ulElem.firstElementChild.textContent);
console.log(ulElem.lastElementChild.textContent);