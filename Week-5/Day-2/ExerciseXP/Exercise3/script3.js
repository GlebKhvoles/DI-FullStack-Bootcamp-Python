var allBoldItems = [];

let paragraph = document.querySelector('p');
paragraph.addEventListener('mouseover', mouseoverP);
paragraph.addEventListener('mouseout', mouseoutP);

function getBold_items() {
    allBoldItems = document.getElementsByTagName('strong');
}

function highlight() {
    getBold_items();
    for (item of allBoldItems) {
        item.style.color = 'blue';
    }
}

function return_normal() {
    getBold_items();
    for (item of allBoldItems) {
        item.style.color = 'black';
    }
}

function mouseoverP() {
    highlight();
}

function mouseoutP() {
    return_normal();
}
