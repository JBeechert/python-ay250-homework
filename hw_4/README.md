## hw_4 README

If our primary metric of "advantage" vs. "disadvantage" is the execution time, it is clear that using dask for fewer than at least $\sim10^6$ darts is a disadvantage. Perhaps dask unnecesarily complicates the task at hand below a certain array size and slows the execution. Dask must only be advantageous when dealing with *very* large arrays.

For more than $\sim400$ darts, the concurrent.futures method performs best. It executes much faster than the simple method and only faces competition from dask at $>10^6$ darts. Even then, the distinction between the two appears inconsequential.

For fewer than $\sim400$ darts, the simple case has fastest execution times. Perhaps this makes sense- for a simple dart toss, keep the method simple. Maybe forking multiple processes for relatively few darts is more trouble than it's worth. 

In terms of simulation rate, the concurrent.futures method runs more quickly than the simple and dask methods above $\sim400$ darts. Again, for less than $\sim400$ darts, it seems best to stick with the simple calculation.
