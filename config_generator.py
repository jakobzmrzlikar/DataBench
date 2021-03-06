import json

def generate(dataset):
    with open("config/master/"+dataset+".json", 'r') as f:
        meta = json.load(f)
    with open("encoding.json", 'r') as f:
        encoding = json.load(f)

    hyperparams = meta["model"]["hyperparameters"]
    build = hyperparams["build"]
    fit = hyperparams["fit"]
    arch = meta["model"]["architecture"]
    epch = [10, 20, 50, 100]
    acti = ["relu", "sigmoid", "hard_sigmoid", "tanh"]

    idx = 0
    for m in range(4):
        arch["Activation"][0] = acti[m]
        for n in encoding["optimizer"]:
            build["optimizer"] = n
            for k in range(4):
                arch["Dense"][0] = 2**(k+5)
                for i in range(4):
                    fit["epochs"] = epch[i]
                    for j in range(4):
                        fit["batch_size"] = 2**(j+4)
                        idx+=1
                        name = "config/generated/"+dataset+'_'+str(idx)+".json"
                        with open(name, 'w') as f:
                            json.dump(meta, f, ensure_ascii=False, indent=2, sort_keys=True)
