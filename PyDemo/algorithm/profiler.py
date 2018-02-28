# encoding: utf-8

"""
File: profiler.py
Author: Rock Johnson

Defines a class for profiling sort algorithms.
A Profiler object tracks the list, the number of comparisons
and exchanges, and the running time. The Profiler can also
print a trace and can create a list of unique or duplicate
numbers.

Example use:

from profiler import Profiler

p = Profiler()
p.test(selectionSort, size = 15, comp = True,
       exch = True, trace = True)
"""
import datetime
import random

class Profiler(object):

    def test(self, function, lyst = None, size = 10,
             unique = True, comp = True, exch = True,
             trace = False):
        """
        :param function: the algorithm being profiled
        :param target: the search target if profiling a search
        :param lyst: allows the caller to use her list
        :param size: the size of the list, 10 by default
        :param unique: if True, list contains unique integers
        :param comp: if True, count comparisons
        :param exch: if True, count exchanges
        :param trace: if True, print the list after each exchange

        Run the function with the given attributes and print
        its profile results.
        """
        self._comp = comp
        self._exch = exch
        self._trace = trace
        if lyst != None:
            self._lyst = lyst
        elif unique:
            self._lyst = [i for i in range(1, size + 1)]
            random.shuffle(self._lyst)
        else:
            self._lyst = []
            for count in range(size):
                self._lyst.append(random.randint(1, size))
        self._exchCount = 0
        self._cmpCount = 0
        self._startClock()
        function(self._lyst)
        self._stopClock()
        print(self)

    def exchange(self):
        """Counts exchanges if on."""
        if self._exch:
            self._exchCount += 1
        if self._trace:
            print(self._lyst)

    def comparison(self):
        """Counts comparisons if on."""
        if self._comp:
            self._cmpCount += 1

    def _startClock(self):
        """Record the starting time."""
        self._start = datetime.datetime.now()

    def _stopClock(self):
        """Stops the clock and computes the elapsed time
        in seconds, to the nearest millisecond."""
        self._elapsedTime = (datetime.datetime.now() - self._start).microseconds

    def __str__(self):
        """Returns the results as a string."""
        result = "Problem size: "
        result += str(len(self._lyst)) + "\n"
        result += "Elapsed time: "
        result += str(self._elapsedTime) + "\n"
        if self._comp:
            result += "Comparisons: "
            result += str(self._cmpCount) + "\n"
        if self._exch:
            result += "Exchanges: "
            result += str(self._exchCount) + "\n"
        return result