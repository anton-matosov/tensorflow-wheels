

# total images/sec: 16.04

```
python tf_cnn_benchmarks.py --forward_only=True --device=cpu --mkl=True \                                                              (mkl_tflow) 
                                                                               --kmp_blocktime=0 --nodistortions --model=resnet50 --data_format=NCHW \
                                                                               --batch_size=32 --num_inter_threads=1 --num_intra_threads=4
TensorFlow:  1.5
Model:       resnet50
Dataset:     imagenet (synthetic)
Mode:        forward-only
SingleSess:  False
Batch size:  32 global
             32.0 per device
Num batches: 100
Num epochs:  0.00
Devices:     ['/cpu:0']
Data format: NCHW
Layout optimizer: False
Optimizer:   sgd
Variables:   parameter_server
==========
Generating model
W0227 17:04:37.464618 140735494935360 tf_logging.py:118] From /Users/antonmatosov/Develop/MachineLearning/benchmarks/scripts/tf_cnn_benchmarks/convnet_builder.py:372: calling reduce_mean (from tensorflow.python.ops.math_ops) with keep_dims is deprecated and will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead
W0227 17:04:38.130288 140735494935360 tf_logging.py:118] From /Users/antonmatosov/Develop/MachineLearning/benchmarks/scripts/tf_cnn_benchmarks/benchmark_cnn.py:1356: Supervisor.__init__ (from tensorflow.python.training.supervisor) is deprecated and will be removed in a future version.
Instructions for updating:
Please switch to tf.train.MonitoredTrainingSession
Running warm up

User settings:

   KMP_AFFINITY=granularity=fine,verbose,compact,1,0
   KMP_BLOCKTIME=0
   KMP_SETTINGS=1
   OMP_NUM_THREADS=4

Effective settings:

   KMP_ABORT_DELAY=0
   KMP_ADAPTIVE_LOCK_PROPS='1,1024'
   KMP_ALIGN_ALLOC=64
   KMP_ALL_THREADPRIVATE=128
   KMP_ATOMIC_MODE=2
   KMP_BLOCKTIME=0
   KMP_DETERMINISTIC_REDUCTION=false
   KMP_DEVICE_THREAD_LIMIT=2147483647
   KMP_DISP_NUM_BUFFERS=7
   KMP_DUPLICATE_LIB_OK=false
   KMP_FORCE_REDUCTION: value is not defined
   KMP_FOREIGN_THREADS_THREADPRIVATE=true
   KMP_FORKJOIN_BARRIER='2,2'
   KMP_FORKJOIN_BARRIER_PATTERN='hyper,hyper'
   KMP_FORKJOIN_FRAMES=true
   KMP_FORKJOIN_FRAMES_MODE=3
   KMP_GTID_MODE=0
   KMP_HANDLE_SIGNALS=false
   KMP_HOT_TEAMS_MAX_LEVEL=1
   KMP_HOT_TEAMS_MODE=0
   KMP_INIT_AT_FORK=true
   KMP_INIT_WAIT=2048
   KMP_ITT_PREPARE_DELAY=0
   KMP_LIBRARY=throughput
   KMP_LOCK_KIND=queuing
   KMP_MALLOC_POOL_INCR=1M
   KMP_NEXT_WAIT=1024
   KMP_NUM_LOCKS_IN_BLOCK=1
   KMP_PLAIN_BARRIER='2,2'
   KMP_PLAIN_BARRIER_PATTERN='hyper,hyper'
   KMP_REDUCTION_BARRIER='1,1'
   KMP_REDUCTION_BARRIER_PATTERN='hyper,hyper'
   KMP_SCHEDULE='static,balanced;guided,iterative'
   KMP_SETTINGS=true
   KMP_SPIN_BACKOFF_PARAMS='4096,100'
   KMP_STACKOFFSET=0
   KMP_STACKPAD=0
   KMP_STACKSIZE=4M
   KMP_STORAGE_MAP=false
   KMP_TASKING=2
   KMP_TASKLOOP_MIN_TASKS=0
   KMP_TASK_STEALING_CONSTRAINT=1
   KMP_TEAMS_THREAD_LIMIT=8
   KMP_VERSION=false
   KMP_WARNINGS=true
   OMP_CANCELLATION=false
   OMP_DEFAULT_DEVICE=0
   OMP_DISPLAY_ENV=false
   OMP_DYNAMIC=false
   OMP_MAX_ACTIVE_LEVELS=2147483647
   OMP_MAX_TASK_PRIORITY=0
   OMP_NESTED=false
   OMP_NUM_THREADS='4'
   OMP_PROC_BIND='false'
   OMP_SCHEDULE='static'
   OMP_STACKSIZE=4M
   OMP_THREAD_LIMIT=2147483647
   OMP_WAIT_POLICY=PASSIVE

I0227 17:05:00.380208 123145543434240 tf_logging.py:110] Starting real work at step 10 at time Tue Feb 27 17:05:00 2018
Done warm up
Step	Img/sec	total_loss	top_1_accuracy	top_5_accuracy
1	images/sec: 16.1 +/- 0.0 (jitter = 0.0)	0.000	0.000	0.000
10	images/sec: 16.3 +/- 0.1 (jitter = 0.3)	0.000	0.000	0.000
20	images/sec: 16.1 +/- 0.1 (jitter = 0.6)	0.000	0.000	0.000
30	images/sec: 16.1 +/- 0.1 (jitter = 0.6)	0.000	0.000	0.000
40	images/sec: 16.2 +/- 0.1 (jitter = 0.3)	0.000	0.000	0.000
50	images/sec: 16.3 +/- 0.1 (jitter = 0.4)	0.000	0.000	0.031
60	images/sec: 16.3 +/- 0.1 (jitter = 0.3)	0.000	0.000	0.000
70	images/sec: 16.2 +/- 0.1 (jitter = 0.3)	0.000	0.000	0.000
80	images/sec: 16.1 +/- 0.1 (jitter = 0.4)	0.000	0.000	0.000
90	images/sec: 16.2 +/- 0.1 (jitter = 0.5)	0.000	0.000	0.000
I0227 17:08:17.842580 123145543434240 tf_logging.py:110] Finishing real work at step 109 at time Tue Feb 27 17:08:17 2018
----------------------------------------------------------------
total images/sec: 16.04
----------------------------------------------------------------
```