#every chess combo
combo = [
    "p",
    "b",
    "k",
    "r",
    "q",
    "k"
]
for B in range(6):
    for A in range(8):
        print(f"{combo[B]}a{A + 1}")
        print(f"{combo[B]}b{A + 1}")
        print(f"{combo[B]}c{A + 1}")
        print(f"{combo[B]}d{A + 1}")
        print(f"{combo[B]}e{A + 1}")
        print(f"{combo[B]}f{A + 1}")
        print(f"{combo[B]}g{A + 1}")
        print(f"{combo[B]}h{A + 1}")