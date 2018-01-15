-- Using haskell just for fun


data Color = Red | White | Blue deriving (Show)

data Collection = Collection {
    red   :: [Color],
    white :: [Color],
    blue  :: [Color]
} deriving (Show)

allocate :: Collection -> Color -> Collection
allocate c color = case color of
                                Red   -> c { red = (color:(red c))}
                                White -> c { white = (color:(white c))}
                                Blue  -> c { blue = (color:(blue c))}

allocates :: [Color] -> Collection
allocates cs = foldl allocate c0 cs
               where c0 = Collection [] [] []

merge :: Collection -> [Color]
merge c = (red c) ++ (white c) ++ (blue c)

run :: IO [Color]
run = return $ merge . allocates $ [Red, Blue, Red, Blue, White, Blue, Red, White]
