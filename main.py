from foxhelpers.distributed_helper import  DistributedEnv

DistributedEnv().ipdb_set_trace()
print(DistributedEnv().local_rank)