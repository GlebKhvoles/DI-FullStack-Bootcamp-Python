let str = document.querySelector("#container");
console.log(str);

let  ul1 = str.nextElementSibling;
let pete = ul1.lastElementChild.textContent = 'Richard';

let uls = document.getElementsByClassName('list');

uls[0].firstElementChild.textContent = 'Gleb';
uls[1].firstElementChild.textContent = 'Gleb';

let li1 = uls[1].firstElementChild;
let li2 = li1.nextElementSibling;
uls[1].removeChild(li2);

uls[0].classList.add('student_list', 'university', 'attendance');
console.log(uls[0]);
uls[1].classList.add('student_list');
console.log(uls[1]);