import time
from threading import Thread
import matplotlib.pyplot as plt

from message import *
from network import Network

def losing_test():
    window_size = 3
    timeout = 0.2
    max_number = 100
    loss_probability_arr = np.linspace(0, 0.9, 9)
    protocol_arr = ["GBN", "SRP"]

    print("p    | GBN             |SRP")
    print("     | t     |k        |t    |  k")

    gbn_time = []
    srp_time = []
    gbn_k = []
    srp_k = []
    for p in loss_probability_arr:
        table_row = f"{p:.1f}\t"

        for protocol in protocol_arr:
            model = Network(window_size, max_number, timeout, p, protocol)
            elapsed_time = model.process_messages()

            k = len(model.received_msgs) / len(model.posted_msgs)

            table_row += f" | {elapsed_time:2.2f}  | {k:.2f}   "
            if protocol == "GBN":
                gbn_time.append(elapsed_time)
                gbn_k.append(k)
            else:
                srp_time.append(elapsed_time)
                srp_k.append(k)

        print(table_row)

    fig, ax = plt.subplots()
    ax.plot(loss_probability_arr, gbn_k, label="Go-Back-N")
    ax.plot(loss_probability_arr, srp_k, label="Selective repeat")
    ax.grid()
    ax.set_xlabel('Вероятность потери пакета')
    ax.set_ylabel('Коэффициент эффективности')
    ax.set_title('Зависимость коэфф. эффек-ти от вер-ти потери пакета, w = 3')
    ax.legend()
    fig.show()

    fig, ax = plt.subplots()
    ax.plot(loss_probability_arr, gbn_time, label="Go-Back-N")
    ax.plot(loss_probability_arr, srp_time, label="Selective repeat")
    ax.grid()
    ax.set_xlabel('Вероятность потери пакета')
    ax.set_ylabel('Время передачи, с')
    ax.set_title('Зависимость врем. передачи от вер-ти потери пакета, w = 3')
    ax.legend()
    fig.show()

    print("p")
    print(loss_probability_arr)
    print("GBN")
    print(gbn_time)
    print("time")
    print("k")
    print(gbn_k)

    print("SRP")
    print(srp_time)
    print("time")
    print("k")
    print(srp_k)


def window_test():
    window_size_arr = range(2, 11)
    timeout = 0.2
    max_number = 100
    loss_probability = 0.2
    protocol_arr = ["GBN", "SRP"]

    print("w    | GBN             |SRP")
    print("     | t     |k        |t    |  k")

    gbn_time = []
    srp_time = []
    gbn_k = []
    srp_k = []
    for window_size in window_size_arr:
        table_row = f"{window_size:}\t"

        for protocol in protocol_arr:
            model = Network(window_size, max_number, timeout, loss_probability, protocol)
            elapsed_time = model.process_messages()

            k = len(model.received_msgs) / len(model.posted_msgs)

            table_row += f" | {elapsed_time:2.2f}  | {k:.2f}   "
            if protocol == "GBN":
                gbn_time.append(elapsed_time)
                gbn_k.append(k)
            else:
                srp_time.append(elapsed_time)
                srp_k.append(k)

        print(table_row)

    fig, ax = plt.subplots()
    ax.plot(window_size_arr, gbn_k, label="Go-Back-N")
    ax.plot(window_size_arr, srp_k, label="Selective repeat")
    ax.grid()
    ax.set_xlabel('Размер окна')
    ax.set_ylabel('Коэффициент эффективности')
    ax.set_title('Зависимость коэфф. эффективности от размера окна, p = 0.2')
    ax.legend()
    fig.show()

    fig, ax = plt.subplots()
    ax.plot(window_size_arr, gbn_time, label="Go-Back-N")
    ax.plot(window_size_arr, srp_time, label="Selective repeat")
    ax.grid()
    ax.set_xlabel('Размер окна')
    ax.set_ylabel('Время передачи, с')
    ax.set_title('Зависимость времени передачи от размера окна, p = 0.2')
    ax.legend()
    fig.show()

    print("w")
    print(window_size_arr)
    print("GBN")
    print(gbn_time)
    print("time")
    print("k")
    print(gbn_k)

    print("SRP")
    print(srp_time)
    print("time")
    print("k")
    print(srp_k)


if __name__ == '__main__':
    print("------------------------------------------")
    print("losing")
    print("------------------------------------------")
    losing_test()

    print("------------------------------------------")
    print("window")
    print("------------------------------------------")
    #window_test()