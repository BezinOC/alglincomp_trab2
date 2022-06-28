import os

class Settings:

    BASE_PATH = os.getcwd()

    #TASK 1 ---------------------------------------

    task1_1 = {
        "name": "Newton-Raphson",
        "out_path": os.path.join(BASE_PATH, "task1_out", "newton")
    }

    task1_2 = {
        "name": "Broyden",
        "out_path": os.path.join(BASE_PATH, "task1_out", "broyden")
    }

    #TASK 2 ---------------------------------------

    task2_1 = {
        1 : {
            "name": "Newton-Raphson",
            "out_path": os.path.join(BASE_PATH, "task2_out", "raiz", "newton")
        },
        2 : {
            "name": "Broyden",
            "out_path": os.path.join(BASE_PATH, "task2_out", "raiz", "broyden")
        }
    }

    task2_2 = {

    }

    task2_3 = {
        1 : {
            "name": "Derivada Passo a Frente",
            "out_path": os.path.join(BASE_PATH, "task2_out", "derivada_df", "foward")
        },
        2 : {
            "name": "Derivada Passo ATrás",
            "out_path": os.path.join(BASE_PATH, "task2_out", "derivada_df", "back")
        },
        3 : {
            "name": "Derivada por Diferença Central",
            "out_path": os.path.join(BASE_PATH, "task2_out", "derivada_df", "central")
        }
    }

    task2_4 = {
        1 : {
            "name": "Richard",
            "out_path": os.path.join(BASE_PATH, "task2_out", "derivada_re", "richard")
        },
    }

    wi_pol = {
        2: {
            1: 1/2,
            2: 1/2
        },
        3: {
            1: 1/6,
            2: 2/3,
            3: 1/6
        },
        4: {
            1: 1/8,
            2: 3/8,
            3: 3/8,
            4: 1/8
        },
        5: {
            1: 7/90,
            2: 16/45,
            3: 2/15,
            4: 16/45,
            5: 7/90
        },
        6: {
            1: 19/288,
            2: 75/288,
            3: 50/288,
            4: 50/288,
            5: 75/288,
            6: 19/288
        },
        7: {
            1: 41/840,
            2: 216/840,
            3: 27/840,
            4: 272/840,
            5: 27/840,
            6: 216/840,
            7: 41/840
        },
        8: {
            1: 751/17280,
            2: 3577/17280,
            3: 1323/17280,
            4: 2989/17280,
            5: 2989/17280,
            6: 1323/17280,
            7: 3577/17280,
            8: 751/17280
        },
        9: {
            1: 989/28350,
            2: 5888/28350,
            3: -928/28350,
            4: 10496/28350,
            5: -4540/28350,
            6: 10496/28350,
            7: -928/28350,
            8: 5888/28350,
            9: 989/28350
        },
        10: {
            1: 2857/89600,
            2: 15741/89600,
            3: 1080/89600,
            4: 19344/89600,
            5: 5778/89600,
            6: 5778/89600,
            7: 19344/89600,
            8: 1080/89600,
            9: 15741/89600,
            10: 2857/89600
        }
    }

    wi_gauss = {
        2: {
            1: 1,
            2: 1
        },
        3: {
            1: 0.8888888888888888,
            2: 0.5555555555555556,
            3: 0.5555555555555556
        },
        4: {
            1: 0.6521451548625461,
            2: 0.6521451548625461,
            3: 0.3478548451374538,
            4: 0.3478548451374538
        },
        5: {
            1: 0.5688888888888889,
            2: 0.4786286704993665,
            3: 0.4786286704993665,
            4: 0.2369268850561891,
            5: 0.2369268850561891
        },
        6: {
            1: 0.3607615730481386,
            2: 0.3607615730481386,
            3: 0.4679139345726910,
            4: 0.4679139345726910,
            5: 0.1713244923791704,
            6: 0.1713244923791704
        },
        7: {
            1: 0.4179591836734694,
            2: 0.3818300505051189,
            3: 0.3818300505051189,
            4: 0.2797053914892766,
            5: 0.2797053914892766,
            6: 0.1294849661688697,
            7: 0.1294849661688697
        },
        8: {
            1: 0.3626837833783620,
            2: 0.3626837833783620,
            3: 0.3137066458778873,
            4: 0.3137066458778873,
            5: 0.2223810344533745,
            6: 0.2223810344533745,
            7: 0.1012285362903763,
            8: 0.1012285362903763	
        },
        9: {
            1: 0.3302393550012598,
            2: 0.1806481606948574,
            3: 0.1806481606948574,
            4: 0.0812743883615744,
            5: 0.0812743883615744,
            6: 0.3123470770400029,
            7: 0.3123470770400029,
            8: 0.2606106964029354,
            9: 0.2606106964029354
        },
        10: {
            1: 0.2955242247147529,
            2: 0.2955242247147529,
            3: 0.2692667193099963,
            4: 0.2692667193099963,
            5: 0.2190863625159820,
            6: 0.2190863625159820,
            7: 0.1494513491505806,
            8: 0.1494513491505806,
            9: 0.0666713443086881,
            10: 0.0666713443086881
        }
    }

    ti_gauss = {
        2: {
            1: -0.5773502691896257,
            2: 0.5773502691896257
        },
        3: {
            1: 0,
            2: -0.7745966692414834,
            3: 0.7745966692414834
        },
        4: {
            1: -0.3399810435848563,
            2: 0.3399810435848563,
            3: -0.8611363115940526,
            4: 0.8611363115940526
        },
        5: {
            1: 0,
            2: -0.5384693101056831,
            3: 0.5384693101056831,
            4: -0.9061798459386640,
            5: 0.9061798459386640
        },
        6: {
            1: 19/288,
            2: 75/288,
            3: 50/288,
            4: 50/288,
            5: 75/288,
            6: 19/288
        },
        7: {
            1: 41/840,
            2: 216/840,
            3: 27/840,
            4: 272/840,
            5: 27/840,
            6: 216/840,
            7: 41/840
        },
        8: {
            1: 751/17280,
            2: 3577/17280,
            3: 1323/17280,
            4: 2989/17280,
            5: 2989/17280,
            6: 1323/17280,
            7: 3577/17280,
            8: 751/17280
        },
        9: {
            1: 989/28350,
            2: 5888/28350,
            3: -928/28350,
            4: 10496/28350,
            5: -4540/28350,
            6: 10496/28350,
            7: -928/28350,
            8: 5888/28350,
            9: 989/28350
        },
        10: {
            1: 2857/89600,
            2: 15741/89600,
            3: 1080/89600,
            4: 19344/89600,
            5: 5778/89600,
            6: 5778/89600,
            7: 19344/89600,
            8: 1080/89600,
            9: 15741/89600,
            10: 2857/89600
        }
    }


