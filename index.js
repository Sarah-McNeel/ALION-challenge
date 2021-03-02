const fs = require('fs')

try {
    const data = fs.readFileSync('./data.txt', 'utf-8').split('\n')
    var rows = data[0].split('x')[0]
    var col = data[0].split('x')[1]
    var puzzle = data.slice(1, parseInt(rows) + 1)
    console.log(puzzle)
    var wordbank = data.slice(parseInt(rows) + 1)
    console.log(wordbank)
    wordbank.forEach(word => {
        word.split('').forEach((char, charI) => {
            puzzle.forEach((row, i) => {
                const index = row.indexOf(char)
                if (word == "") {
                    path.forEach(function (e) {
                        mark[e.row][e.com] = true;
                    });
                } else if (0 <= row && row < grid.length &&
                    0 <= col && col < grid[row].length &&
                    !in_path(path, row, col) &&
                    word[0] == grid[row][col]) {
                    for (var r = -1; r <= 1; r++) {
                        for (var c = -1; c <= 1; c++) {
                            search(row + r, col + c, word.substr(1), path.concat({ row: row, col: col }));
                            // Find all horizontal left->right and vertical up->down words.
                            function GetWordCount(array2D, word) {
                                var rowCount = array2D.length
                                var rowSize = array2D[0].length
                                var string = Join2DArray(array2D)
                                var wordLen = word.length
                                var wordCount = 0;
                                // Search in rows
                                for (var j = 0; j < rowCount; j++)
                                    for (var i = 0; i <= rowSize - wordLen; i++)
                                        wordCount += IsSubstring(string, word, j * rowSize + i, 1)
                                // Search in columns
                                for (var i = 0; i < rowSize; i++)
                                    for (var j = 0; j <= rowCount - wordLen; j++)
                                        wordCount += IsSubstring(string, word, j * rowSize + i, rowSize)
                                return wordLen > 1 ? wordCount : wordCount / 2
                            }
                        }
                    }
                }
            })
        })
    })
} catch (error) {
    /* do something */
}
