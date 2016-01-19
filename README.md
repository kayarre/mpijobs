# Mpijobs

A Python3 library for running many jobs on multiple processes, using
MPI.

## Example

The following example runs 3 jobs. For each of them, a message is
printed on the screen.

`````python
from mpi4py import MPI
import mpijobs

class MyJob(mpijobs.Job):
    def __init__(self,
                 local_params,
                 status=mpijobs.JobStatus.queued,
                 running_time=None):
        super().__init__(status, running_time)
        self.params = local_params

    def run(self, rank):
        print("Hi, I am {0} (process {1})".format(self.params, rank))

job_list = [MyJob(name) for name in ('Bob', 'Alice', 'Stephen')]
mpijobs.run_event_loop(MPI.COMM_WORLD, job_list)
`````

The program must be run using ``mpirun`` (or an equivalent program,
depending on your MPI library):

    mpirun -n 3 python3 example.py

The output is the following (actual ranks might vary):

    Hi, I am Stephen (process 1)
    Hi, I am Alice (process 2)
    Hi, I am Bob (process 1)

## Copyright

See the COPYRIGHT.md file.
