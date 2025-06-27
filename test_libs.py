try:
    import cv2
    import numpy as np
    import sklearn
    import matplotlib
    import seaborn
    import skimage
    print("All libraries imported successfully!")
except ImportError as e:
    print(f"Error importing library: {e}")