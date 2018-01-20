type Buffer = [Int]
type SortedList = [Int]
type NoRepeatItemList = [Int]

dropSameItem :: Int -> SortedList -> SortedList
dropSameItem v (x:xs) | x > v  = (x:xs)
                      | x < v  = (x:(dropSameItem v xs))
                      | x == v = dropSameItem v xs
dropSameItem _ [] = []

pop :: Buffer -> SortedList -> NoRepeatItemList
pop bs (x:y:xs) = if x == y
                  then pop bs $ dropSameItem x xs
                  else pop (x:bs) $ (y:xs)
pop bs (x:[])   = reverse (x:bs)
pop bs []       = reverse bs


run :: SortedList -> IO NoRepeatItemList
run = return . pop []
