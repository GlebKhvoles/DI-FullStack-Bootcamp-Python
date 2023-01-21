//Stars
let star = ""

for ( let x = 0; x < 6; x++); {
    star += '*';
console.log (star);
}

for (let x = 0; x < 6; x++) {  
    star = '';
    for (let i = 0; i <= x; i++) {
        star += '* ';       
    }
    console.log(star)
}