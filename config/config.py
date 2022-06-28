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

    wi = {
        1: {
            1: 1
        },
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

    #TASK 3 ---------------------------------------

    task3 = {
        "name": "Runge-Kutta-Nystrom",
        "out_path": os.path.join(BASE_PATH, "task3_out", "Runge-Kutta-Nystrom")
    }
