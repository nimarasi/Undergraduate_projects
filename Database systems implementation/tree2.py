import math

global t


class Node:
    def __init__(self, keys=[]):
        self.items = keys

    def add(self, key):
        nodes_count = len([item for item in self.items if isinstance(item, Node)])
        if nodes_count == 0:
            self.items.append(key)
            self.items.sort()
        else:
            # loop on all indexs of self.items
            for i in range(len(self.items)):
                # if find key
                if not isinstance(self.items[i], Node):
                    # if new key that we want to insert is < self.items key
                    if key < self.items[i]:
                        # insert new key to left node of this self.items key
                        # if dont have overflow in that node result == None else we have overflowed keys
                        result = self.items[i - 1].add(key)
                        if result:# if overflow
                            self.items.insert(i, result[0]) # first element of result insert to self.items[i]
                            self.items.insert(i + 1, Node(result[1:])) # result[1:] insert to self.items[i+1] as node
                        break

                # if we arrive to end of self.items
                if i == len(self.items) - 1:
                    # add this key to last index of self.items which is node
                    # if overflow result != None
                    result = self.items[i].add(key)
                    if result:
                        self.items.append(result[0])
                        self.items.append(Node(result[1:]))
                    break
        # check overflow in self.items
        keys_count = len([item for item in self.items if not isinstance(item, Node)])
        if keys_count > 2 * t - 1:
            mid = math.ceil(len(self.items) / 2)
            result = self.items[mid:]
            self.items = self.items[:mid]
            return result
        else:
            return None

    def __str__(self):
        output = []
        for item in self.items:
            if isinstance(item, Node):
                output.append(item.__str__())
            else:
                output.append(str(item))
        return "{ " + " , ".join(output) + " }"


def add_key(root, key):
    """
    it only checks overflow of root node
    """
    result = root.add(key) # if result == None we dont have overflow else we have overflow and we put overflowed keys in result
    if result:
        new_root = Node([root, result[0], Node(result[1:])])
        return new_root
    else:
        return root


def main():
    global t

    keys = [5, 3, 21, 9, 1, 13, 2, 7, 10, 12, 4, 8]
    # keys = ['a','b','c','d','e','f','g','h']
    root = Node()
    t = 2

    for key in keys:
        print(f'Add {key}')
        root = add_key(root,key)
        print(root)
        print('\n')


if __name__ == '__main__':
    main()
