#!/bin/bash

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

# Define the URLs for the checkpoints
BASE_URL="https://dl.fbaipublicfiles.com/segment_anything_2/072824/"
sam2_hiera_t_url="${BASE_URL}sam2_hiera_tiny.pt"
sam2_hiera_s_url="${BASE_URL}sam2_hiera_small.pt"
sam2_hiera_b_plus_url="${BASE_URL}sam2_hiera_base_plus.pt"
sam2_hiera_l_url="${BASE_URL}sam2_hiera_large.pt"

# Create models directory if it doesn't exist
mkdir -p ./models

# Check for input argument
if [ "$#" -eq 0 ]; then
    # No argument provided, download all checkpoints
    echo "Downloading sam2_hiera_tiny.pt checkpoint..."
    wget -P ./models $sam2_hiera_t_url || { echo "Failed to download checkpoint from $sam2_hiera_t_url"; exit 1; }

    echo "Downloading sam2_hiera_small.pt checkpoint..."
    wget -P ./models $sam2_hiera_s_url || { echo "Failed to download checkpoint from $sam2_hiera_s_url"; exit 1; }

    echo "Downloading sam2_hiera_base_plus.pt checkpoint..."
    wget -P ./models $sam2_hiera_b_plus_url || { echo "Failed to download checkpoint from $sam2_hiera_b_plus_url"; exit 1; }

    echo "Downloading sam2_hiera_large.pt checkpoint..."
    wget -P ./models $sam2_hiera_l_url || { echo "Failed to download checkpoint from $sam2_hiera_l_url"; exit 1; }

elif [ "$1" == "--tiny" ]; then
    echo "Downloading sam2_hiera_tiny.pt checkpoint..."
    wget -P ./models $sam2_hiera_t_url || { echo "Failed to download checkpoint from $sam2_hiera_t_url"; exit 1; }

elif [ "$1" == "--small" ]; then
    echo "Downloading sam2_hiera_small.pt checkpoint..."
    wget -P ./models $sam2_hiera_s_url || { echo "Failed to download checkpoint from $sam2_hiera_s_url"; exit 1; }

elif [ "$1" == "--base" ]; then
    echo "Downloading sam2_hiera_base_plus.pt checkpoint..."
    wget -P ./models $sam2_hiera_b_plus_url || { echo "Failed to download checkpoint from $sam2_hiera_b_plus_url"; exit 1; }

elif [ "$1" == "--large" ]; then
    echo "Downloading sam2_hiera_large.pt checkpoint..."
    wget -P ./models $sam2_hiera_l_url || { echo "Failed to download checkpoint from $sam2_hiera_l_url"; exit 1; }

else
    echo "Invalid argument. Use --tiny, --small, --base, --large, or no argument to download all."
    exit 1
fi

echo "Download completed."
