# Evaluation: iteration-1
:::{note}
This jupyter book is a work in progress. This page will shortly be extended.
:::

The results for the second training iteration (iteration 1) are summarized below.  
For all experimental setups/video types, a few test and training frames are pictured in the following tables.

:::{note}
Labeling results are depicted acording to this scheme:  
“+”: Original markers set by the human scorer,  
“x” : Markers computed by the model, label accuracy < …% ,  
“dot”: Markers computed by the model, label accuracy > …
:::

The frames were trimmed, focusing on the pigeon, and excluding the experimental surrounding.

## StopSignalParadigm
<!---TABLE--->

## ImagingSkinnerbox
<!---TABLE--->

## HexagonalArena
<!---TABLE--->

## Statistics
The formal evaluation results are summarized in the table below:

|                    |                              |     ResNet_50    |     ResNet_101    |     ResNet_152    |
|--------------------|------------------------------|------------------|-------------------|-------------------|
|     Iteration 0    |     training   iterations    |                  |     1030000       |     1030000       |
|                    |     training   dataset       |                  |     95            |     95            |
|                    |     train   error            |                  |     1.12          |     1.04          |
|                    |     test   error             |                  |     38.11         |     18.74         |
|                    |     p-cutoff   used          |                  |     0.3           |     0.3           |
|     Iteration 1    |     training   iterations    |                  |     2000000       |     2000000       |
|                    |     training   dataset       |                  |     95            |     95            |
|                    |     train error              |                  |     2.81          |     2.07          |
|                    |     test   error             |                  |     13.26         |     17.72         |
|                    |     p-cutoff   used          |                  |     0.3           |     0.3           |

Notably, the training error has increased for both, ResNet101 and ResNet152 when evaluation results are compared to the respective results of training iteration 0. Concurrently, the test error has decreased for both models.