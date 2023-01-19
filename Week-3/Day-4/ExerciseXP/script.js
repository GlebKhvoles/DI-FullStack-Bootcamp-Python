//Exercise1
let x = 5;
let y = 2;

if (x > y) {
    console.log(`x is the biggest number`);
}

//Exercise2
let newDog = "Chihuahua";

console.log(newDog.length);
newDog.toUpperCase();
newDog.toLowerCase();

if (newDog = "Chihuahua") {
    console.log("I love Chihuahuas, it's my favorite dog breed");
} else {console.log("I dont care, I prefer cats");
}

//Exercise3
let userStr = prompt("Enter the number");
let user = Number(userStr);

if (user % 2 == 0) {
    console.log("x is an even number");
} else {
    console.log("x is an odd number");
}

//Exercise4
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let usersConnected = users.length;

 switch(usersConnected){
case 0:     
    console.log("no one is online");
    break;
case 1:
    console.log(users[0], "is online");
    break;
case 2:     
console.log(users[0], users[1], "are online");
    break;

default:    
 console.log(`${users[0]}, ${users[1]}, and, ${usersConnected-2} are online`);
}
