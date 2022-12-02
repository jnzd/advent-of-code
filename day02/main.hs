import System.IO 

score :: [String] -> Int
score x = foldl (+) 0 (map score_game x)

score_game :: String -> Int
score_game [x,_,y] = result (translate_A x) (translate_B y) + translate_B y

translate_A :: Char -> Int
translate_A 'A' = 1
translate_A 'B' = 2
translate_A 'C' = 3

translate_B :: Char -> Int
translate_B 'X' = 1
translate_B 'Y' = 2
translate_B 'Z' = 3

result :: Int -> Int -> Int
result x y = ((y-x+1) `mod` 3) * 3


main = do  
    contents <- readFile "./in.txt"
    -- contents <- readFile "./sample.txt"
    putStrLn (show (score (lines contents)))