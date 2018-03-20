# encoding: utf-8

"""
File: marketmodel.py
Author: Rock Johnson
"""
from dataStructure.demo.queue.cashier import Cashier
from dataStructure.demo.queue.customer import Customer

class MarketModel(object):
    """超市模型"""

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival):
        self._probabilityOfNewArrival = probabilityOfNewArrival
        self._lengthOfSimulation = lengthOfSimulation
        self._averageTimePerCus = averageTimePerCus
        self._cashier = Cashier()

    def runSimulation(self):
        """Run the clock for n ticks."""
        for currentTime in range(self._lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self._probabilityOfNewArrival,
                currentTime,
                self._averageTimePerCus)

            # Send customer to cashier if successfully
            # generated
            if customer != None:
                self._cashier.addCustomer(customer)

            # Tell cashier to provide another unit of service
            self._cashier.serveCustomers(currentTime)

    def __str__(self):
        return str(self._cashier)