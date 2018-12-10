import Test.Hspec

import qualified Advent

main :: IO ()
main = hspec $ do
    describe "Day 1" $ do
        it "Star 1" $ do
            content <- readFile "data/day1.txt"
            (Advent.day1 content) `shouldBe` (402 :: Integer)
        it "Star 2" $ do
            content <- readFile "data/day1.txt"
            (Advent.day1Part2 content) `shouldBe` (481 :: Integer)
