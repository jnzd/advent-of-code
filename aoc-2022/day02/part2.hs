import System.IO 

score :: [String] -> Int
score x = foldl (+) 0 (map score_game x)

score_game :: String -> Int
score_game [x,_,y] = let v1 = translate_A x in 
                     let v2 = translate_B y in 
                     let v3 = ((v1-1+v2) `mod` 3) + 1 in
                        result v1 v3 + v3

translate_A :: Char -> Int
translate_A 'A' = 1
translate_A 'B' = 2
translate_A 'C' = 3

translate_B :: Char -> Int
translate_B 'X' = -1
translate_B 'Y' = 0
translate_B 'Z' = 1

result :: Int -> Int -> Int
result x y = ((y-x+1) `mod` 3) * 3


main = do  
    contents <- readFile "./in.txt"
    -- contents <- readFile "./sample.txt"
    -- contents <- readFile "./test.txt"
    putStrLn (show (score (lines contents)))