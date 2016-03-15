#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import unittest

from sklearn.metrics.pairwise import euclidean_distances

import numpy as np

from fastdtw import fastdtw, dtw


class FastdtwTest(unittest.TestCase):

    def setUp(self):
        self.x_1d = [1, 2, 3, 4, 5]
        self.y_1d = [2, 3, 4]
        self.x_2d = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
        self.y_2d = np.array([[2,2], [3,3], [4,4]])
        self.dist_2d = lambda a, b: sum((a - b) ** 2) ** 0.5

    def test_1d_fastdtw(self):
        self.assertEqual(fastdtw(self.x_1d, self.y_1d, dist=euclidean_distances)[0], 2)

    def test_1d_dtw(self):
        self.assertEqual(dtw(self.x_1d, self.y_1d ,
                             dist=euclidean_distances)[0], 2)

    def test_2d_fastdtw(self):
        self.assertAlmostEqual(fastdtw(self.x_2d, self.y_2d, dist=euclidean_distances)[0], ((1+1)**0.5)*2)

                
if __name__ == '__main__':
    unittest.main()
