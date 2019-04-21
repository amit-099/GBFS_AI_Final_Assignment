import time

from math import ceil

from Graph_Construction import construct_graph
from OCL_Framework import OCL_Algo
from a_star_search import a_star_algo
from best_first_search import best_first_algo
from comparison_graph import compare_by_time_and_node, compare_by_time_and_edge, compare_by_expanded_node


def single_run():
    total_nodes = 5
    total_edges = 10
    goal_node = total_nodes - 1
    graph = construct_graph(total_nodes, total_edges)

    start_ocl = time.time()
    result_ocl = OCL_Algo(graph, goal_node)
    end_ocl = time.time()

    print("Result OCL:  ", result_ocl)

    elapsed_ocl = (end_ocl - start_ocl) * 1000
    print("elapsed OCL:   ", elapsed_ocl)

    start_astar = time.time()
    result_astar = a_star_algo(graph, goal_node)
    end_astar = time.time()

    print("Result a star:  ", result_astar)

    elapsed_astar = (end_astar - start_astar) * 1000
    print("elapsed aStar:   ", elapsed_astar)

    start_best_first = time.time()
    result_best_first = best_first_algo(graph, goal_node)
    end_best_first = time.time()

    print("Result best first:  ", result_best_first)

    elapsed_best_first = (end_best_first - start_best_first) * 1000
    print("elapsed best first:   ", elapsed_best_first)


def comp_by_total_expanded_nodes():
    total_nodes = 5
    x = []
    y1 = []
    y2 = []
    y3 = []

    while True:
        if total_nodes >= 500:
            break
        total_edges = 3 * total_nodes
        goal_node = total_nodes - 1
        nodes1 = 0
        nodes2 = 0
        nodes3 = 0

        for i in range(200):
            graph = construct_graph(total_nodes, total_edges)

            result_ocl = OCL_Algo(graph, goal_node)
            nodes_ocl = result_ocl.__len__()

            result_astar = a_star_algo(graph, goal_node)
            nodes_astar = result_astar.__len__()

            result_best_first = best_first_algo(graph, goal_node)
            nodes_best_first = result_best_first.__len__()

            nodes1 += nodes_ocl
            nodes2 += nodes_astar
            nodes3 += nodes_best_first

        x.append(total_nodes)
        y1.append(nodes1 / 200)
        y2.append(nodes2 / 200)
        y3.append(nodes3 / 200)

        if total_nodes < 50:
            total_nodes += 5
        elif total_nodes < 200:
            total_nodes += 10
        elif total_nodes < 350:
            total_nodes += 30
        else:
            total_nodes += 50

        if total_nodes == 50:
            compare_by_expanded_node(x, y1, y2, y3)
        elif total_nodes == 200:
            compare_by_expanded_node(x, y1, y2, y3)
        elif total_nodes == 350:
            compare_by_expanded_node(x, y1, y2, y3)
        elif total_nodes == 500:
            compare_by_expanded_node(x, y1, y2, y3)


def comp_by_nodes_time():
    total_nodes = 5
    x = []
    y1 = []
    y2 = []
    y3 = []

    while True:
        if total_nodes >= 500:
            break
        total_edges = 3 * total_nodes
        goal_node = total_nodes - 1
        time1 = 0
        time2 = 0
        time3 = 0

        for i in range(200):
            graph = construct_graph(total_nodes, total_edges)

            start_ocl = time.time()
            result_ocl = OCL_Algo(graph, goal_node)
            end_ocl = time.time()

            elapsed_ocl = end_ocl - start_ocl
            print("elapsed OCL:   ", elapsed_ocl)

            start_astar = time.time()
            result_astar = a_star_algo(graph, goal_node)
            end_astar = time.time()

            elapsed_astar = end_astar - start_astar
            print("elapsed aStar:   ", elapsed_astar)

            start_best_first = time.time()
            result_best_first = best_first_algo(graph, goal_node)
            end_best_first = time.time()

            elapsed_best_first = end_best_first - start_best_first
            print("elapsed best first:   ", elapsed_best_first)

            time1 += elapsed_ocl
            time2 += elapsed_astar
            time3 += elapsed_best_first
        x.append(total_nodes)
        y1.append(time1 / 200)
        y2.append(time2 / 200)
        y3.append(time3 / 200)

        if total_nodes < 50:
            total_nodes += 5
        elif total_nodes < 200:
            total_nodes += 10
        elif total_nodes < 350:
            total_nodes += 30
        else:
            total_nodes += 50

        if total_nodes == 50:
            compare_by_time_and_node(x, y1, y2, y3)
        elif total_nodes == 200:
            compare_by_time_and_node(x, y1, y2, y3)
        elif total_nodes == 350:
            compare_by_time_and_node(x, y1, y2, y3)
        elif total_nodes == 500:
            compare_by_time_and_node(x, y1, y2, y3)


def comp_by_edges_time():
    total_edges = 15
    x = []
    y1 = []
    y2 = []
    y3 = []

    while True:
        if total_edges >= 2000:
            break
        total_nodes = ceil(total_edges / 3)
        goal_node = total_nodes - 1
        time1 = 0
        time2 = 0
        time3 = 0

        for i in range(200):
            graph = construct_graph(total_nodes, total_edges)

            start_ocl = time.time()
            result_ocl = OCL_Algo(graph, goal_node)
            end_ocl = time.time()

            elapsed_ocl = end_ocl - start_ocl
            print("elapsed OCL:   ", elapsed_ocl)

            start_astar = time.time()
            result_astar = a_star_algo(graph, goal_node)
            end_astar = time.time()

            elapsed_astar = end_astar - start_astar
            print("elapsed aStar:   ", elapsed_astar)

            start_best_first = time.time()
            result_best_first = best_first_algo(graph, goal_node)
            end_best_first = time.time()

            elapsed_best_first = end_best_first - start_best_first
            print("elapsed best first:   ", elapsed_best_first)

            time1 += elapsed_ocl
            time2 += elapsed_astar
            time3 += elapsed_best_first
        x.append(total_edges)
        y1.append(time1 / 200)
        y2.append(time2 / 200)
        y3.append(time3 / 200)

        if total_edges < 150:
            total_edges += 15
        elif total_edges < 600:
            total_edges += 30
        elif total_edges < 1050:
            total_edges += 90
        else:
            total_edges += 150

        if total_edges == 200:
            compare_by_time_and_edge(x, y1, y2, y3)
        elif total_edges == 600:
            compare_by_time_and_edge(x, y1, y2, y3)
        elif total_edges == 1000:
            compare_by_time_and_edge(x, y1, y2, y3)
        elif total_edges >= 2000:
            compare_by_time_and_edge(x, y1, y2, y3)
