from input import parse_cmd_line, parse_file
from graph import Graph


def main():
    in_file, plot_graph = parse_cmd_line()
    vertices, edges = parse_file(in_file)
    print(f"#E={len(edges)}, #V={len(vertices)}")
    print("on est ici là")
    graph = Graph(vertices, edges)
    
    
    # On trouve un chemin qui passe par toutes les arêtes
    path = graph.find_path()
    
    if plot_graph:
        graph.plot()


if __name__ == "__main__":
    main()

