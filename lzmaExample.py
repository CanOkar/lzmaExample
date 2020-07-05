#basic example of using lzma compression algorithm
import lzma
file = open("file_name.extension", "rb")
data = file.read()
obj = lzma.LZMAFile("output.xz", mode="wb")
obj.write(data)
