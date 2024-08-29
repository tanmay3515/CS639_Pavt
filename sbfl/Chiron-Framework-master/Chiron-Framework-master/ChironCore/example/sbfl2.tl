penup

if :x > 0 [
    if :y > 0 [
        if :z > 0 [
            backward 5
            left 45
        ] else [
            forward 10
            right 45
        ]
    ] else [
        if :z > 0 [
            backward 100
            left 30
        ] else [
            forward 10
            right 30
        ]
    ]
] 