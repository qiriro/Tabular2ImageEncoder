import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import numpy as np


class SuperTML:
    def __init__(self, problem='supervised', image_size=224, verbose=False):
        self.problem = problem
        self.verbose = verbose
        self.folder = None
        self.image_size = image_size
