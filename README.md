# texqlite
Converts text file to sqlite db.
I was looking for some software to do this, but many people said that I should just make my own custom script. So I did, but I've made this for a bit more wide use. You can tell script what the data separator string is. 
I'll add few more features if I can. PRs are highly appreciated!

# Installation
It's your choice. Just clone this repo, and use them. It would be easier to use if you copy the script into your PATH directory such as `/usr/local/bin`. 

# Usage.
* **Method 1:** Start using by `./texqlite -i`. This will open an interactive mode! 
* **Method 2:** To do it quickly, use this command: `./texqlite sample.txt`. And texqlite will just run by default setting. 
Currently, Method 2 is not supporting the multiple fields. It will be added soon. 
 
# Requirements
sqlite3 

