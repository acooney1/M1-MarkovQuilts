import matplotlib.pyplot as plt
import random
from PIL import Image
"""
A script utilizing Markov chains to generate patchwork quilt art. Patch patterns are treated as states with defined transition probabilities to create a visually appealing quilt design.
Patch patterns sourced from https://www.mywebquilter.com/ and manipulated for uniqueness and clarity.

@author Amanda Cooney
@version 2025.9.16
"""

# defining transition matrix: quilt patch patterns = states with specified transition probabilities

# randomized transition matrix
patch_patterns = {
    "vertical_stripes": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.1, "four_square_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.1},
    "nine_square_checker": {"vertical_stripes": 0.1, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.1},
    "calico": {"vertical_stripes": 0.1, "nine_square_checker": 0.1, "calico": 0.0, "four_square_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.0, "broken_dishes": 0.1},
    "four_square_checker": {"vertical_stripes": 0.1, "nine_square_checker": 0.8, "calico": 0.1, "four_square_checker": 0.0, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0},
    "antique": {"vertical_stripes": 0.4, "nine_square_checker": 0.2, "calico": 0.1, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.1, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0},
    "diamond": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.1, "four_square_checker": 0.2, "antique": 0.4, "diamond": 0.0, "ninesquarehalfcolor": 0.1, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.0},
    "ninesquarehalfcolor": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.1, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.4},
    "blue+white": {"vertical_stripes": 0.3, "nine_square_checker": 0.1, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.1, "broken_dishes": 0.1},
    "orange_pinwheel": {"vertical_stripes": 0.0, "nine_square_checker": 0.4, "calico": 0.1, "four_square_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0},
    "pink_rhombus": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.2, "pink_rhombus": 0.0, "half_checker": 0.1, "broken_dishes": 0.3},
    "half_checker": {"vertical_stripes": 0.0, "nine_square_checker": 0.1, "calico": 0.1, "four_square_checker": 0.1, "antique": 0.1, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.1, "pink_rhombus": 0.1, "half_checker": 0.0, "broken_dishes": 0.1},
    "broken_dishes": {"vertical_stripes": 0.1, "nine_square_checker": 0.1, "calico": 0.1, "four_square_checker": 0.1, "antique": 0.3, "diamond": 0.1, "ninesquarehalfcolor": 0.1, "blue+white": 0.1, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0}
}

# cool-toned transition matrix
# patch_patterns = {
#     "vertical_stripes": {"vertical_stripes": 0.0, "nine_square_checker": 0.2, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.2},
#     "nine_square_checker": {"vertical_stripes": 0.2, "nine_square_checker": 0.2, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0},
#     "calico": {"vertical_stripes": 0.2, "nine_square_checker": 0.2, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.2},
#     "four_square_checker": {"vertical_stripes": 0.2, "nine_square_checker": 0.2, "calico": 0.2, "four_square_checker": 0.0, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.2},
#     "antique": {"vertical_stripes": 0.2, "nine_square_checker": 0.0, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.2},
#     "diamond": {"vertical_stripes": 0.2, "nine_square_checker": 0.2, "calico": 0.0, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.2},
#     "ninesquarehalfcolor": {"vertical_stripes": 0.2, "nine_square_checker": 0.0, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.2},
#     "blue+white": {"vertical_stripes": 0.2, "nine_square_checker": 0.2, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.2},
#     "orange_pinwheel": {"vertical_stripes": 0.2, "nine_square_checker": 0.2, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0},
#     "pink_rhombus": {"vertical_stripes": 0.0, "nine_square_checker": 0.2, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.2},
#     "half_checker": {"vertical_stripes": 0.2, "nine_square_checker": 0.0, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.2},
#     "broken_dishes": {"vertical_stripes": 0.2, "nine_square_checker": 0.0, "calico": 0.2, "four_square_checker": 0.2, "antique": 0.0, "diamond": 0.0, "ninesquarehalfcolor": 0.0, "blue+white": 0.2, "orange_pinwheel": 0.0, "pink_rhombus": 0.0, "half_checker": 0.0, "broken_dishes": 0.0},
# }

# warm-toned transition matrix
# patch_patterns = {
#     "vertical_stripes": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.2, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.2, "pink_rhombus": 0.2, "half_checker": 0.0, "broken_dishes": 0.0},
#     "nine_square_checker": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.2, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.2, "pink_rhombus": 0.0, "half_checker": 0.2, "broken_dishes": 0.0},
#     "calico": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.2, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.2, "half_checker": 0.2, "broken_dishes": 0.0},
#     "four_square_checker": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.2, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.2, "half_checker": 0.2, "broken_dishes": 0.0},
#     "antique": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.2, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.2, "pink_rhombus": 0.2, "half_checker": 0.2, "broken_dishes": 0.0},
#     "diamond": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.0, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.2, "pink_rhombus": 0.2, "half_checker": 0.2, "broken_dishes": 0.0},
#     "ninesquarehalfcolor": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.0, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.2, "pink_rhombus": 0.2, "half_checker": 0.2, "broken_dishes": 0.0},
#     "blue+white": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.0, "diamond": 0.2, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.2, "pink_rhombus": 0.2, "half_checker": 0.2, "broken_dishes": 0.0},
#     "orange_pinwheel": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.0, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.2, "pink_rhombus": 0.2, "half_checker": 0.2, "broken_dishes": 0.0},
#     "pink_rhombus": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.2, "ninesquarehalfcolor": 0.0, "blue+white": 0.0, "orange_pinwheel": 0.2, "pink_rhombus": 0.2, "half_checker": 0.2, "broken_dishes": 0.0},
#     "half_checker": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.2, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.0, "pink_rhombus": 0.2, "half_checker": 0.2, "broken_dishes": 0.0},
#     "broken_dishes": {"vertical_stripes": 0.0, "nine_square_checker": 0.0, "calico": 0.0, "four_square_checker": 0.0, "antique": 0.2, "diamond": 0.2, "ninesquarehalfcolor": 0.2, "blue+white": 0.0, "orange_pinwheel": 0.2, "pink_rhombus": 0.0, "half_checker": 0.2, "broken_dishes": 0.0},
# }


# isolating pattern names for random selection
pattern_names = list(patch_patterns.keys())

# generative function to call the next patch based upon the above transition matrix
def get_next_patch(current_patch="vertical_stripes"):
    next_patch = random.choices(pattern_names, [patch_patterns[current_patch][next_patch] for next_patch in pattern_names], k=48)
    return next_patch

quilt = get_next_patch("vertical_stripes")
print(quilt)

# creating a list of images to visualize the patch patterns
patch_visuals = []

for patch in quilt:
    img = Image.open(f"assets/{patch}.png")
    patch_visuals.append(img)

# setting up a mutable index to label the saved output file
idx = 5

# displaying the generated quilt pattern using matplotlib
for i, img in enumerate(patch_visuals):
    plt.subplot(8, 6, i + 1)
    plt.imshow(img)
    plt.axis('off')

# saving the generated quilt pattern as a single image to the examples folder
output_path = f"examples/generated_quilt({idx}).png"
plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.close()