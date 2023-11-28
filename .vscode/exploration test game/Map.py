import random
rng = random.randint
minimap = [ 
    [3, 3, 100, 100, 9],
    [1, 1, 100, 100, 12],
    [2, 1, 100, 100, 2],
    [3, 1, 100, 100, 1],
    [4, 1, 100, 100, 2],
    [5, 1, 100, 100, 1],
    [5, 2, 100, 100, 2],
    [5, 3, 100, 100, 3],
    [5, 4, 100, 100, 2],
    [5, 5, 100, 100, 11],
    [4, 5, 100, 100, 2],
    [3, 5, 100, 100, 1],
    [2, 5, 100, 100, 2],
    [1, 5, 100, 100, 1],
    [1, 4, 100, 100, 2],
    [1, 2, 100, 100, 2],
    [2, 2, 0,0, 4,"WASD TO MOVE (player 1)"],
    [2, 2.2, 0,0, 4,"ARROW KEYS TO MOVE (player 2)"],
    [2, 2.4, 0,0, 4,"LEFT AND RIGHT SHIFT TO RUN"],
    #hallway
    [0, 2, 100, 100, 5],
    [0, 1, 100, 100, 5],
    [0, 0, 100, 100, 5],
    [0, -1, 100, 100, 5],
    [0, -2, 100, 100, 8, 0, 20],
    [-1, 3, 100, 100, 7],
    [-1, 4, 0, 0,4,"freddy KILL"],
    [-1, 2, 100, 100, 2],
    [-1, 1, 100, 100, 2],
    [-1, 0, 100, 100, 2],
    [-1, -1, 100, 100, 2],
    [1, 0, 100, 100, 2],
    [1, -1, 100, 100, 2],
    [0, 4, 100, 100, 2],
    #checkpoint 2
    [0, 18, 100, 100, 1],
    [-1, 18, 100, 100, 1],
    [1, 18, 100, 100, 1],
    [-1, 19, 100, 100, 8, 2, -16],
    [1, 19, 100, 100, 3],
    [-1, 20, 100, 100, 1],
    [0, 20, 100, 100, 9],
    [0, 21, 100, 100, 1],
    [-1, 21, 100, 100, 1],
    [1, 21, 100, 100, 1],
    [1, 20, 100, 100, 1],
    [0, 19, 0,0, 4,"fake wall ->"],
    [0, 19.2, 0,0, 4,"<-spawn"],
    #hallway
    [-1, 17, 100, 100, 2,],
    [0, 17, 100, 100, 2,],
    [1, 17, 100, 100, 2,],
    [2, 21, 100, 100, 2,],
    [2, 17, 100, 100, 2,],
    [3, 21, 100, 100, 2,],
    [3, 17, 100, 100, 2,],
    [4, 21, 100, 100, 2,],
    [4, 17, 100, 100, 2,],
    [5, 21, 100, 100, 2,],
    [5, 17, 100, 100, 2,],
    [6, 21, 100, 100, 2,],
    [6, 17, 100, 100, 2,],
    [7, 21, 100, 100, 2,],
    [7, 17, 100, 100, 2,],
    [8, 21, 100, 100, 2,],
    [8, 17, 100, 100, 2,],
    [9, 21, 100, 100, 2,],
    [9, 17, 100, 100, 2,],
    [6,18, 100, 100, 10, [0,2], [-2,0], [0,-2], [2,0]],
    [8,18, 100, 100, 10, [0,2], [-2,0], [0,-2], [2,0]],
    [10,18, 100, 100, 10, [0,2], [-2,0], [0,-2], [2,0]],
    [11,20, 100, 100, 10, [0,-2], [2,0], [0,2], [-2,0]],
    [13,20, 100, 100, 10, [0,-2], [2,0], [0,2], [-2,0]],
    [14,18, 100, 100, 10, [0,2], [-2,0], [0,-2], [2,0]],
    [10, 21, 100, 100, 2,],
    [10, 17, 100, 100, 2,],
    [11, 21, 100, 100, 2,],
    [11, 17, 100, 100, 2,],
    [12, 21, 100, 100, 2,],
    [12, 17, 100, 100, 2,],
    [13, 21, 100, 100, 2,],
    [13, 17, 100, 100, 2,],
    [14, 21, 100, 100, 2,],
    [14, 17, 100, 100, 2,],
    [15, 21, 100, 100, 2,],
    [15, 17, 100, 100, 2,],
    [16, 21, 100, 100, 2,],
    [16, 17, 100, 100, 2,],
    [17, 21, 100, 100, 2,],
    [17, 17, 100, 100, 2,],
    [18, 21, 100, 100, 1,],
    [18, 17, 100, 100, 1,],
    [17, 19, 0,0, 4,"Herbert"],
    [18, 20, 100, 100, 1,],
    [18, 18, 100, 100, 1,],
    [19, 21, 100, 100, 1,],
    [19, 17, 100, 100, 1,],
    [20, 21, 100, 100, 1,],
    [20, 17, 100, 100, 1,],
    [20, 19, 100, 100, 9,],
    [21, 21, 100, 100, 1,],
    [21, 17, 100, 100, 1,],
    [22, 21, 100, 100, 1,],
    [22, 17, 100, 100, 1,],
    [22, 20, 100, 100, 1,],
    [22, 18, 100, 100, 1,],
    [23,17, 100, 100, 10, [0,4], [0,-4], [0,4], [0,-4]],
    [25,17, 100, 100, 10, [0,4], [0,-4], [0,4], [0,-4]],
    [27,17, 100, 100, 10, [0,4], [0,-4], [0,4], [0,-4]],
    [29,17, 100, 100, 10, [0,4], [0,-4], [0,4], [0,-4]],
    [31,17, 100, 100, 10, [0,4], [0,-4], [0,4], [0,-4]],
    [23, 20, 100, 100, 1,],
    [23, 18, 100, 100, 1,],
    [24, 20, 100, 100, 1,],
    [24, 18, 100, 100, 1,],
    [25, 20, 100, 100, 1,],
    [25, 18, 100, 100, 1,],
    [26, 20, 100, 100, 1,],
    [26, 18, 100, 100, 1,],
    [27, 20, 100, 100, 1,],
    [27, 18, 100, 100, 1,],
    [28, 20, 100, 100, 1,],
    [28, 18, 100, 100, 1,],
    [29, 20, 100, 100, 1,],
    [29, 18, 100, 100, 1,],
    [30, 20, 100, 100, 1,],
    [30, 18, 100, 100, 1,],
    [31, 20, 100, 100, 1,],
    [31, 18, 100, 100, 1,],
    [32, 20, 100, 100, 1,],
    [32, 18, 100, 100, 1,],
    [23, 21, 100, 100, 1,],
    [23, 17, 100, 100, 1,],
    [24, 21, 100, 100, 1,],
    [24, 17, 100, 100, 1,],
    [25, 21, 100, 100, 1,],
    [25, 17, 100, 100, 1,],
    [26, 21, 100, 100, 1,],
    [26, 17, 100, 100, 1,],
    [27, 21, 100, 100, 1,],
    [27, 17, 100, 100, 1,],
    [28, 21, 100, 100, 1,],
    [28, 17, 100, 100, 1,],
    [29, 21, 100, 100, 1,],
    [29, 17, 100, 100, 1,],
    [30, 21, 100, 100, 1,],
    [30, 17, 100, 100, 1,],
    [31, 21, 100, 100, 1,],
    [31, 17, 100, 100, 1,],
    [32, 21, 100, 100, 1,],
    [32, 17, 100, 100, 1,],
    [32, 19, 100, 100, 9,],
    [33, 16, 100, 100, 1,],
    [33, 22, 100, 100, 1,],
    [34, 16, 100, 100, 1,],
    [34, 22, 100, 100, 1,],
    [35, 16, 100, 100, 1,],
    [35, 22, 100, 100, 1,],
    [36, 16, 100, 100, 1,],
    [36, 22, 100, 100, 1,],
    [37, 16, 100, 100, 1,],
    [37, 22, 100, 100, 1,],
    [38, 16, 100, 100, 1,],
    [38, 22, 100, 100, 1,],
    [39, 16, 100, 100, 1,],
    [39, 22, 100, 100, 1,],
    [40, 16, 100, 100, 1,],
    [40, 22, 100, 100, 1,],
    [34, 17, 100, 100, 10,[0,4], [0,-4], [5,4], [-5,-4]],
    [36, 17, 100, 100, 10,[0,4], [0,-4], [-5,4], [5,-4]],
    [38, 17, 100, 100, 10,[0,4], [0,-4], [5,4], [-5,-4]],
    [40, 17, 100, 100, 10,[0,4], [0,-4], [-5,4], [5,-4]],
    [42, 17, 100, 100, 10,[0,4], [0,-4], [5,4], [-5,-4]],
    [44, 17, 100, 100, 10,[0,4], [0,-4], [-5,4], [5,-4]],
    [44, 17, 100, 100, 10,[0,4], [0,-4], [5,4], [-5,-4]],
    [46, 17, 100, 100, 10,[0,4], [0,-4], [-5,4], [5,-4]],
    [48, 17, 100, 100, 10,[0,4], [0,-4], [5,4], [-5,-4]],
    [50, 17, 100, 100, 10,[0,4], [0,-4], [-5,4], [5,-4]],
    [52, 17, 100, 100, 10,[0,4], [0,-4], [5,4], [-5,-4]],
    [54, 17, 100, 100, 10,[0,4], [0,-4], [-5,4], [5,-4]],
    [41, 16, 100, 100, 1,],
    [41, 22, 100, 100, 1,],
    [42, 16, 100, 100, 1,],
    [42, 22, 100, 100, 1,],
    [43, 16, 100, 100, 1,],
    [43, 22, 100, 100, 1,],
    [44, 16, 100, 100, 1,],
    [44, 22, 100, 100, 1,],
    [45, 16, 100, 100, 1,],
    [45, 22, 100, 100, 1,],
    [46, 16, 100, 100, 1,],
    [46, 22, 100, 100, 1,],
    [47, 16, 100, 100, 1,],
    [47, 22, 100, 100, 1,],
    [48, 16, 100, 100, 1,],
    [48, 22, 100, 100, 1,],
    [49, 16, 100, 100, 1,],
    [49, 22, 100, 100, 1,],
    [50, 16, 100, 100, 1,],
    [50, 22, 100, 100, 1,],
    [51, 16, 100, 100, 1,],
    [51, 22, 100, 100, 1,],
    [52, 16, 100, 100, 1,],
    [52, 22, 100, 100, 1,],
    [53, 16, 100, 100, 1,],
    [53, 22, 100, 100, 1,],
    [54, 16, 100, 100, 1,],
    [54, 22, 100, 100, 1,],
    [35, 21, 100, 100, 10,[0,-4], [0,4], [5,-4], [-5,4]],
    [37, 21, 100, 100, 10,[0,-4], [0,4], [-5,-4], [5,4]],
    [39, 21, 100, 100, 10,[0,-4], [0,4], [5,-4], [-5,4]],
    [41, 21, 100, 100, 10,[0,-4], [0,4], [-5,-4], [5,4]],
    [43, 21, 100, 100, 10,[0,-4], [0,4], [5,-4], [-5,4]],
    [45, 21, 100, 100, 10,[0,-4], [0,4], [-5,-4], [5,4]],
    [47, 21, 100, 100, 10,[0,-4], [0,4], [5,-4], [-5,4]],
    [49, 21, 100, 100, 10,[0,-4], [0,4], [-5,-4], [5,4]],
    [51, 21, 100, 100, 10,[0,-4], [0,4], [5,-4], [-5,4]],
    [53, 21, 100, 100, 10,[0,-4], [0,4], [-5,-4], [5,4]],
    [37, 19, 100, 100, 9,],
    [42, 19, 100, 100, 9,],
    [47, 19, 100, 100, 9,],
    [52, 19, 100, 100, 9,],
    [55, 16, 100, 100, 1,],
    [55, 19, 100, 100, 1,],
    [55, 20, 100, 100, 1,],
    [55, 21, 100, 100, 1,],
    [55, 22, 100, 100, 1,],
    [55, 17, 100, 100, 9,],
    [56, 18, 100, 100, 1,],
    [56, 16, 100, 100, 6,],
    [57, 18, 100, 100, 1,],
    [57, 16, 100, 100, 1,],
    [57, 17, 100, 100, 1,],
    [55, 18, 100, 100, 1,],
    [50, 14, 100, 100, 1,],
    [50, 15, 100, 100, 1,],
    [58, 16, 100, 100, 1,],
    [58, 15, 100, 100, 1,],
    [58, 14, 100, 100, 1,],
    [58, 13, 100, 100, 1,],
    [58, 12, 100, 100, 1,],
    [50, 13, 100, 100, 1,],
]

