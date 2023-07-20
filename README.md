# sd_training_config

Just a toml file to be used for [kohya-ss/sd-scripts](https://github.com/kohya-ss/sd-scripts/) and [KohakuBlueleaf/LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS)

Please follow the proper instructions to set up `sd-scripts` and run `pip install lycoris_lora` to install LyCORIS

Then all you need to do is to modify the `XXX.toml` file and run

```
python train_network.py --config_file XXX.toml
```

You can do sequential training by putting `sequntial_train.py` in the `sd_scripts` directory and run

```
python sequential_train.py --script_name train_network.py --dir_path /path/to/config_directory

```


### Why did I make this?

There were several repositories that implemented scripts that facilitate the use of `kohya-ss/sd-scripts` before but unfortunately (at least for me) all of them, as far as I know, move to work on gui

Luckily, in the meanwhile, the support for `toml` file is added in `sd-scripts`

The only problem is that the arugments that can be used remain pretty obscure (the best way to get all of them seems to be the old-fashion `--help`), so I think it would be helpful to list all of them in a single file where things can be modified directly
