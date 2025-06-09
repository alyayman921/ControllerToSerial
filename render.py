# 3D render
import vtk
import os
import threading

# Get the current directory and STL file path
cdir = os.getcwd()
filedir = os.path.join(cdir, "controller_assets", "cube.stl")

class Render:
    def __init__(self, alpha, beta, gamma):
        # Initialize rotation angles
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

        # Reader to load the STL file
        self.reader = vtk.vtkSTLReader()
        self.reader.SetFileName(filedir)

        # Create the transform
        self.transform = vtk.vtkTransform()
        self.apply_transform()

        # Set up the transform filter
        self.transform_filter = vtk.vtkTransformPolyDataFilter()
        self.transform_filter.SetInputConnection(self.reader.GetOutputPort())
        self.transform_filter.SetTransform(self.transform)
        self.transform_filter.Update()

        # Mapper and actor setup
        self.mapper = vtk.vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.transform_filter.GetOutputPort())
        self.actor = vtk.vtkActor()
        self.actor.SetMapper(self.mapper)

        # Renderer and rendering window
        self.renderer = vtk.vtkRenderer()
        self.render_window = vtk.vtkRenderWindow()
        self.render_window.AddRenderer(self.renderer)
        self.render_interactor = vtk.vtkRenderWindowInteractor()
        self.render_interactor.SetRenderWindow(self.render_window)

        # Add the actor to the scene
        self.renderer.AddActor(self.actor)
        self.renderer.SetBackground(0, 0, 0)  # Background color

    def apply_transform(self):
        """ Apply the current rotation values to the transform """
        self.transform.Identity()  # Reset the transform
        self.transform.RotateX(self.alpha)
        self.transform.RotateY(self.beta)
        self.transform.RotateZ(self.gamma)

    def update_rotation(self, alpha, beta, gamma):
        """ Update the rotation angles and re-render the scene """
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.apply_transform()
        self.transform_filter.Update()
        self.render_window.Render()

    def start(self):
        """ Start the rendering process """
        self.render_window.Render()
        self.render_interactor.Start()
    def quit_render(self, obj, event):
        self.render_interactor.Exit()
        self.render_window.Finalize()  # Finalize the window before exiting

if __name__ == "__main__":
    # Initial angles
    initial_alpha = 0
    initial_beta = 0
    initial_gamma = 0

    # Create the render object
    render_obj = Render(initial_alpha, initial_beta, initial_gamma)
    
    # Start rendering
    render_obj.start()

def hi():
    # controller.py
    from render import Render
    import time

    # Create a render object with initial angles
    render_obj = Render(0, 0, 0)

    # Start the rendering in a separate thread
    import threading
    render_thread = threading.Thread(target=render_obj.start)
    render_thread.start()

    # Simulate updating the angles dynamically from the controller
    for i in range(0, 360, 10):
        time.sleep(1)  # Wait for 1 second before updating angles
        render_obj.update_rotation(i, 2 * i, 3 * i)  # Update angles alpha, beta, gamma dynamically
