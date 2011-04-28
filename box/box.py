#!/usr/bin/env python
import sys
def parse(f):
    root = (1,[])
    stack = []
    stack.append(root)
    for line in f:
        line = line.strip()
        if line.isdigit():
            c = int(line)
            new_box = []
            p_c,parent_box = stack.pop()
            p_c -=1
            parent_box.append(new_box)
            if p_c > 0:
                stack.append((p_c,parent_box))
            stack.append((c,new_box))
        else:
            c,box = stack.pop()
            box.append(line)
            c -= 1
            if c > 0:
                stack.append((c,box))
    return root[1][0]
   
def find_width(node=None, depth=1):
    global root
    w = depth * 4
    if not node:
        node = root
    if isinstance(node,list):
        w_c = 0
        for child in node:
            if isinstance(child,list):
                w_c = max(w_c,find_width(child, depth+1))
            else:
                w_c = max(w_c,find_width(child, depth))
        w = max(w,w_c)
    else:
        w += len(node)
    return w

def print_boxes(node=None, offset=1):
    """ using inorder traversal"""
    global root, max_w
    if not node:
        node = root
    w = find_width(node, 1)

    print '| '*(offset-1) + '.' + '-' * (max_w-((offset-1)*4)-2) + '.' + ' |'*(offset-1)
    for child in node:
        if isinstance(child,list):
            print_boxes(child,offset+1)
        else:
            print '| '*offset + child + ' '*(max_w-len(child)-offset*4) + ' |'*offset
    print '| '*(offset-1) + "'" + '-' * (max_w-((offset-1)*4)-2) + "'" + ' |'*(offset-1)

root = parse(sys.stdin)
max_w = find_width(root)
print_boxes()