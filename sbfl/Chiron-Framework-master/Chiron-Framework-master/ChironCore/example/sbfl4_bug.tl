if(:x<20)
    [   if(:y<20)
            [   if (:z<30)
                [pendown
                forward 30]
                ] 
        else
            [ right(90)]]
else
    [   if(:y<20)[
           if (:z<30)
            [ right(90) ]]
        else
            [backward 20]]