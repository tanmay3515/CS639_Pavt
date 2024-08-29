pendown
:a = :x
:b = :y
:c = :z
    if :a > :b [
        if :a > :c [
            left 60
        ] else [
            right 60
    ]
    ]

    if :b > :c [
        if :b > :a [
            left 75
        ] else [
            right 75
        ]
    ]

    if :c > :a [
        if :c > :b [
            left 50
        ] else [
            right 45
    ]
    ]
