from collections import deque

class node:
  def __init__(self,val):
      self.l = None
      self.r = None
      self.v = val
      self.color = 0
      self.d = 0
      
class tree:
  def __init__(self):
      self.root = None
      self.l = None
      self.r = None
      self.h = 0
      
  def fromlist(self, alist):
      for i in alist:
          self.add_val(i)
          
  def get_root(self):
      return self.root

  def add_val(self, val):
      root = self.get_root()
        
      # Create a root if there is no root
      if not root:
          root = node(val)
          self.root = root
          self.root.color = 0
      else:
          parent = root
          
          while(root):
            parent = root
            if val <= root.v:
                root = root.l
            else:
                root = root.r
          if val <= parent.v:
              parent.l = node(val)
          else:
              parent.r = node(val)
              
  def search(self,val):
      root = self.get_root()
      parent = None
      branch = None # left or right
      print "\nsearch path to ", val, ":",
      while root:
         print root.v,
         
         if val == root.v:
             print '\n'    
             return parent, branch, root
          
         elif val <= root.v:
             print 'left',
             parent = root
             root = root.l
             branch = 'l'
             if not root:
                 print 'not found'
                 return
             
         elif val >= root.v:
             print 'right',
             parent = root 
             root = root.r
             branch = 'r'
             if not root:
                 print 'not found'
                 return
      
      return None

  # Find the height of a (sub)tree (DFS)
  # This function changes node.h on its way.
  # When this is not desired, use find_height_recursion
  def find_height(self,root):
      height  = 0
      stack = list() # use list() to simulate a queue
      stack.append(root)
      root.h = 0
      while(len(stack)>0):
          node = stack.pop()
          if node.l or node.r:
              if node.l:
                  node.l.h = node.h + 1
                  stack.append(node.l)
              if node.r:
                  node.r.h = node.h + 1
                  stack.append(node.r)
          else: # when a leaf is reached
              height = max(height, node.h)
      return height
  
  def find_height_recursion(self, root, height):
        height_l = height # The two lines prevent errors when left or right
        height_r = height # branch is missing
        if root.l:
            height_l = self.find_height_recursion(root.l, height+1)
            # Increment in height if a new branch is found.
            # The height is incremented only in stack
        if root.r:
            height_r = self.find_height_recursion(root.r, height+1)
     
        return max(height_l, height_r)
      
  # Traverse a tree (BFS)
  def traverse_and_print(self):
      root = self.get_root()
      queue = deque() # list() is not good for simulating the a queue
      layer = dict()
      ith = 0
      at_color = 0
      layer[0] = []
      if root:
          queue.append(root)
          root.color = 0
      else:
          return None
      
      print "Traverse the tree",
      while len(queue)>0:
         node = queue.popleft()
         if at_color != node.color:
             ith +=1
             at_color = node.color
             layer[ith]= []
         layer[ith].append(node.v)
         print node.v, 
         if node.l:
             node.l.color = not node.color
             queue.append(node.l)
            
         if node.r:
             node.r.color = not node.color
             queue.append(node.r)
      return layer

  def find_first_imbalanced_node(self):
      depth = min(depth,node.h)
      # tbd
      
def right_rotate(z):
    """
            z                  x
           / \               /   \
          x  T4             y     z   
         / \        -->    / \   / \
        y  T3             T1 T2 T3  T4 
       / \
      T1 T2

    """
    x = z.l
    tmp = x.r  
    x.r = z
    z.l = tmp
    return x


def left_rotate(z):
    """
            z                  x
           / \               /   \
         T1   x             z     y   
             / \       --> / \   / \
            T2  y         T1 T2 T3  T4 
               / \
              T3 T4

     """
    x = z.r
    tmp = x.l  
    x.l = z
    z.r = tmp
    return x








