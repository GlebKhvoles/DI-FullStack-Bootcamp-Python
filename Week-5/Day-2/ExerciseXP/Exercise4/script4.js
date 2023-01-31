let form = document.querySelector('form');

form.addEventListener('submit', submitForm);

function submitForm(e) {
    let radius = Number(form.elements.radius.value);
    form.elements.volume.value = 4/3 * 3.14 * radius**3;    
    e.preventDefault();
}