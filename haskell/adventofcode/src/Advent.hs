module Advent
    ( day1
    , day1Part2
    ) where

import qualified Data.Set as Set

day1 :: String -> Integer
day1 content = 
    let 
        linesContent = lines content
        numContent = map textToInt linesContent
    in
        sum numContent

textToInt :: String -> Integer
textToInt (strSign:strNum) = 
    let
        factor = if strSign == '+' then 1 else -1
        num = read strNum :: Integer
    in
        num * factor

data SumResult = SumResult Integer Bool (Set.Set Integer)

day1Part2 :: String -> Integer
day1Part2 content =
    let
        linesContent = lines content
        numContent = map textToInt linesContent
        isRepeated (SumResult i b s) = not b  
        repeat = dropWhile (isRepeated) (sumUntilRepeated (cycle numContent) Set.empty)
        (SumResult i b s) = head repeat
    in
        i

sumUntilRepeated :: [Integer] -> Set.Set Integer -> [SumResult]
sumUntilRepeated num set = 
    let
        s = num !! 0 + num !! 1
        newNum = s:(drop 2 num)
        inside = Set.member s set
        newSet = Set.insert s set
    in
        (SumResult s inside newSet):(sumUntilRepeated newNum newSet)
