//Exercise1
const people = ["Greg", "Mary", "Devon", "James"];
people.shift();

people.splice(2, 1, 'Jason');

people.push('Gleb');

console.log(people.indexOf('Mary'));

let copy = people.slice(0,3);

console.log(copy.indexOf("Foo")); //Answer - false

let last = copy[copy.length -1];

//Part2

for (let x = 0; x < people.length; x++) {
    console.log(people[x])
}

for (let x = 0; x < people.length; x++) {
    console.log(people[x])
    if (people[x] == "Jason") {
        break;
    }
}

//Exercise2
const colors = ["Blue", "Red", "Black", "Grey", "Orange"];
let suffix = ["st", "nd", "rd", "th", "th"];
for (let x=0; x<colors.length; x++) {
    console.log(`My ${x + 1}${suffix[x]} choice is ${colors[x]}`);
}

//Exercise3
//let number = prompt("Write the number");
//typeof(number); //string
//while (number < 10) {
   // number = prompt("Write a different number");
//}

//Exercise4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    }
}

console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor + " and " + building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants[0] + " has " + building.numberOfRoomsAndRent.sarah[0] + " rooms");

if (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david > building.numberOfRoomsAndRent.dan) {
    building.numberOfRoomsAndRent.dan = 1200;
}

//Exercise5
let family = {
    age: {sarah: [40], dan: [42], david: [7]}
}

for (let x in family) {
    console.log(x)
} 

for (let x in family) {
    console.log(family[x]);
} 

//Exercise6
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }

  let str = " "

  for (let x in details) {
    str += x + " " + details[x] + " ";
  }

  console.log(str);

  //Exercise7
  const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

  let letters  = [];

  names.forEach(element => {
    letters.push(element.substring(0,1));       
});

letters.sort();
console.log(letters.join(""));
