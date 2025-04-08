#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# Copyright (C) 2024 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_lib import lib_fixups

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

from extract_utils.fixups_blob import (
    blob_fixups_user_type,
    blob_fixup,
)
from extract_utils.module import lib_fixups_user_type

namespace_imports = [
    'hardware/qcom-caf/sm8450',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/sony/sm8450-common',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib64/vendor.somc.camera.device@3.2-impl.so', 'vendor/lib64/vendor.somc.camera.device@3.3-impl.so',
     'vendor/lib64/vendor.somc.camera.device@3.4-impl.so', 'vendor/lib64/vendor.somc.camera.device@3.5-impl.so',
     'vendor/bin/hw/vendor.somc.hardware.camera.provider@1.0-service'): blob_fixup()
	.replace_needed('libutils.so', 'libutils-v32.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'pdx223',
    'sony',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8450-common', module.vendor
    )
    utils.run()
