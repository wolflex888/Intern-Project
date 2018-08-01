# train
mkdir -pv model/$1
python3 train_r_mo2.py --model $1 --save_history_path log/$1 --model_type $2 \
    --hidden_size $3 --index $4 --loss_function $5 --batch_size 256 \
    --nb_epoch 200 --action train --save_dir model/ 
    
# test 
python3 train_r_mo2.py --action test --model $1 --load_model $1/ --test_y npy/$1.npy \
    --model_type $2 --hidden_size $3 --index $4 --loss_function $5  
