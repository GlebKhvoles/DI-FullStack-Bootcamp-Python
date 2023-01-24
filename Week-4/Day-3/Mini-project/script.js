

function playTheGame() {
    let conf = confirm("Do you wanna play a game?");
    let computerNumber = Math.floor(Math.random() * 10);
    console.log(computerNumber);
    if (!conf)  {
        alert('No problem, Goodbye');
    } else if (conf) {
        let q1 = prompt('Enter a number between 0 and 10');
        if (isNaN(q1)) {
            alert('Sorry Not a number, Goodbye');
        }
        if (q1 < 0 || q1 > 10) { 
            alert('Sorry it’s not a good number, Goodbye');           
        }
    }
    compareNumbers();
}


//Part2
function compareNumbers(userNamber, computerNumber) {
    let attempts = 0;
    if (userNamber == computerNumber) {
        alert('WINNER!');
        return true;
    } else if (userNamber > computerNumber) {
        alert('Your number is bigger then the computer’s, guess againYour number is bigger then the computer’s, guess again');
        prompt('Enter a new number');
    } else if (userNamber < computerNumber) {
        alert('Your number is smaller then the computer’s, guess again');
        prompt('Enter a new number');
    } else if (attempts > 3) {
        alert('out of chances');
    }
    }

