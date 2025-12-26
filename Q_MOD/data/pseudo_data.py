

def load_pseudo_dataset():
    return {"nodes": [1, 2, 3, 4],
"edges": [(1,3), (2,3), (4,3), (1,4)],
"L": {1:0, 2:0, 3:26, 4:0},
"renewables": {
1: 2, # solar what ever pipeline well Lihle!!!!!
2: 12 
},
"R": {
(1,3): 0.40,
(2,3): 8.35,
(4,3): 0.25,
(1,4): 0.30
},


"c_gen": {3: 1.8},
"c_plus": 25.0,
"W_balance": -10.0
}
