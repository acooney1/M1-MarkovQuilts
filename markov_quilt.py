import matplotlib.pyplot as plt
import random
from PIL import Image
"""
A script utilizing Markov chains to generate patchwork quilt art

@author Amanda Cooney
@version 2025.9.16
"""

# Defining the quilt patches as state and transition probabilities

patch_patterns = {
    "vertical_stripes": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.1, "foursquare_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.1},
    "nine_square_checker": {"vertical_stripes": 0.1, "nine_square_checker": 0.0, "calico": 0.0, "foursquare_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.1},
    "calico": {"vertical_stripes": 0.1, "nine_square_checker": 0.1, "calico": 0.0, "foursquare_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.0, "broken_dishes": 0.1},
    "foursquare_checker": {"vertical_stripes": 0.1, "nine_square_checker": 0.8, "calico": 0.1, "foursquare_checker": 0.0, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0},
    "antique": {"vertical_stripes": 0.4, "nine_square_checker": 0.2, "calico": 0.1, "foursquare_checker": 0.2, "antique": 0.0, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0},
    "diamond": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.1, "foursquare_checker": 0.2, "antique": 0.4, "diamond": 0.0, "ninesquarehalfcolor": 0.1, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.0},
    "ninesquarehalfcolor": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "foursquare_checker": 0.0, "antique": 0.2, "diamond": 0.1, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.4},
    "blue+white": {"vertical_stripes": 0.3, "nine_square_checker": 0.1, "calico": 0.0, "foursquare_checker": 0.0, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.1},
    "orange_pinwheel": {"vertical_stripes": 0.0, "nine_square_checker": 0.4, "calico": 0.1, "foursquare_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0},
    "pink_rhombus": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "foursquare_checker": 0.0, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.2, "pink_rhombus": 0.0, "half_checker": 0.1, "broken_dishes": 0.3},
    "half_checker": {"vertical_stripes": 0.0, "nine_square_checker": 0.1, "calico": 0.1, "foursquare_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.0, "broken_dishes": 0.1},
    "broken_dishes": {"vertical_stripes": 0.1, "nine_square_checker": 0.1, "calico": 0.1, "foursquare_checker": 0.1, "antique": 0.3, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0}
}

pattern_names = list(patch_patterns.keys())

# Generative function to call the next patch based upon the above transition matrix

def get_next_patch(current_patch="vertical_stripes"):
    next_patch = random.choices(pattern_names, [patch_patterns[current_patch][next_patch] for next_patch in pattern_names], k=12)
    return next_patch

quilt = get_next_patch("vertical_stripes")
print(quilt)

patch_visuals = []

#for patch in quilt: