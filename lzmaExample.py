#basic example of using lzma compression algorithm
import lzma
file = open("2.FDB", "rb")
data = file.read()
obj = lzma.LZMAFile("output.xz", mode="wb")
obj.write(data)
