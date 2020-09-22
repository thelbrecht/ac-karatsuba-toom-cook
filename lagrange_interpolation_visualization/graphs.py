import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class Graphs:  
    def create_view(self):
        fig = plt.figure()
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_color(self.maincolor)
        ax.spines['bottom'].set_color(self.maincolor)

        ax.xaxis.label.set_color(self.maincolor)
        ax.yaxis.label.set_color(self.maincolor)
        ax.tick_params(axis='x', colors=self.maincolor)
        ax.tick_params(axis='y', colors=self.maincolor)

        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.setp(ax.spines.values(), linewidth=1.5)
        
        ax.xaxis.set_tick_params(width=1)
        ax.yaxis.set_tick_params(width=1)
        
        
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')

        return plt
    def linear_function(self):
        x = np.linspace(-8,8,100)
        self.maincolor = 'black'
        plt = self.create_view()


        plt.plot(x,x+3, self.maincolor)

        plt.plot(0,3,'ro') 
        plt.plot(-3,0,'ro') 


        plt.savefig("linear_function.png",transparent=True)

    def quadratic_function(self):
        x = np.linspace(-10,10,100)

        self.maincolor = 'black'
        plt = self.create_view()

        
        plt.plot(1,1,'ro') 
        plt.plot(-1,1,'ro') 
        plt.plot(0,0, 'ro') 

        plt.plot(x, x**2, self.maincolor)
        plt.savefig("quadratic_function.png",transparent=True)
    
    
    def cubic_function(self):
        x = np.linspace(0.2,10,100)
        self.maincolor = 'white'
        plt = self.create_view()
        # red dashes, blue squares and green triangles

        plt.plot(x, x**3, 'w')
        plt.savefig("introductory_graphs/cubic_function.png",transparent=True)

    def render_all(self):
        self.linear_function()
        self.quadratic_function()
        # self.cubic_function()

g = Graphs()
g.render_all()