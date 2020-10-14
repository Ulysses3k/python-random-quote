import sys

def primary():
  f = open("quotes.txt", "a")
  f.write(sys.argv[1])
  f.write("\n")
  
  f.close()

if __name__== "__main__":
  primary()
