# Clank 

Example Python Click CLI

# Usage

```
# Create a virtual environment
pip install virtualenv
python3 -m venv venv
source venv/bin/activate

# Install the necessary python packages
pip install -r requirements.txt
pip install --editable .
```

```
clankcli clank texter "Hello"
clankcli clank blinker "Hello"
clankcli clank underliner "Hello"
clankcli clank bolder "Hello"
clankcli clank chooser "Hello" --c "red"

clankcli heliopad --t "Lets go" --n 10
```