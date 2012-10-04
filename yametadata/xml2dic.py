from xml.dom.minidom import parseString

class NotTextNodeError:
    pass


def getTextFromNode(node):
    """
    scans through all children of node and gathers the
    text. if node has non-text child-nodes, then
    NotTextNodeError is raised.
    """
    t = ""
    for n in node.childNodes:
        if n.nodeType == n.TEXT_NODE:
            t += n.nodeValue
        else:
            raise NotTextNodeError
    return t


def nodeToDic(node):
    """
    nodeToDic() scans through the children of node and makes a
    dictionary from the content.
    three cases are differentiated:
    - if the node contains no other nodes, it is a text-node
    and {nodeName:text} is merged into the dictionary.
    - if there is more than one child with the same name
    then these children will be appended to a list and this
    list is merged to the dictionary in the form: {nodeName:list}.
    - else, nodeToDic() will call itself recursively on
    the nodes children (merging {nodeName:nodeToDic()} to
    the dictionary).
    """
    dic = {}
    multlist = {}  # holds temporary lists where there are multiple children
    if node.attributes:
        for key in node.attributes.keys():
            value = node.attributes[key]
            dic.update({key: getTextFromNode(value)})

    for n in node.childNodes:

        multiple = False
        if n.nodeType != n.ELEMENT_NODE:
            continue
        # find out if there are multiple records
        if len(node.getElementsByTagName(n.nodeName)) > 1:
            multiple = True
            # and set up the list to hold the values
            if n.nodeName not in multlist:
                multlist[n.nodeName] = []

        try:
            #text node
            text = getTextFromNode(n)
        except NotTextNodeError:
            if multiple:
                # append to our list
                multlist[n.nodeName].append(nodeToDic(n))
                dic.update({n.nodeName: multlist[n.nodeName]})
                continue
            else:
                # 'normal' node
                dic.update({n.nodeName: nodeToDic(n)})
                continue

        # text node
        if multiple:
            multlist[n.nodeName].append(text)
            dic.update({n.nodeName: multlist[n.nodeName]})
        else:
            dic.update({n.nodeName: text})

    return dic

def as_dict(content):
    return nodeToDic(parseString(content))