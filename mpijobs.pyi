# -*- mode: python3 -*-
# -*- encoding: utf-8 -*-

from enum import Enum
from typing import Any, List, Callable

class JobStatus(Enum):
    finished = 1
    running = 2
    queued = 3

class Job:
    def __init__(self,
                 status: int=JobStatus.queued,
                 running_time: Any = None) -> None: ...
    def __repr__(self) -> str: ...
    def run(self, rank: int) -> None: ...

def run_event_loop(comm: Any,
                   job_list: List[Job],
                   master_rank: int = 0,
                   log_flag: bool = False,
                   callback: Callable[[List[Job], List[Job]], None] = None) -> List[Job]: ...
