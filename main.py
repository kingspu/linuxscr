def alterConfig(dir, oldConfig,newConfig):
    pass

def alterConfigs(dirs, oldConfigs,newConfigs):
    """First arg: list of file directories you wish to alter
     Second arg: list of config names (or list of list of config names if you want to edit multiple configs in one file) you wish to alter (be exact or your getting fried). Make sure index matches
     Third arg: new config including the argument ex. TRUE, (this can also be a list if you changed multiple in previous argument)"""

    i = 0
    for dir in dirs:
        editedConfigs = []
        with open(dir, "r+") as f:
            if f.writable() and f.readable():
                config = f.readlines()
                configcpy = config[:]
                print(config)
                for line in config:
                    if isinstance(oldConfigs[i], str):
                        if oldConfigs[i] in line:
                            configcpy.remove(line)

                    else:
                        for subConfig in oldConfigs[i]:
                            if subConfig in line and line in configcpy:
                                configcpy.remove(line)
                editedConfigs = configcpy
            elif (not f.writable()) and f.readable():
                print(f"WARNING!!! Directiory {dir} is not writeable!")
                continue
            elif (not f.readable()) and f.writable():
                print(f"WARNING!!! Directiory {dir} is not readable!")
                continue
            else:
                print(f"WARNING!!! Directiory {dir} is neither writable nor readable! Your COOKED 🤣🤣🤣 (or somethings wrong with my code)")
                continue


            if isinstance(newConfigs[i], str):
                newConfigs[i] = newConfigs[i]
                editedConfigs.append("\n")
                editedConfigs.append(newConfigs[i])
            else:
                editedConfigs.append("\n")
                editedConfigs += [x + "\n" for x in newConfigs[i]]
                editedConfigs[-1].replace("\n","")
            print(editedConfigs)
            f.seek(0)
            f.truncate()
            f.writelines(editedConfigs)
        i+=1

t = "TRUE"
f = "FALSE"
alterConfigs([r"C:\Users\danny.DESKTOP-GRB5QI1\OneDrive\Desktop\donfig.txt"],[["config1:","config2:"]],[["config1: 41","config2: 67"]])
#alterConfigs(["test.txt"],[["this is another config:", "this is a config:", "this is another different config:"]],[[f"this is another config: {f}",f"this is a config: {t}",f"this is another different config: {f}"]])
#alterConfigs(["test.txt","hello.txt"],["this is another another config:","this is a config"],["this is another another config: FALSE","this is a config: FALSE"])