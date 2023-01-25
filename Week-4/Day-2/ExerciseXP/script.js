//Exercise1
 function infoAboutMe(myName, myAge, myHobbies) {
    console.log('My name is ' + myName + ', my age is ' + myAge + ', and my hobbies are ' + myHobbies);
 }
 
 infoAboutMe('Gleb', 27, 'icehockey, reading and traveling');

 function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log('You name is', personName, 'you are', personAge, 'years old', 'your favorite color is', personFavoriteColor);
 }
 
 infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

//Exercise2
// function calculateTip() {
   // let bill = Number(prompt('Enter amount of bill'));
   // if (bill < 50) {
      //   tips = 20;    
     // } else if (bill <= 200) {
      // tips = 15;   
     // } else if (bill > 200) {
      //   tips = 10;   
      // }
      // console.log(`bill - ${bill}; tips - ${bill * (tips / 100)}; final bill - ${bill + (bill * (tips / 100))}`);
  // }

//calculateTip();

//Esercise3
function isDivisible() {
    let summ = 0;
    let str = '';

    for (let i = 0; i <= 500; i++) {
        if (i % 23 == 0) {
            summ += i;  
            str += i + ' ';  
        }     
    }
   console.log('Outcome: ' + str);
   console.log('Summ: ' + summ);
   }
isDivisible();

function isDivisible(divisor = 23) {
   let summ = 0;
   let str = '';
  
   for (let i = 0; i <= 500; i++) {
       if (i % divisor == 0) {
           summ += i;    
           str += i + ' ';
       }     
      }
   console.log('Outcome: ' + str);
   console.log('Summ: ' + summ);
   }
isDivisible(33);

//Exercise4
const stock = { 
   "banana": 6, 
   "apple": 0,
   "pear": 12,
   "orange": 32,
   "blueberry":1
}  

const prices = {    
   "banana": 4, 
   "apple": 2, 
   "pear": 1,
   "orange": 1.5,
   "blueberry":10
} 

let shoppingList = ['banana', 'orange', 'apple'];

function myBill() {
   let summ = 0;
   for (let i of shoppingList) {
   if (i in stock && stock[i] > 0) {
        summ += prices[i];
        console.log(`${i} stock before ${stock[i]}`);
		  stock[i] -= 1;
		  console.log(`${i} stock now ${stock[i]}`);
      }
   }
   return summ;
} 
let total = myBill()
console.log('Total pices is ', total);

//Exercise 5
let order = [0.25, 0.1, 0.05, 0.01];

function changeEnough(itemPrice, amountOfChange) {
   let summ = 0;
   for (const i in amountOfChange) {
      summ += amountOfChange[i] * order[i];     
  }
  return summ >= itemPrice;
}
console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2,100,0,0]));

//Exercise6
function hotelCost() {
   let numberOfNights = 0;
   while (isNaN(numberOfNights) == true || numberOfNights == 0) {
      numberOfNights = Number(prompt("Number of nights"));
   }
   let nightPrice = numberOfNights * 140;
   return nightPrice;
}

function planeRideCost() {
   let destination = '';
   while (destination == '' || (isNaN(destination)) == false) {
      destination = prompt('Your destination');
   }
   if (destination == 'London') {
      return 183;
   } else if (destination == 'Paris') {
      return 220;
   } else {
      return 300;
   }
}

function rentalCarCost() {
   let numberOfDays = 0;
   while (isNaN(numberOfDays) == true || numberOfDays == 0) {
      numberOfDays = Number(prompt("Number of days"));
   }
   if (numberOfDays > 10) {
      return numberOfDays * 38;
   } else {
      return numberOfDays * 40;
   }
}

function totalVacationCost() {
   let totalCost = hotelCost() + planeRideCost() + rentalCarCost();
   return totalCost;
}


