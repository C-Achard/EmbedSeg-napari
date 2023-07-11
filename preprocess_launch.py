from embedseg_napari._dock_widget import Predict, Train, Preprocess
import napari

if __name__ == "__main__":
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(Preprocess(viewer))
    napari.run()
