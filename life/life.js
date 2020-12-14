/* MTG life counter to be turned into an app*/
//Background raidial gradient for JS maipulaztion
//p1 background
var plyrOneBG = "background: radial-gradient(#, #9198e5)";
//p2 background
var plyrTwoBG = "background: radial-gradient(#6aa313, #9c161c)";

//Player One
var countOne = 20;
//Player one life Up
function plyrOneUp(){
    countOne++;
    document.getElementById("numOne").innerHTML = countOne;
    if(countOne > 0){
        document.getElementById("playerOne").style = plyrOneBG;
    }
}

//Player One life Down
function plyrOneDown(){
    countOne--;
    document.getElementById("numOne").innerHTML = countOne;
    if(countOne < 1){
        document.getElementById("playerOne").style.background = "darkred";
    }
}
//Player Two
var countTwo = 20;
//Player Two Life Up
function plyrTwoUp(){
    countTwo++;
    document.getElementById("numTwo").innerHTML = countTwo;
    if(countOne > 0){
        document.getElementById("playerTwo").style = plyrTwoBG;
    }
}
//Player Two Life Down
function plyrTwoDown(){
    countTwo--;
    document.getElementById("numTwo").innerHTML = countTwo;
    if(countTwo < 1){
        document.getElementById("playerTwo").style.background = "darkred";
    }
}
//Reset Line Counters to 20
