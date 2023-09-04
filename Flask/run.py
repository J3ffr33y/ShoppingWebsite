# Author: J3FFREY WANG
# Date: 28/7/23

from market import app

# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)
