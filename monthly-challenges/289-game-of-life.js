/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function (board) {

    var copyBoard = JSON.parse(JSON.stringify(board));

    m = board.length;
    n = board[0].length;

    for (let rowId = 0; rowId < board.length; rowId++) {
        const row = copyBoard[rowId];
        for (let colId = 0; colId < row.length; colId++) {
            const cell = row[colId];

            var NghCounts = getNeighbors(rowId, colId, copyBoard).reduce((a, b) => a + b, 0);
            copyBoard = applyRules(cell, NghCounts, rowId, colId, board, copyBoard);


        }
    }

    console.log(board)
    console.log(copyBoard)
};


var applyRules = function (cell, NghCounts, rowId, colId, board, copyB) {
    //console.log(rowId, colId, '--', NghCounts)
    if (cell == 0 && NghCounts == 3) {
        //console.log('Rule 4')
        board[rowId][colId] = 1
    }
    else if (cell == 1 && NghCounts < 2) {
        //console.log('Rule 1')
        board[rowId][colId] = 0
    }
    else if (cell == 1 && NghCounts > 3) {
        //console.log('Rule 3')
        board[rowId][colId] = 0
    }
    else {
        board[rowId][colId] = copyB[rowId][colId];
    }

    return copyB;
}


// get neighbours  functions 
function getNeighbors(i, j, board) {
    let allPosibleIndexes = [
        [i - 1, j],
        [i, j - 1],
        [i - 1, j - 1],
        [i + 1, j],
        [i, j + 1],
        [i + 1, j + 1],
        [i + 1, j - 1],
        [i - 1, j + 1]
    ];
    let allPosibleValues = []
    allPosibleIndexes.forEach(([x, y]) => {
        try {
            allPosibleValues.push(board[x][y])
        } catch (err) {

        }
    })

    //console.log(board)
    //console.log(i, j, allPosibleValues)
    return allPosibleValues.filter(v => v != undefined);
}




gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]);