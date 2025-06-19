class TreeStructure:


  def __init__(self, data):
        self.data  = data
        self.children = list()

  def add_child(self,child):
        self.children.append(child)

  def default_argument (self, name="Carlo"):
      print(name)

if __name__ == '__main__':

      print(3/5)
      comphrenshion_dictionary = {x: "" for x in range(0,19)}
      for i in range(10):
            if i % 2:
                  continue
            if i // 4 == 1:
                  break
            print(i)
      wipe_out=  {"Germany","Usa"}
      wipe_out.remove("Germany")
      remove_itemn = wipe_out.pop()
      print(remove_itemn)
      list_number = [n for n in range(0,9)]
      list_names = ["Z","i","b","o","R","a","y"]
      print(list_names[0:5:2])
      values = "abcde"
      print(" ".join(values[1::2]))
      print(values)
      root = TreeStructure(1)
      root.default_argument("Yiheng Mao")
      child = TreeStructure(9)
      second_child = TreeStructure(12)
      root.add_child(child)