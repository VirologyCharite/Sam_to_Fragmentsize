# Sam_to_Fragmentsize

## Summary
`fragsize.py` takes a modified samfile and gives out the ID of each pair of reads and the length of the fragment they originate from. `sum.py` takes this output and plots it in a historgram, giving the mean, the standard deviation, the maximum and the minimun fragmentlength.

## Reasoning
This is being done in order to judge if the laboratory steps can be optimised, in particular fragmentation and size exclusion.

## Fragsize.py
- Samfiles of paired end reads mapped to a reference have to be given to this program. All IDs where only one of the two paired end reads map are being ignored.
