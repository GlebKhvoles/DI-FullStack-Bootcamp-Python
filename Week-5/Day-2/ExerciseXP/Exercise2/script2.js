let form = document.querySelector('form');
console.log(form);

let fname = document.getElementById('fname');
console.log(fname);
let lname = document.getElementById('lname');
console.log(lname);
let submit = document.getElementById('submit');
console.log(submit);

let fname2 = document.getElementsByName('fname');
console.log(fname2);
let lname2 = document.getElementsByName('lname');
console.log(lname2);

form.addEventListener('submit', submitForm);
function submitForm(e) {
    if (fname.value == '' || lname.value == '') {
        return;
}
let ul = document.querySelector('ul');
let liFname = document.createElement('li');
let liLname = document.createElement('li');
liFname.innerHTML = fname.value;
liLname.innerHTML = lname.value;
ul.appendChild(liFname);
ul.appendChild(liLname);
e.preventDefault()
}