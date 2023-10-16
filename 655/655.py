print(
    *(
        " ".join(
            x.capitalize()
            for x in input().split()
        )
        for _ in range(int(input())))
    ,
    sep="\n"
)
