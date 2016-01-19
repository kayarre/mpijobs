#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

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
