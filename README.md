# Min-transfers-algo
The Min-Transfers Problem is a famous real world problem which involes finding the most optimal routes such that the number of vehicle transffers(switching in between different vehicles) is minimized.

This project aims to write fully fucntioning codes of atleast 3 of the 5 suggested algorithms that were given in the research paper and compare their effectiveness.



## Checkpoint 2 Update

- have  added a folder for **Checkpoint 2**, which includes:
  - The Latex source code of our technical summary report.
  - The PDF version of the report.
  - A similar folder for checkpoint 1 has also been created  (previously forgot to push the latex code for checkpoint1 report,but that is done now)
- We now have a better understanding of:
  - How TPP-graphs work.
  - The strengths and weaknesses of different algorithms for this problem.
- We aim to implement and test **at least 3 out of 5 algorithms** described in the paper.
- currently looking for datasets aswell,either using the one in the study or from somehwere else.

## Goals
- Look for potential datasets to test the algorithms on
- Implement multiple algorithms (Single Queue, No Queue, etc.) from the paper.
- Compare their speed and accuracy on real transportation data(if possible)

## CHECKPOINT 3 update
To generate the random datasets,run the following command
python generate_data.py

To run the Min-Transfers Algorithm on the generated datasets and compare the performance of the SQ, NQ, and MQ algorithms, run the following command:

python main.py

This will:

->Load the generated datasets (small, medium, and large samples).

->Run each algorithm (SQ, NQ, MQ) on each dataset.

->Output the minimum number of transfers and timing results for each source and dataset.

NOTE:The data folder has all the datasets,algortihms folder has all the algorithms that we wrote for this project