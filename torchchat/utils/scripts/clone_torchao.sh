#!/bin/bash
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

source "$(dirname "${BASH_SOURCE[0]}")/install_utils.sh"

pushd ${TORCHCHAT_ROOT}
clone_torchao
popd
