import unittest
from medical_data_visualizer import draw_cat_plot, draw_heat_map

class TestMedicalData(unittest.TestCase):
    def test_catplot_figure(self):
        fig = draw_cat_plot()
        self.assertIsNotNone(fig)

    def test_heatmap_figure(self):
        fig = draw_heat_map()
        self.assertIsNotNone(fig)

if __name__ == "__main__":
    unittest.main()
