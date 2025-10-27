# LLMs

## 🛠 Step 1: Create a Virtual Environment

Navigate to your project folder in the terminal or command prompt:

```bash
cd path/to/your/project
```

Then run one of these commands:

### On **Windows**

```bash
python -m venv venv
```

### On **macOS / Linux**

```bash
python3 -m venv venv
```

---

## 🚀 Step 3: Activate the Virtual Environment

### On **Windows (CMD)**

```bash
venv\Scripts\activate
```

### On **Windows (PowerShell)**

```bash
.\venv\Scripts\Activate.ps1
```

### On **macOS / Linux**

```bash
source venv/bin/activate
```

## 🧹 Step 4: Deactivate When Done

When you’re finished working:

```bash
deactivate
```

---

## 🧰 Optional: Installing Dependencies

Once your virtual environment is active, you can install packages like this:

```bash
pip install numpy pandas
```

And save them to a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Later, you (or someone else) can install them again using:

```bash
pip install -r requirements.txt
```


