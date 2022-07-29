# waterdrop
Waterdrop is a celebration of the good actors in the blockchain space.


## Running it
0. (install python & node.js locally)
1. git clone ```https://github.com/ProphetFund/waterdrop.git```
2. create virtual environment: ```python -m venv venv``` 
Comment: isn't this ```python -m venv .venv```? 

3. activate python environment &  install all dependencies: ```source venv/bin/activate && pip install -r requirements.txt```
4. change directory to app ```cd app```
4. install npm dependencies ```npm install```
4. run app: ```python app.py``` or ```npm run run``` or ```gunicorn app:app``` (all work lol)
5. navigate to http://127.0.0.1:5000/

Comment: ```npm run build-css``` and in new terminal ```python app.py```


### TODO
Remaining tasks for waterdrop (& completion rates):
    - blockchain: 50% done
        - files pinned as permanent storage on ipfs: 100%
        - figure out minting allowlist: 40%, 2-4hours. Not really sure on this one. Alternative is just plain code it in and deploy on Polygon. That way we also qualify for the polygon track. Negative is that nfts are worth much less.
        - deploy contract:
            - (with no merkle tree on ETH L1 this is ~20$, not a lot. With allowlist it can get humongous, i dont know how much merkle tree saves yet.) 0% done, 15mins
    - frontend: 80% done
        - add mint functionality 0%, (1-2 hours)
        - optional: load more button
    - logistics:
        - writeup: 0% (1.5 hr)
    - data:
        - final cleanup of addresses (and adding polygon faucets if we deploy there): 90% done, 30mins