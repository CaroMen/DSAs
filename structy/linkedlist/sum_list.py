"""
    Description:
      Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

    Thought:
      we have to iterate through the linked list
      create a variable that starts at 0 and a variable to store head
      loop while head variable is not None and increment the sum variable by the head.val

"""

def sum_list(head):
  final_sum = 0
  current = head

  while current is not None:
    final_sum += current.val
    current = current.next

  return final_sum
