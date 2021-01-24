


let elem = document.getElementById("res");
let mem = "";


function functionZero() {
    mem += "0";
    elem.innerHTML = mem;
}

function functionOne() {
    mem += "1";
    elem.innerHTML = mem;
}

function functionClr(){
    mem = "";
    elem.innerHTML = "";
}

function functionSum(){
    mem += "+";
    elem.innerHTML = mem;
}

function functionSub(){
    mem += "-";
    elem.innerHTML = mem;
}

function functionMul(){
    mem += "*";
    elem.innerHTML = mem;
}

function functionDiv(){
    mem += "/";
    elem.innerHTML = mem;
}

function functionEql(){
    // group 1 [01]+
    // group 2 [+-*/]+
    // group 3 [01]+
    var re = /(^[01]+)([\+|\-|\*|\/])([01]+$)/;
    var match = re.exec(mem);
   
    var result = processOperator(match[1], match[2], match[3]);
    
    elem.innerHTML= result.toString(2);
    mem = ""
}

function processOperator(num1, operator, num2){
    switch(operator){
      case "+":
          return parseInt(num1, 2 ) + parseInt(num2, 2);
      case "-":
          return parseInt(num1, 2 ) - parseInt(num2, 2);
      case "*":
          return parseInt(num1, 2 ) * parseInt(num2, 2);
      case "/":
          console.log( parseInt(num1, 2 ) / parseInt(num2, 2)) ;
          return parseInt(num1, 2 ) / parseInt(num2, 2) >>>0;
    } 
}



