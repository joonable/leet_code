def sortedInsert(llist, data):
    head = curr = llist
    if data < curr.data:
        node = DoublyLinkedListNode(data)
        node.prev, node.next = None, curr
        curr.prev = node
        return node

    prev, curr = curr, curr.next
    while curr:
        if prev.data <= data < curr.data:
            node = DoublyLinkedListNode(data)
            node.prev, node.next = prev, curr
            prev.next = node
            curr.prev = node
            return head
        prev, curr = curr, curr.next

    node = DoublyLinkedListNode(data)
    node.prev = prev
    prev.next = node
    return head