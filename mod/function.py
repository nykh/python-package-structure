from util.Foo import Foo

def get_foo():
    return Foo()

if __name__ == "__main__":
  print("Running as package!")
  
  foo = Foo()
