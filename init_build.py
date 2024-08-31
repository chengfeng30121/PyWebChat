import os

os.makedirs("/home/runner/.buildozer/android/platform/android-sdk/licenses/", exist_ok=True)

with open("/home/runner/.buildozer/android/platform/android-sdk/licenses/android-sdk-license", "w") as f:
    f.write("\n24333f8a63b6825ea9c5514f83c2829b004d1fee")