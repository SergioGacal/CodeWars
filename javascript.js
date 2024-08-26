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

function solveTTT(board) {
    for (let i = 0; i < 9; i++) {
        if (board[i] === '') {
            board[i] = 'X';
            if (isWinningMove(board, 'X')) {
                return i;
            }
            board[i] = '';
        }
    }
    for (let i = 0; i < 9; i++) {
        if (board[i] === '') {
            return i;
        }
    }
    return -1;
}

function isWinningMove(board, player) {
    const winningCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];

    return winningCombos.some(combo => {
        return combo.every(index => board[index] === player);
    });
}

var laLigaGoals = 43;
var championsLeagueGoals = 10;
var copaDelReyGoals = 5;

var totalGoals = laLigaGoals + championsLeagueGoals + copaDelReyGoals;