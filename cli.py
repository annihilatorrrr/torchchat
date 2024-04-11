# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import time
import os
from pathlib import Path

import torch
import torch.nn as nn

default_device = "cpu"  # 'cuda' if torch.cuda.is_available() else 'cpu'

def cli_args():
    import argparse

    parser = argparse.ArgumentParser(description="Your CLI description.")

    parser.add_argument(
        "--seed",
        type=int,
        default=1234, # set None for release
        help="Initialize torch seed"
    )
    parser.add_argument(
        "--prompt", type=str, default="Hello, my name is", help="Input prompt."
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Whether to launch in interactive mode",
    )
    parser.add_argument(
        "--tiktoken",
        action="store_true",
        help="Whether to use tiktoken tokenizer.",
    )
    parser.add_argument(
        "--export",
        action="store_true",
        help="Use torchat to export a model.",
    )
    parser.add_argument(
        "--generate",
        action="store_true",
        help="Use torchat to generate a sequence using a model.",
    )
    parser.add_argument(
        "--num-samples",
        type=int,
        default=5,
        help="Number of samples.")
    parser.add_argument(
        "--max-new-tokens",
        type=int,
        default=200,
        help="Maximum number of new tokens."
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=200,
        help="Top-k for sampling.")
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.8,
        help="Temperature for sampling."
    )
    parser.add_argument(
        "--compile",
        action="store_true",
        help="Whether to compile the model."
    )
    parser.add_argument(
        "--compile-prefill",
        action="store_true",
        help="Whether to compile the prefill (improves prefill perf, but higher compile times)",
    )
    parser.add_argument(
        "--profile",
        type=Path,
        default=None,
        help="Profile path."
    )
    parser.add_argument(
        "--speculate-k",
        type=int,
        default=5,
        help="Speculative execution depth."
    )
    parser.add_argument(
        "--draft-checkpoint-path",
        type=Path,
        default=None,
        help="Draft checkpoint path.",
    )
    parser.add_argument(
        "--checkpoint-path",
        type=Path,
        default="not_specified",
        help="Model checkpoint path.",
    )
    parser.add_argument(
        "--checkpoint-dir",
        type=Path,
        default=None,
        help="Model checkpoint directory.",
    )
    parser.add_argument(
        "--params-path",
        type=Path,
        default=None,
        help="Parameter file path.",
    )
    parser.add_argument(
        "--tokenizer-path",
        type=Path,
        default=None,
        help="Model checkpoint path.",
    )    
    parser.add_argument(
        "--output-pte-path",
        type=str,
        default=None,
        help="Filename"
    )
    parser.add_argument(
        "--output-dso-path",
        type=str,
        default=None,
        help="Filename"
    )
    parser.add_argument(
        "--dso-path",
        type=Path,
        default=None,
        help="Use the specified AOTI DSO model."
    )
    parser.add_argument(
        "--pte-path",
        type=Path,
        default=None,
        help="Use the specified Executorch PTE model."
    )    
    parser.add_argument(
        "-d",
        "--dtype",
        default="float32",
        help="Override the dtype of the model (default is the checkpoint dtype). Options: bf16, fp16, fp32",
    )
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(
        "--quantize",
        type=str,
        default="{ }",
        help="Quantization options."
    )
    parser.add_argument(
        "--device",
        type=str,
        default=default_device,
        help="Device to use"
    )

    args = parser.parse_args()

    if args.seed:
              torch.manual_seed(args.seed)

    return args