import numpy as np

def calculate_rdf(volume, num_particles, distances, bin_width):
    bins = np.arrange(0, max(distances) + bin_width, bin_width)
    hist, edges = np.histogram(distances, bins = bins)

    rdf = []
    for i in range(len(hist)):
        r = (edges[i] + edges[i+1])/2
        shell_volume = 4 * np.pi * r**2 * bin_width
        number_density = num_particles/ volume


        

