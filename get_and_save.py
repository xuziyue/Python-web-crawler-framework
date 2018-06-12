import requests
import os

def save_graph(url: str, root: str, name: str) -> None:
    """Save the graph with address url at root with name.

    @param url: url of the graph we want to get
    @param root: the place to save pictures
    @param name: the name the graph will be saved as.
    """
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        # Create a path
        path = root + '/' + name

        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, "wb") as f:
                f.write(r.content)
                f.close()
                print("{} is saved at {}".format(name, root))
        else:
            print("{} is already exist".format(name))
    except:
        print("failed")
