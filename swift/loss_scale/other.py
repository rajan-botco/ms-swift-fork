# Copyright (c) ModelScope Contributors. All rights reserved.
from .base import ConfigLossScale


class IgnoreEmptyThinkLossScale(ConfigLossScale):
    loss_scale_config = 'ignore_empty_think.json'


class ThinkMaskLossScale(ConfigLossScale):
    """Zero out loss on <think>...</think> content; full SFT loss on the answer after </think>."""
    loss_scale_config = 'think_mask.json'
