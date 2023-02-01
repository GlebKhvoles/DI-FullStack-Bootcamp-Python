let animate = document.getElementById('animate');
let leftPos = 0;

function myMove() {
    leftPos = 0;
    animate.style.left = leftPos + 'px';  
    let box = setInterval(() => {
        leftPos += 1;
        animate.style.left = leftPos + 'px'; 
        if (leftPos == 350) {
            clearInterval(box);
        }        
    }, 1);    
}