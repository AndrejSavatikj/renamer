import os

folder = "./Downloads/T2122_AprilFools_Program_v4d-images"
dstFolder = "./Downloads/Renamed"

# files =
# print(files)
for count, filename in enumerate(sorted(os.listdir(folder))):
    print(count, filename)
    index = count + 1
    if index < 10:
        dst = f"information_0{str(index)}.jpg"

    else:
        dst = f"information_{str(index)}.jpg"

    src = f"{folder}/{filename}"
    dst = f"{dstFolder}/{dst}"

    os.rename(src, dst)

print("done")
