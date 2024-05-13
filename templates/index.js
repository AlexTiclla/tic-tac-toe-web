// index.js

document.addEventListener('DOMContentLoaded', () => {
    const squares = document.querySelectorAll('.square');
    const message = document.getElementById('message');
    let currentPlayer = 'X';
    let gameActive = true;

    squares.forEach(square => {
        square.addEventListener('click', handleClick);
    });

function handleClick() {
    if (!gameActive || this.textContent !== '') return;

    this.textContent = currentPlayer;
    if (checkWinner(currentPlayer)) {
        message.textContent = `¡Ganó el jugador ${currentPlayer}!`;
        gameActive = false;
        return;
    }
    if (isBoardFull()) {
        message.textContent = '¡Empate!';
        gameActive = false;
        return;
    }
    if (currentPlayer === 'X') {
        currentPlayer = 'O';
        makeComputerMove();
        // Verifica si la máquina ha ganado después de hacer su movimiento
        if (checkWinner(currentPlayer)) {
            message.textContent = `¡Ganó el jugador ${currentPlayer}!`;
            gameActive = false;
            return;
        }
        // Después de que la máquina hace su movimiento, cambia el jugador a 'X'
        currentPlayer = 'X';
    }
}
    

    function checkWinner(player) {
        const winningConditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
            [0, 4, 8], [2, 4, 6] // Diagonals
        ];
        return winningConditions.some(condition => {
            return condition.every(cell => squares[cell].textContent === player);
        });
    }

    function isBoardFull() {
        return Array.from(squares).every(square => square.textContent !== '');
    }

    function makeComputerMove() {
        let bestScore = -Infinity;
        let move;
        for (let i = 0; i < 9; i++) {
            // ¿Está el lugar vacío?
            if (squares[i].textContent == '') {
                squares[i].textContent = 'O';
                let score = minimax(squares, 0, false);
                squares[i].textContent = '';
                if (score > bestScore) {
                    bestScore = score;
                    move = i;
                }
            }
        }
        squares[move].textContent = 'O';
    }
    
    function minimax(board, depth, isMaximizing) {
        if (checkWinner('O')) {
            return 1;
        } else if (checkWinner('X')) {
            return -1;
        } else if (isBoardFull()) {
            return 0;
        }
    
        if (isMaximizing) {
            let bestScore = -Infinity;
            for (let i = 0; i < 9; i++) {
                if (board[i].textContent == '') {
                    board[i].textContent = 'O';
                    let score = minimax(board, depth + 1, false);
                    board[i].textContent = '';
                    bestScore = Math.max(score, bestScore);
                }
            }
            return bestScore;
        } else {
            let bestScore = Infinity;
            for (let i = 0; i < 9; i++) {
                if (board[i].textContent == '') {
                    board[i].textContent = 'X';
                    let score = minimax(board, depth + 1, true);
                    board[i].textContent = '';
                    bestScore = Math.min(score, bestScore);
                }
            }
            return bestScore;
        }
    }
});
