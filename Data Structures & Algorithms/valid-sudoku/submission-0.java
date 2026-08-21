class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i = 0; i < 9; i++){
            Set<Character> iset = new HashSet<Character>();
            Set<Character> jset = new HashSet<Character>();
            for(int j = 0; j < 9; j++){
                if(board[i][j] != '.'){
                    if(iset.contains(board[i][j])){
                        return false;
                    }
                    iset.add(board[i][j]);
                }
                if(board[j][i] != '.'){
                    if(jset.contains(board[j][i])){
                        return false;
                    }
                    jset.add(board[j][i]);
                }
            }
        }

        for(int r = 0; r < 3; r++){
            for(int c = 0; c < 3; c++){
                Set<Character> sqset = new HashSet<Character>();
                for(int i = r*3; i < r*3 + 3; i++){
                    for(int j = c*3; j < c*3 +3; j++){
                        if(board[i][j] != '.'){
                            if(sqset.contains(board[i][j])){
                                return false;
                            }
                            sqset.add(board[i][j]);
                        }
                    }
                }
            }
        }

        return true;
    }
}
