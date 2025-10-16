import tkinter as tk
import math
import random
import turtle
import time

class AnimatedSun:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HNO Sun")
        self.root.configure(bg='lightblue')
        
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg='lightblue')
        self.canvas.pack()
        
        self.center_x, self.center_y = 300, 300
        self.iteration = 0
        self.max_iterations = 100
        
        # Sun parameters
        self.sun_radius = 80
        self.num_rays = 16
        self.ray_lengths = [random.randint(40, 70) for _ in range(self.num_rays)]
        
        self.animate()
        
    def animate(self):
        if self.iteration >= self.max_iterations:
            # Animation finished, show Arabic text after a brief pause
            self.root.after(500, self.show_arabic_text)
            return
            
        # Draw the main sun body gradually
        if self.iteration < 50:
            # Animate the sun circle growing
            current_radius = int(self.sun_radius * (self.iteration / 50))
            self.canvas.delete("sun_circle")
            self.canvas.create_oval(
                self.center_x - current_radius, 
                self.center_y - current_radius,
                self.center_x + current_radius, 
                self.center_y + current_radius,
                fill='yellow', outline='orange', width=3, tags="sun_circle"
            )
        
        # Draw rays gradually after the circle is formed
        elif self.iteration < 100:
            ray_index = (self.iteration - 50) * self.num_rays // 50
            
            for i in range(min(ray_index + 1, self.num_rays)):
                angle = 2 * math.pi * i / self.num_rays
                
                # Ray start point (on sun edge)
                start_x = self.center_x + self.sun_radius * math.cos(angle)
                start_y = self.center_y + self.sun_radius * math.sin(angle)
                
                # Ray end point (extending out)
                end_x = self.center_x + (self.sun_radius + self.ray_lengths[i]) * math.cos(angle)
                end_y = self.center_y + (self.sun_radius + self.ray_lengths[i]) * math.sin(angle)
                
                # Draw ray with gradient color
                ray_color = '#FFD700' if i % 2 == 0 else '#FFA500'
                self.canvas.create_line(
                    start_x, start_y, end_x, end_y,
                    fill=ray_color, width=4, tags=f"ray_{i}"
                )
        
        self.iteration += 1
        self.root.after(50, self.animate)
    
    def show_arabic_text(self):
        # Clear canvas and show Arabic text
        self.canvas.delete("all")
        self.canvas.configure(bg='white')
        self.canvas.create_text(
            300, 300,
            text="ههههههه لا أمزح",
            font=("Arial", 48, "bold"),
            fill="black"
        )
        # Wait 6 seconds then close and start turtle
        self.root.after(6000, self.start_turtle_animation)
    
    def start_turtle_animation(self):
        self.root.destroy()
        # Start the turtle animation
        run_turtle_sun()

def run_turtle_sun():
    forw = 10
    t = turtle.Turtle()
    turtle.setup(width=800, height=600)
    turtle.title("HNO Sun")
    turtle.bgcolor("black")
    t.speed(0)
    t.hideturtle()
    
    start_time = time.time()
    iterations = 0
    max_iterations = 201
    
    while iterations < max_iterations:
        t.forward(forw)
        t.color("yellow")
        t.left(120-23)
        t.left(1)
        forw += 1
        t.forward(forw)
        t.color("greenyellow")
        t.right(350)
        t.radians()
        t.color("orange")
        t.right(30)
        
        iterations += 1
    
    turtle.done()

# Run the animation sequence
AnimatedSun().root.mainloop()