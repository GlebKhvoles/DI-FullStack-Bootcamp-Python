const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift()
console.log('Exercise 1 part 1',fruits);

fruits.sort();
console.log('Exercise 1 part 2', fruits);

fruits.push("Kiwi");
console.log('Exercise 1 part 3', fruits);

fruits.splice(0,1);
console.log('Exercise 1 part 4', fruits);

fruits.reverse();
console.log('Exercise 1 part 5', fruits);

const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let Oranges = moreFruits [1] [1];
console.log('Exercise 2',Oranges);