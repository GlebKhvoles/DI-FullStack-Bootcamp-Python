function song() {
    let numBottles = 0;  
    let dropBottles = 0; 
    while (isNaN(numBottles) || numBottles == 0) {
        numBottles = Number(prompt("Enter number of bottles"));
    }       

    while (numBottles > 0) {
        dropBottles += 1;
        console.log(`${numBottles} ${numBottles == 1 ? "bottle":"bottles"} of beer on the wall`);    
        console.log(`${numBottles} ${numBottles == 1 ? "bottle":"bottles"} of beer`);  
        
        if (numBottles > dropBottles) {
            numBottles -= dropBottles;
            console.log(`Take ${dropBottles} down, pass ${dropBottles == 1 ? "it":"them"} it around`);  
            console.log(`${numBottles} ${numBottles == 1 ? "bottle":"bottles"} of beer on the wall`);           
        } else {
            dropBottles = numBottles;
            numBottles = 0;
            console.log(`Take ${dropBottles} down, pass ${dropBottles == 1 ? "it":"them"} it around`);  
            console.log(`no bottle of beer on the wall`);               
        }
        console.log(``);   
    }
} 

song();