# coding=utf-8
# Copyright 2021 The Deeplab2 Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utility functions for optical flow."""
from cvx2 import latest as cv
import numpy as np


def warp_flow(img: np.ndarray, flow_tensor: np.ndarray) -> np.ndarray:
  flow = flow_tensor.copy()
  h, w = flow.shape[:2]
  flow[..., 0] += np.arange(w)
  flow[..., 1] += np.arange(h)[:, np.newaxis]
  res = cv.remap(img, flow, None, cv.INTER_LINEAR)
  return res


def remove_occlusions(warped_binary_img: np.ndarray,
                      occlusion_map: np.ndarray) -> np.ndarray:
  return warped_binary_img.astype(np.bool) & (1 - occlusion_map).astype(np.bool)
