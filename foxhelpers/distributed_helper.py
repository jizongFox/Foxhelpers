import os
from dataclasses import dataclass

from torch import distributed as dist


def is_distributed() -> bool:
    try:
        return dist.is_initialized()
    except:
        return False


@dataclass
class DistributedEnv:
    is_distributed: bool = is_distributed()
    local_rank: int = os.environ.get("LOCAL_RANK", 0)
    word_size: int = os.environ.get("WORLD_SIZE", 1)

    @property
    def on_master(self) -> bool:
        if is_distributed():
            return self.local_rank == 0
        return True

    def barrier(self) -> None:
        if self.is_distributed:
            dist.barrier()

    def ipdb_set_trace(self):
        import ipdb