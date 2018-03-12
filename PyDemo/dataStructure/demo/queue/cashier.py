# encoding: utf-8

"""
File: cashier.py
Author: Rock Johnson
"""
from dataStructure.linkeds.linkedqueue import LinkedQueue

class Cashier(object):
    """收银员对象"""

    def __init__(self):
        self._totalCustomerWaitTime = 0
        self._customerServed = 0
        self._currentCustomer = None
        self._queue = LinkedQueue()

    def addCustomer(self, c):
        self._queue.add(c)

    def serveCustomers(self, currentTime):
        if self._currentCustomer is None:
            # No Customers yet
            if self._queue.isEmpty():
                return
            else:
                # Pop first waiting customer
                # and tally results
                self._currentCustomer = self._queue.pop()
                self._totalCustomerWaitTime += currentTime \
                    - self._currentCustomer.arrivalTime()
        # Give a unit of service
        self._currentCustomer.serve()

        # If current customer is finished, send it away
        if self._currentCustomer.amountOfServiceNeeded() == 0:
            self._currentCustomer = None

    def __str__(self):
        result = "Total for the cashier\n" + \
                 "Number of customers served: " + \
                 str(self._customerServed) + "\n"
        if self._customerServed != 0:
            aveWaitTime = self._totalCustomerWaitTime / \
                          self._customerServed
            result += "Number of customers left in queue: " \
                      + str(len(self._queue)) + "\n" \
                      + "Average time customers spend\n" \
                      + "waiting to be served: "\
                      + "%5.2f" % aveWaitTime
        return result