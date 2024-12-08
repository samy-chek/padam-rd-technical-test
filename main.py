from input import parse_cmd_line, parse_file
from graph import Graph

in_file = "hard_to_choose.txt"

def main():
    in_file, plot_graph = parse_cmd_line()
    vertices, edges = parse_file(in_file)
    print(f"#E={len(edges)}, #V={len(vertices)}")
    print("ICIIIIII")
    graph = Graph(vertices, edges)
    if plot_graph:
        graph.plot()


if __name__ == "__main__":
    main()
