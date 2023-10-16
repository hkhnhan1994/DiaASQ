set -ex

export CUDA_VISIBLE_DEVICES=0

cd src

for SEED in 5 10 15 20 25
do
K=5
INFER_PATH=$K
CTRL_TOKEN=post
TASK=diaasq
OUT_DIR="../outputs/$TASK/top${K}_seed${SEED}"

mkdir -p $OUT_DIR


python main.py \
    --data_path "../data/" \
    --dataset "phone" \
    --model_name_or_path t5-base \
    --output_dir $OUT_DIR \
    --num_train_epochs 10 \
    --save_top_k 0 \
    --task $TASK \
    --top_k $K \
    --ctrl_token $CTRL_TOKEN \
    --num_path $INFER_PATH \
    --seed $SEED \
    --train_batch_size 4 \
    --gradient_accumulation_steps 3 \
    --learning_rate 1e-4 \
    --lowercase \
    --sort_label \
    --data_ratio 1.0 \
    --check_val_every_n_epoch 2  \
    --agg_strategy vote \
    --eval_batch_size 4 \
    --constrained_decode \
    --do_train \
    # > $OUT_DIR/train.log
    # --load_ckpt_name "best.ckpt" \
    # --load_path_cache \
    > $OUT_DIR/train.log 2>&1 | tee $OUT_DIR/train.log
done
