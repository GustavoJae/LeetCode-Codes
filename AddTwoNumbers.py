'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself'''
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # a ideia é aproveitar que as listas estao na ordem contraria para comecar a somar pelas
        # unidades, e carregando o carry até um algarismo maior

        # vamos criar um no dummy que representará o nó "atual" da resposta em que calculamos as somas
        dummy = ListNode()

        # aquis será o nó "head" da resposta
        res = dummy

        # iniciar os valores iniciais de carry e dos nos
        carry = total = 0
        curr1 = l1
        curr2 = l2

        # enquanto existir ou carry ou algum dos nos para somar
        while curr1 or curr2 or carry>0:

            # somamos os valores e atualizamos o no em que estamos
            total = carry
            if curr1:
                total += curr1.val
                curr1 = curr1.next
            if curr2:
                total += curr2.val
                curr2 = curr2.next

            # calcula qual é o numero que será guardado e o carry
            n = total % 10
            carry = total // 10

            # incrementa a nossa lista ligada
            dummy.next = ListNode(n)
            dummy = dummy.next
        # retorna o primeiro elemento da lista ligada
        return res.next