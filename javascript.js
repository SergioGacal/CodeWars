function evenOrOdd(number) {
    if (number % 2 === 0) {
        return 'Odd'} 
        else {return 'Even'}
    }

    function helloWorld(){
        var str = 'Hello World!';
        console.log(str);
      }
      
      let v1 = 50,
      v2 = 100,
      v3 = 150,
      v4 = 200,
      v5 = 2,
      v6 = 250;
      
      function equal1(){
        let a = v1,   
            b = v1;   
        return a + b;
      }
      
      function equal2(){
        let a =  v3,
            b =  v1;
        return a - b;
      }
      
      function equal3(){
        let a =  v1,
            b =  v5;
        return a * b;
      }
      
      function equal4(){
        let a =  v4,
            b =  v5;
        return a / b;
      }
      
      function equal5(){
        let a =  v2,
            b =  v6;
        return a % b;
      }
function howManyDalmatians(number) {
    if (number <= 10) {
        return 'Hardly any';
    } else if (number <= 50) {
        return 'More than a handful!';
    } else if (number <= 100) {
        return "Woah that's a lot of dogs!";
    } else {
        return '101 DALMATIANS!!!';
    }
}
