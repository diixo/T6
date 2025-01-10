import time
import os
from datetime import datetime

# Wandb configs
wandb_log = True
wandb_project = 'nanogpt-neo'

# Model configs
n_layer = 48
n_head = 49
head_dim = 64
q_lora_rank: int = 1024
qk_rope_head_dim: int = 32
kv_lora_rank: int = 512
v_head_dim: int = 64
n_embd = 1600
dropout = 0.0
bias = False
# Training configs
batch_size = 6
block_size = 1024
gradient_accumulation_steps = 60 // batch_size
max_iters = 100000
lr_decay_iters = 100000
eval_interval = 1000
eval_iters = 200
log_interval = 10

# Optimizer configs
optimizer_name = 'adamw'
learning_rate = 1e-4
weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.95
grad_clip = 1.0
decay_lr = True
warmup_iters = 2000
min_lr = 1e-5
schedule = 'cosine'

# System configs
compile = True
model_type = 'llama-mla'
