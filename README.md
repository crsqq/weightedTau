weightedTau
===========

A weighted version of Kendall's Tau as described in: Sebastiano Vigna. A
weighted correlation index for rankings with ties. CoRR, abs/1404.3325, 2014. 

Note: This is a naive implementation with O(n^2). The performance is reasonable
for small datasets (~10000 entries).

There is no documentation / tests yet and there wont be until someone ask me
for it.

## Installation
```
git clone https://github.com/crsqq/weightedTau
cd weightedTau
make shared
cd ..
```

## Usage

```
from weightedTau.weightedTau import weightedTau
weightedTau(x, y)
```
Where `x, y` are two rank vectors of the same length.

