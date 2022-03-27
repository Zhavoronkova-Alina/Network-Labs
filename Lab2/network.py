import numpy as np
import time
from threading import Thread
from router import Router, DesignatedRouter


class Network:
    designated_router: DesignatedRouter

    def __init__(self):
        self.designated_router = None
        self.stop_flag = False
        self.printer_flag = False
        self.blink_conn_arr = []

    def router_run(self, neighbors):
        conn, index = self.designated_router.add_connection()
        router = Router(conn, index)
        router.neighbors = neighbors.copy()
        router.router_start()

        while True:
            router.proc_message()
            if self.blink_conn_arr[router.index]:
                router.router_off()
                time.sleep(2)
                router.router_start()
                self.blink_conn_arr[router.index] = False

            if self.stop_flag:
                break
        pass

    def designated_router_run(self):
        self.designated_router = DesignatedRouter()

        while True:
            self.designated_router.proc_message()
            if self.printer_flag:
                self.designated_router.print_shortest_ways()
                self.printer_flag = False
            if self.stop_flag:
                break
        pass

    def stopper(self):
        time.sleep(10)
        self.stop_flag = True
        pass

    def printer(self):
        while True:
            time.sleep(1)
            self.printer_flag = True
            if self.stop_flag:
                break
        pass

    def connections_breaker(self):
        time.sleep(2)
        threshold = 0.5
        while True:
            time.sleep(0.01)
            val = np.random.rand()
            if val >= threshold:
                index = np.random.randint(0, len(self.blink_conn_arr))
                self.blink_conn_arr[index] = True
                time.sleep(2)

            if self.stop_flag:
                break
        pass

    def simulate(self, nodes, neighbors):
        dr_thread = Thread(target=self.designated_router_run, args=())

        node_threads = [Thread(target=self.router_run, args=(neighbors[i],)) for i in range(len(nodes))]
        self.blink_conn_arr = [False for i in range(len(nodes))]

        dr_thread.start()
        for i in range(len(nodes)):
            node_threads[i].start()

        printer_thread = Thread(target=self.printer, args=())
        conn_breaker_thread = Thread(target=self.connections_breaker, args=())
        conn_breaker_thread.start()
        printer_thread.start()

        time.sleep(5)
        self.stop_flag = True
        for i in range(len(nodes)):
            node_threads[i].join()

        dr_thread.join()