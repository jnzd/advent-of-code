-- -- --- Part Two ---
-- Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

-- Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

-- An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
-- An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
-- Considering all lines from the above example would now produce the following diagram:

-- 1.1....11.
-- .111...2..
-- ..2.1.111.
-- ...1.2.2..
-- .112313211
-- ...1.2....
-- ..1...1...
-- .1.....1..
-- 1.......1.
-- 222111....
-- You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

-- Consider all of the lines. At how many points do at least two lines overlap?

import Data.List

formatInput :: String -> ((Int, Int), (Int, Int))
formatInput s =
    let x1 = read $ takeWhile (/= ',') s
        s' = drop 1 $ dropWhile (/= ',') s
        y1 = read $ takeWhile (/= ' ') s'
        s'' = drop 4 $ dropWhile (/= ' ') s'
        x2 = read $ takeWhile (/= ',') s''
        s''' = drop 1 $ dropWhile (/= ',') s''
        y2 = read $ takeWhile (/= ' ') s'''
    in ((x1, y1), (x2, y2))

pointsCovered :: ((Int, Int), (Int, Int)) -> [(Int, Int)]
pointsCovered ((x1, y1), (x2, y2))
    | x1 == x2  = [(x1, y) | y <- [min y1 y2 .. max y1 y2]]
    | y1 == y2  = [(x, y1) | x <- [min x1 x2 .. max x1 x2]]
    | x1 <= x2 && y1 <= y2 = 
        [(min x1 x2 + i, min y1 y2 + i) | i <- [0 .. range]]
    | x1 <= x2 && y1 >= y2 = 
        [(min x1 x2 + i, max y1 y2 - i) | i <- [0 .. range]]
    | x1 >= x2 && y1 <= y2 = 
        [(max x1 x2 - i, min y1 y2 + i) | i <- [0 .. range]]
    | x1 >= x2 && y1 >= y2 = 
        [(max x1 x2 - i, max y1 y2 - i) | i <- [0 .. range]]
    | otherwise = []
    where range = abs $ x1 - x2

main :: IO ()
main = do
    input <- readFile "in.txt"
    let formattedVents = map formatInput $ lines input
    let coveredPoints = filter (\x -> length x > 1) $ groupBy (\(x1,y1) (x2,y2) -> x1 == x2 && y1 == y2) $ sort $ concatMap pointsCovered formattedVents
    print $ length coveredPoints