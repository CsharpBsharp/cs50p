def main():
    filename = input("Enter file name: ").strip().lower()
    fileext = find_extension(filename)
    mediatype = find_mediatype(fileext)
    print(mediatype)

def find_extension(filename=""):
    if "." in filename:
        return filename[filename.rindex("."):]
    return ""

def find_mediatype(fileext=""):
    mediatype = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip",
    }
    return mediatype.get(fileext, "application/octet-stream")

main()
