let arr = [
    {
        title: '"The Night in Lisbon"',
        author: 'Erich Maria Remarque',
        image : 'https://www.lbi.org/media/images/19_Night-in-Lisbon-01.height-1030.png',
        alreadyRead : true
    },
    {        
        title: '"All Quiet on the Western Front"',
        author: 'Erich Maria Remarque',
        image : 'https://www.littlebrown.com/wp-content/uploads/2017/06/9780316739924.jpg?fit=1712%2C2600',
        alreadyRead : false
    }
]

let divElem = document.querySelector('.listBooks');
let tableElem = document.createElement('table');
divElem.appendChild(tableElem);
console.log(divElem);

for (const book of arr) {
    let tr = document.createElement('tr');
    let td = document.createElement('td');
    let tdImage = document.createElement('td');
    tableElem.appendChild(tr);
    tr.appendChild(td);
    tr.appendChild(tdImage);
    let image = document.createElement('img');
    td.innerHTML = book.title + ' written by ' + book.author;
    image.setAttribute('src', book.image);
    image.style.width = '100px';
    td.style.border = 'solid black 2px';
    tdImage.style.border = 'solid black 1px';
    if (book.alreadyRead) {
        tr.style.backgroundColor = 'red';
    }
    tdImage.appendChild(image);


}