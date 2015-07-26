We've asked two robots to help us simulate this situation:
Achilleborg (A1 -- fast agile prototype) and Tortoimenator (T2 -- heavy slow cyborg).

A1 is faster than T2, so it has a **X** seconds head start on A1.
For **X** seconds T2 will move at **t2_speed\*X** metres.
So A1 must first reach the point whence T2 already reached.
But T2 is moving and next step for A1 is to reach the next point and so on to infinity.
The paradox is correct in theory,
but in practice A1 easily outruns T2. Hm... maybe we can calculate when A1 will catch up to T2.

```
T2 - 3m/s
A1 - 6m/s

2s
|------------> T2 - 6m
|> A1 - 0m

3s
|------------------> T2 - 9m
|------------> A1 - 6m

3.5s
|---------------------> T2 - 10.5m
|------------------> A1 - 9m
```

You are given A1 and T2’s speed in m/s as well as the length of the advantage T2 has in seconds.
Try to count the time when from when A1 come abreast with T2 (count from T2 start).
The result should be given in seconds with precious &plusmn;10<sup>-8</sup>.
