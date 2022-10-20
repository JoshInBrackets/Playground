head' :: [a] -> a
head' [] = error "No head for empty lists!!!"
head' (x:_) = x
main = putStrLn (show (head' [1,2,3,4,5,6,7,8,9,0]))