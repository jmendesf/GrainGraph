import numpy as np
import os

def compare_edge_curves(edge_curve, prev_edge_curve, idx_map):
    if prev_edge_curve is None or len(prev_edge_curve) == 0 :
        curves = []
        for edge in edge_curve:
            idx1 = idx_map[edge[0]]
            idx2 = idx_map[edge[1]]
            curves.append(tuple((idx1, idx2)))
        return np.array([(0, 0)]), np.array(curves)

    prev_edge_set = set(map(tuple, prev_edge_curve))

    new_tuples = []
    old_tuples = []
    
    for edge in edge_curve:
        idx1 = idx_map[edge[0]]
        idx2 = idx_map[edge[1]]
        if tuple(edge) in prev_edge_set:
            old_tuples.append(tuple((idx1, idx2)))
        else:
            new_tuples.append(tuple((idx1, idx2)))
    
    new_tuples = np.array(new_tuples, dtype=edge_curve.dtype) if len(new_tuples) > 0 else np.array([(0, 0)])
    old_tuples = np.array(old_tuples, dtype=edge_curve.dtype) if len(old_tuples) > 0 else np.array([(0, 0)])

    return new_tuples, old_tuples

def cloud_nodes_add_quantity(ps_cloud, labels_connected, nb_neighbors_connected) :
    ps_cloud.add_scalar_quantity("Labels", labels_connected)
    ps_cloud.add_scalar_quantity("Number of neighbors", nb_neighbors_connected)


def get_sorted_files(directory):
    all_files = os.listdir(directory)
    
    files_only = []
    
    for f in all_files :
        if os.path.isfile(os.path.join(directory, f)) :
            if ".txt" in f :
                files_only.append(f)
    
    sorted_files = sorted([os.path.join(directory, f) for f in files_only])
    
    return sorted_files