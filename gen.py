import types
import lightweight_gan.cli as c
import sys

argvs = {"cpu":True, "--name":"face", "--num-image-tiles":1,"--results_dir": './results',"--image_size":256}

if len(sys.argv) > 1:  # コマンドライン引数が存在すれば
    args_list = sys.argv[1:]  # ":"が重要．リスト作成
    keys = args_list[0::2]  # 偶数インデックスをkeyに
    vals = args_list[1::2]  # 奇数インデックスを値に
    argvs_cmd = dict(zip(keys, vals))  # コマンドライン引数辞書の作成
    for key in argvs_cmd.keys():  # コマンドライン引数辞書のkeyのループ
        if key in argvs:  # keyが元の辞書に存在したら
            argvs[key] = argvs_cmd[key]  # 辞書のデフォルト値を書き換える

c.train_from_folder(cpu = argvs["cpu"],name =argvs["--name"],generate=True,num_image_tiles=int(argvs["--num-image-tiles"]),
generate_types =['default'],results_dir=argvs["--results_dir"],image_size = int(argvs["--image_size"]))

#c.train_from_folder(generate=True,cpu = True,name="face")
