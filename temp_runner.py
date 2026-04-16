import subprocess
import os

# Run with NO_CODE_ANALYSIS build
code = subprocess.run([
    'cmake', '..',
    '-DCMAKE_BUILD_TYPE=Release',
    '-DNO_CODE_ANALYSIS=1'
], cwd='build/blutter_dartvm3.10.0_android_arm64').returncode

if code != 0:
    print("Cmake failed")
    exit(1)

code = subprocess.run(['ninja'], cwd='build/blutter_dartvm3.10.0_android_arm64').returncode
if code != 0:
    print("Build failed")
    exit(1)

code = subprocess.run([
    './bin/blutter_dartvm3.10.0_android_arm64',
    '-i', './extracted/lib/arm64-v8a/libapp.so',
    '-o', 'output_test'
]).returncode

print(f"Execution finished with code: {code}")
