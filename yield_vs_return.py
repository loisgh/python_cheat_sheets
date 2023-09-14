'''
Yield is a keyword in Python that is used in conjunction with generator functions.
It allows you to produce a series of values for iteration without having to construct
an entire sequence (like a list) ahead of time, which can be a big advantage in terms
of memory usage and performance. Here's a deeper dive:

Basic Concepts:
Generator Functions vs Normal Functions: A normal function in Python uses the return
statement to send back a value immediately and terminate its execution. In contrast,
a generator function uses yield, which means the function can be resumed from where
it left off.

Lazy Evaluation: Generators allow for lazy evaluation. This means values are produced
one at a time and only when requested, as opposed to producing all values upfront and
storing them in memory.

State Preservation: Once a generator function hits yield, it retains its current state
(including local variables) and goes into a suspended mode. When called next, execution
resumes immediately after where the yield was previously encountered.


Benefits of Using yield:
Memory Efficiency: Generators are memory-efficient because they produce values on-the-fly
and do not need to store them in memory. This is especially useful when working with large
datasets.

On-the-Fly Computation: Generators can be used to represent infinite sequences. For example,
a generator could produce an infinite sequence of Fibonacci numbers, computing each number
as it's requested.

Pipeline Processing: Generators can be used in a pipeline fashion. For example, you could
have one generator that reads from a file, another that processes data, and another that
writes data, all working in a lazy, step-by-step manner.

Important Notes:
One-time Use: A generator is an iterator and can only be traversed once. Once all values
have been produced by the generator and it's exhausted, you'll need to create a new generator
instance to iterate over it again.

Generator Expressions: Python also supports generator expressions, which are a concise way
to create simple generators. They look like list comprehensions but use () instead of [].
For example: (x*2 for x in range(5)) produces values 0, 2, 4, 6, 8 on-the-fly.

In summary, yield facilitates the creation of generators in Python, enabling lazy evaluation,
memory-efficient iteration, and powerful data processing patterns.

For more information:
https://www.scaler.com/topics/python-yield-vs-return/
'''




