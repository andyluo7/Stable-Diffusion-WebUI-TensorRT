import launch
import sys

python = sys.executable

launch.run_pip("install importlib-metadata", "importlib-metadata")

from importlib_metadata import version

launch.run_pip("install onnx", "onnx")

# Polygraphy
launch.run_pip("install polygraphy", "polygraphy")

# ONNX GS
launch.run_pip("install onnx-graphsurgeon --extra-index-url https://pypi.ngc.nvidia.com","onnx-graphsurgeon")

# OPTIMUM
launch.run_pip("install optimum","optimum")

launch.run_pip("install --pre --extra-index-url https://pypi.nvidia.com tensorrt==9.0.1.post11.dev4 --no-cache-dir","tensorrt")
