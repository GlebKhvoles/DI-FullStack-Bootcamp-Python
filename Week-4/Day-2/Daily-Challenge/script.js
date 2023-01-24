let userWord = "";

while ((userWord.indexOf(",")) == -1) {
    userWord = prompt("please write at least 5 words separate by a ,. i will display it as a message for you");
}

let arrayOfWords = userWord.split(",");

console.log(arrayOfWords)

 let longest = arrayOfWords.sort(
     function (a, b) {
        return b.length - a.length;
   }
)[0];
console.log(arrayOfWords);
console.log(longest);
let longest2 = '';

for(let char of arrayOfWords) {
    if(char.length > longest2.length) {
        longest2 = char
    }
}

console.log(longest2);
console.log( '*'.repeat((longest2.length) + 6));

for (let i in arrayOfWords) {
    if (i == 0) {
        console.log("*" + arrayOfWords[i] + " ".repeat((longest2.length) - (arrayOfWords[i].length)) + "    *");
    } else {
        console.log("*" + arrayOfWords[i] + " ".repeat((longest2.length) - (arrayOfWords[i].length)) + "    *");
    }
}

console.log( '*'.repeat((longest2.length) + 6));