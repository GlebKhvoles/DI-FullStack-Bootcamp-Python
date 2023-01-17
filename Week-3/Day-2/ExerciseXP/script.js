//Part1
//Exercise1

let favoriteFood = "chicken";
let favoriteMeal = "dinner";
console.log(`I eat ${favoriteFood} at every ${favoriteMeal}`);

//Exercise2

const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLenght = myWatchedSeries.length;
let myWatchedSeriesSentence = myWatchedSeries.toString();
console.log('I watched' ,myWatchedSeriesLenght, 'series:' ,myWatchedSeriesSentence);

//Part2

let movie = 'the bing bang theory';
let series = myWatchedSeries.indexOf(movie);
console.log(series);
let myWatchedSeries[series] = 'Freinds';
console.log(series);
myWatchedSeries.push('BMS');
myWatchedSeries.unshift('Sherlok');
myWatchedSeries.splice(1,1);
let moneyHeist = myWatchedSeries.indexof('money heist');
console.log(myWatchedSeries[moneyHeist][2]);
console.log(myWatchedSeries);

//Exercise3

let celsius = prompt('what temperature you want to calculate');
let fahrenheit = (celsius / 5 * 9) + 32;
console.log(`${celsius}°C is ${fahrenheit}°F`);

//Exercise4

let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction:It will output 55, because 34 and 21 are numbers
// Actual:55

a = 2;

console.log(a+b) //second expression
// Prediction:It will output 55, because 2 and 23 are numbers
// Actual:23

//What is the value of c?
//undefined

console.log(3 + 4 + '5') //third expression
// Prediction:7'5'
// Actual:'75'

//Exercise5

typeof(15)
// Prediction:number
// Actual:number

typeof(5.5)
// Prediction:number
// Actual:number

typeof(NaN)
// Prediction:undefined
// Actual:number

typeof("hello")
// Prediction:string
// Actual:string

typeof(true)
// Prediction:function
// Actual:boolean

typeof(1 != 2)
// Prediction:boolean
// Actual:boolean

"hamburger" + "s"
// Prediction:"hamburgers"
// Actual:"hamburgers"

"hamburgers" - "s"
// Prediction:NaN
// Actual:"hamburgers" - "s"

"1" + "3"
// Prediction:'13'
// Actual:'13'

"1" - "3"
// Prediction:NaN
// Actual:-2

"johnny" + 5
// Prediction:'johny5'
// Actual:'johny5'

"johnny" - 5
// Prediction:NaN
// Actual:NaN

99 * "hello"
// Prediction:'hello,hello,hello,hello,hello,hello...'
// Actual:NaN

1 != 1
// Prediction:false
// Actual:false

1 == "1"
// Prediction:true
// Actual:true

1 === "1"
// Prediction:false
// Actual:false


//Exercise6

5 + "34"
// Prediction:'534'
// Actual:'534'

5 - "4"
// Prediction:NaN
// Actual:1

10 % 5
// Prediction:0.5
// Actual:0

5 % 10
// Prediction:0.5
// Actual:5

"Java" + "Script"
// Prediction:'JavaScript'
// Actual:'JavaScript'

" " + " "
// Prediction:'  '
// Actual:'  '

" " + 0
// Prediction:'0'
// Actual:' 0'

true + true
// Prediction:undefinde
// Actual:2

true + false
// Prediction:1
// Actual:1

false + true
// Prediction:1
// Actual:1

false - true
// Prediction:0
// Actual:-1

!true
// Prediction:false
// Actual:false

3 - 4
// Prediction:-1
// Actual:-1

"Bob" - "bill"
// Prediction:NaN
// Actual:NaN