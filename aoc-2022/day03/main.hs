import System.IO 

solve_one :: [String] -> Int
solve_one x = sum $ map (get_priority . get_duplicate) x

solve_two :: [String] -> Int
solve_two xs = sum $ map get_priority (map get_common_item (group xs))

get_duplicate :: String -> Char
get_duplicate x = go (take ((length x) `div` 2) x) (drop ((length x) `div` 2) x)
    where go (x:xs) ys = if x `elem` ys then x else go xs ys

items :: String
items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

get_priority :: Char -> Int
get_priority x = head [i | (i, y) <- zip [1..] items, y == x]

group :: [String] -> [[String]]
group [] = []
group (x:y:z:xs) = [x,y,z] : group xs

get_common_item :: [String] -> Char
get_common_item [xs,ys,zs] = head [x | x <- xs, x `elem` ys, x `elem` zs]

main = do  
    contents <- readFile "./in.txt"
    -- contents <- readFile "./sample.txt"
    putStrLn $ show $ solve_one $ lines contents
    putStrLn $ show $ solve_two $ lines contents