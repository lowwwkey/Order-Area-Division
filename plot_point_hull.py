# -*-coding:utf-8-*-

from matplotlib import pyplot as plt

def scatter_plot_set(points_set, color_degree, hull_set=None):
    coords = [i for points in points_set for i in points]
    xs, xy=zip(*coords)
    plt.figure(figsize=(16, 8))
    plt.scatter(xs, xy, c=color_degree, cmap=plt.cm.get_cmap('viridis_r'))
    plt.colorbar()
        
    if hull_set != None:
        for hull in hull_set:
            for i in range(1,len(hull)+1):
                if i==len(hull): i=0 # wrap
                c0=hull[i-1]
                c1=hull[i]
                plt.plot((c0[0],c1[0]),(c0[1],c1[1]),'r')
    plt.show()
